import os
import tempfile
import unittest

from app.config import edits_enabled
from app.db import connect, init_db
from app.graph import graph_json
from app.lint import lint_all, lint_results
from app.markdown import render_markdown
from app.repository import (
    backlinks,
    get_page,
    grouped_pages,
    outgoing_links,
    revisions,
    save_page,
)
from app.seed import seed_if_empty
from app.okf import OKFError, page_to_okf, parse_okf, parse_source_okf
from app.wikilinks import extract_wikilinks, normalize_slug


class WikiCoreTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.wiki_tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        os.environ["AGENT_REBEL_WIKI_DIR"] = self.wiki_tmp.name
        self.conn = connect()
        init_db(self.conn)
        seed_if_empty(self.conn)

    def tearDown(self):
        self.conn.close()
        self.tmp.cleanup()
        self.wiki_tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)
        os.environ.pop("AGENT_REBEL_WIKI_DIR", None)

    def test_seed_creates_index_and_links(self):
        page = get_page(self.conn, "index")
        assert page is not None
        self.assertEqual(page["title"], "The Agent Wiki")
        links = outgoing_links(self.conn, page["id"])
        self.assertGreaterEqual(len(links), 8)
        self.assertFalse(any(link["is_broken"] for link in links))

    def test_seed_explains_okf_workflow(self):
        self.assertIsNotNone(get_page(self.conn, "knowledge/okf-and-rag"))
        self.assertIsNotNone(get_page(self.conn, "meta/wiki-workflow"))
        self.assertIsNotNone(get_page(self.conn, "protocols/protocols-overview"))
        self.assertIsNotNone(get_page(self.conn, "capabilities/capabilities-overview"))
        self.assertIsNotNone(get_page(self.conn, "memory/context-vs-memory"))
        self.assertIsNotNone(get_page(self.conn, "meta/use-okf"))
        self.assertIsNotNone(get_page(self.conn, "evaluation/evaluation-overview"))
        self.assertIsNotNone(get_page(self.conn, "failures/failure-modes-overview"))
        self.assertIsNotNone(get_page(self.conn, "tools/qdrant"))
        self.assertIsNotNone(get_page(self.conn, "tools/cognee"))
        self.assertIsNotNone(get_page(self.conn, "basics/the-illusion-of-agents"))
        self.assertIsNotNone(get_page(self.conn, "meta/self-describing-wiki"))

    def test_wikilink_extraction_and_slug_safety(self):
        links = extract_wikilinks("[[strategies/retrieval-first|Retrieval first]]")
        self.assertEqual(links[0]["target_slug"], "strategies/retrieval-first")
        self.assertEqual(
            normalize_slug("Strategies Retrieval First"), "strategies-retrieval-first"
        )
        with self.assertRaises(ValueError):
            normalize_slug("../secret")

    def test_render_markdown_linkifies_bare_urls(self):
        html = render_markdown(
            "Visit https://example.com, [Docs](https://docs.example.com), and `https://code.example.com`.",
            set(),
        )
        self.assertIn(
            '<a href="https://example.com" rel="noreferrer">https://example.com</a>,',
            html,
        )
        self.assertIn(
            '<a href="https://docs.example.com" rel="noreferrer">Docs</a>',
            html,
        )
        self.assertIn("<code>https://code.example.com</code>", html)

    def test_render_markdown_tables(self):
        html = render_markdown(
            "| Product | Self-host |\n|---|---:|\n| [LiteLLM](../providers/litellm.md) | yes |\n| Kong | no |",
            {"providers/litellm"},
            base_slug="comparisons/feature-matrix",
        )
        self.assertIn('<div class="table-wrap"><table>', html)
        self.assertIn('<th style="text-align:left">Product</th>', html)
        self.assertIn('<th style="text-align:right">Self-host</th>', html)
        self.assertIn(
            '<a class="wiki-link" href="/agent/wiki/providers/litellm">LiteLLM</a>',
            html,
        )
        self.assertIn('<td style="text-align:left">Kong</td>', html)

    def test_render_markdown_mermaid_block(self):
        html = render_markdown(
            "```mermaid\nflowchart TD\n    A --> B\n```",
            set(),
        )
        self.assertIn('<pre class="mermaid">flowchart TD\n    A --&gt; B</pre>', html)
        self.assertNotIn("<code>", html)

    def test_render_markdown_plain_code_block_unchanged(self):
        html = render_markdown("```python\nprint(1)\n```", set())
        self.assertIn("<pre><code>print(1)</code></pre>", html)

    def test_resolve_relative_md_links(self):
        from app.markdown import resolve_relative_md_link

        self.assertEqual(
            resolve_relative_md_link(
                "../providers/litellm.md", "comparisons/feature-matrix"
            ),
            "providers/litellm",
        )
        self.assertEqual(
            resolve_relative_md_link(
                "landscape-map.md", "catalog/llm-proxy-knowledge-base"
            ),
            "catalog/landscape-map",
        )
        self.assertIsNone(resolve_relative_md_link("https://example.com/x.md", "a/b"))

    def test_okf_parse_and_serialize(self):
        page = get_page(self.conn, "strategies/retrieval-first")
        assert page is not None
        document = page_to_okf(page)
        parsed = parse_okf(document)
        self.assertEqual(parsed.title, "Retrieval First")
        self.assertEqual(parsed.page_type, "strategy")
        self.assertIn("retrieval", parsed.tags)
        with self.assertRaises(OKFError):
            parse_okf("# Missing frontmatter")

    def test_okf_parse_keeps_navigation_metadata(self):
        parsed = parse_okf(
            """---
title: Ordered Page
type: guide
section: Start
section_title: Start
section_order: 1
nav_order: 2
description: A page with sidebar metadata.
tags:
  - test
---

# Ordered Page
"""
        )
        self.assertEqual(parsed.section, "Start")
        self.assertEqual(parsed.section_title, "Start")
        self.assertEqual(parsed.section_order, 1)
        self.assertEqual(parsed.nav_order, 2)

    def test_grouped_pages_uses_frontmatter_navigation_order(self):
        save_page(
            self.conn,
            slug="ordered/later",
            title="Later",
            page_type="guide",
            section="Ordered",
            section_title="Ordered",
            section_order=-1,
            nav_order=2,
            description="Second ordered page.",
            tags=["test"],
            body_markdown="# Later",
            change_summary="Create later ordered page.",
        )
        save_page(
            self.conn,
            slug="ordered/earlier",
            title="Earlier",
            page_type="guide",
            section="Ordered",
            section_title="Ordered",
            section_order=-1,
            nav_order=1,
            description="First ordered page.",
            tags=["test"],
            body_markdown="# Earlier",
            change_summary="Create earlier ordered page.",
        )
        groups = grouped_pages(self.conn)
        first_group = next(iter(groups.items()))
        self.assertEqual(first_group[0], "Ordered")
        self.assertEqual(
            [page["title"] for page in first_group[1]], ["Earlier", "Later"]
        )

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
        target = get_page(self.conn, "basics/what-is-an-agent")
        assert target is not None
        incoming = backlinks(self.conn, target["id"])
        incoming_slugs = {link["from_slug"] for link in incoming}
        self.assertIn("index", incoming_slugs)

    def test_relation_lists_dedupe_repeated_links_with_counts(self):
        save_page(
            self.conn,
            slug="tests/repeated-links",
            title="Repeated Links",
            page_type="concept",
            description="A page with repeated links.",
            tags=["test"],
            body_markdown="Links to [[index]], [[index|home]], and [[missing/page]] twice: [[missing/page]].",
            change_summary="Create repeated links test.",
        )
        page = get_page(self.conn, "tests/repeated-links")
        assert page is not None
        links = outgoing_links(self.conn, page["id"])
        by_slug = {link["target_slug"]: link for link in links}

        self.assertEqual([link["target_slug"] for link in links].count("index"), 1)
        self.assertEqual(by_slug["index"]["link_count"], 2)
        self.assertEqual(
            [link["target_slug"] for link in links].count("missing/page"), 1
        )
        self.assertEqual(by_slug["missing/page"]["link_count"], 2)
        self.assertTrue(by_slug["missing/page"]["is_broken"])

        index = get_page(self.conn, "index")
        assert index is not None
        incoming = backlinks(self.conn, index["id"])
        repeated = [
            link for link in incoming if link["from_slug"] == "tests/repeated-links"
        ]
        self.assertEqual(len(repeated), 1)
        self.assertEqual(repeated[0]["link_count"], 2)

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
        assert page is not None
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
