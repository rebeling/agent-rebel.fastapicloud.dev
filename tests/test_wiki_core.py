import os
import tempfile
import unittest

from app.config import edits_enabled
from app.db import connect, init_db
from app.graph import graph_json
from app.lint import lint_all, lint_results
from app.repository import backlinks, get_page, outgoing_links, revisions, save_page
from app.seed import seed_if_empty
from app.okf import OKFError, page_to_okf, parse_okf, parse_source_okf
from app.wikilinks import extract_wikilinks, normalize_slug


class WikiCoreTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        self.conn = connect()
        init_db(self.conn)
        seed_if_empty(self.conn)

    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)

    def test_seed_creates_index_and_links(self):
        page = get_page(self.conn, "index")
        self.assertIsNotNone(page)
        self.assertEqual(page["title"], "Agent Rebel")
        links = outgoing_links(self.conn, page["id"])
        self.assertGreaterEqual(len(links), 8)
        self.assertFalse(any(link["is_broken"] for link in links))

    def test_seed_explains_okf_workflow(self):
        self.assertIsNotNone(get_page(self.conn, "concepts/okf-wiki"))
        self.assertIsNotNone(get_page(self.conn, "guides/ingest-query-lint"))

    def test_wikilink_extraction_and_slug_safety(self):
        links = extract_wikilinks("[[strategies/retrieval-first|Retrieval first]]")
        self.assertEqual(links[0]["target_slug"], "strategies/retrieval-first")
        self.assertEqual(normalize_slug("Strategies Retrieval First"), "strategies-retrieval-first")
        with self.assertRaises(ValueError):
            normalize_slug("../secret")

    def test_okf_parse_and_serialize(self):
        page = get_page(self.conn, "strategies/retrieval-first")
        document = page_to_okf(page)
        parsed = parse_okf(document)
        self.assertEqual(parsed.title, "Retrieval First")
        self.assertEqual(parsed.page_type, "strategy")
        self.assertIn("retrieval", parsed.tags)
        with self.assertRaises(OKFError):
            parse_okf("# Missing frontmatter")

    def test_source_okf_parse(self):
        source = parse_source_okf(
            """---
title: Test Source
type: note
---

Raw material.
"""
        )
        self.assertEqual(source.title, "Test Source")
        self.assertEqual(source.source_type, "note")
        self.assertEqual(source.content, "Raw material.")

    def test_editing_is_disabled_by_default(self):
        os.environ.pop("AGENT_REBEL_EDITABLE", None)
        self.assertFalse(edits_enabled())

    def test_backlinks_are_available(self):
        target = get_page(self.conn, "strategies/retrieval-first")
        incoming = backlinks(self.conn, target["id"])
        incoming_slugs = {link["from_slug"] for link in incoming}
        self.assertIn("index", incoming_slugs)

    def test_broken_links_are_warnings(self):
        save_page(
            self.conn,
            slug="tests/broken-link",
            title="Broken Link Test",
            page_type="concept",
            description="A page with a broken link.",
            tags=["test"],
            body_markdown="This points at [[missing/page]].",
            change_summary="Create broken link test.",
        )
        lint_all(self.conn)
        findings = lint_results(self.conn)
        self.assertTrue(any(item["code"] == "broken-link" for item in findings))
        self.assertTrue(any(item["severity"] == "warning" for item in findings))

    def test_save_creates_revisions(self):
        save_page(
            self.conn,
            slug="tests/revision",
            title="Revision Test",
            page_type="concept",
            description="First version.",
            tags="test",
            body_markdown="First body.",
            change_summary="First save.",
        )
        page = get_page(self.conn, "tests/revision")
        save_page(
            self.conn,
            slug="tests/revision",
            title="Revision Test",
            page_type="concept",
            description="Second version.",
            tags="test",
            body_markdown="Second body.",
            change_summary="Second save.",
        )
        history = revisions(self.conn, page["id"])
        self.assertEqual([item["revision_number"] for item in history], [2, 1])

    def test_graph_json_contains_nodes_and_edges(self):
        graph = graph_json(self.conn)
        self.assertIn("nodes", graph)
        self.assertIn("edges", graph)
        self.assertTrue(any(node["id"] == "index" for node in graph["nodes"]))
        self.assertTrue(any(edge["source"] == "index" for edge in graph["edges"]))


if __name__ == "__main__":
    unittest.main()
