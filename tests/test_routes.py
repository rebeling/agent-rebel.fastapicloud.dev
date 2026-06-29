import os
import tempfile
import unittest

from fastapi.testclient import TestClient

from main import app


class RouteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        os.environ["AGENT_REBEL_EDITABLE"] = "true"
        self.client = TestClient(app)
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)
        os.environ.pop("AGENT_REBEL_EDITABLE", None)

    def test_homepage_renders_agent_rebel(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Agent Rebel", response.text)
        self.assertIn("Strategy, knowledge, and failure modes for AI agents", response.text)

    def test_page_route_renders_markdown_and_relations(self):
        response = self.client.get("/wiki/strategies/retrieval-first")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Retrieval First", response.text)
        self.assertIn("Outgoing Links", response.text)
        self.assertIn("Backlinks", response.text)

    def test_edit_save_creates_page_and_history(self):
        response = self.client.post(
            "/edit/tests/route-save",
            data={
                "document": """---
title: Route Save
type: concept
description: Saved through the editor route.
tags:
  - test
  - route
---

# Route Save

Links to [[index]].
""",
            },
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)
        page = self.client.get("/wiki/tests/route-save")
        self.assertEqual(page.status_code, 200)
        self.assertIn("Route Save", page.text)
        history = self.client.get("/history/tests/route-save")
        self.assertIn("Updated tests/route-save.", history.text)

    def test_invalid_okf_returns_editor_error(self):
        response = self.client.post(
            "/edit/tests/bad-okf",
            data={"document": "# Missing frontmatter"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("OKF validation", response.text)

    def test_graph_and_lint_routes(self):
        graph = self.client.get("/graph.json")
        self.assertEqual(graph.status_code, 200)
        self.assertIn("nodes", graph.json())
        graph_page = self.client.get("/graph")
        self.assertEqual(graph_page.status_code, 200)
        self.assertIn("Wiki Graph", graph_page.text)
        lint = self.client.get("/lint")
        self.assertEqual(lint.status_code, 200)
        self.assertIn("Lint Report", lint.text)

    def test_source_ingest(self):
        response = self.client.post(
            "/sources",
            data={
                "document": """---
title: Test Source
type: note
---

Raw source material.
""",
            },
            follow_redirects=False,
        )
        self.assertEqual(response.status_code, 303)
        sources = self.client.get("/sources")
        self.assertIn("Test Source", sources.text)


class ReadOnlyRouteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        os.environ.pop("AGENT_REBEL_EDITABLE", None)
        self.client = TestClient(app)
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)

    def test_page_keeps_disabled_edit_button(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('type="button" disabled title="Editing is disabled"', response.text)
        self.assertIn(">Edit</button>", response.text)

    def test_sources_keeps_disabled_ingest_button(self):
        response = self.client.get("/sources")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Source OKF", response.text)
        self.assertIn('disabled title="Source ingest is disabled"', response.text)
        self.assertIn(">Ingest Source</button>", response.text)

    def test_edit_route_still_forbidden(self):
        response = self.client.get("/edit/index")
        self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main()
