import os
import tempfile
import unittest

from fastapi.testclient import TestClient

from main import app


class RouteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.wiki_tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        os.environ["AGENT_REBEL_WIKI_DIR"] = self.wiki_tmp.name
        os.environ["LLM_PROXY_DB_PATH"] = f"{self.tmp.name}/llm_proxy.db"
        os.environ["LLM_PROXY_WIKI_DIR"] = f"{self.wiki_tmp.name}/llm-proxy"
        os.environ["AGENT_REBEL_EDITABLE"] = "true"
        self.client = TestClient(app)
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()
        self.wiki_tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)
        os.environ.pop("AGENT_REBEL_WIKI_DIR", None)
        os.environ.pop("LLM_PROXY_DB_PATH", None)
        os.environ.pop("LLM_PROXY_WIKI_DIR", None)
        os.environ.pop("AGENT_REBEL_EDITABLE", None)

    def test_landing_lists_both_wikis(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Agent Wiki", response.text)
        self.assertIn("The LLM Proxy Wiki", response.text)
        self.assertIn('href="/agent/"', response.text)
        self.assertIn('href="/llm-proxy/"', response.text)

    def test_unknown_wiki_returns_404(self):
        response = self.client.get("/nope/")
        self.assertEqual(response.status_code, 404)

    def test_legacy_wiki_url_redirects(self):
        response = self.client.get(
            "/wiki/strategies/retrieval-first", follow_redirects=False
        )
        self.assertEqual(response.status_code, 301)
        self.assertEqual(
            response.headers["location"], "/agent/wiki/strategies/retrieval-first"
        )

    def test_homepage_renders_agent_knowledge_base(self):
        response = self.client.get("/agent/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("The Agent Wiki", response.text)
        self.assertIn(
            "A practical map of agent concepts, types, capabilities, memory, protocols, evaluation, and failure modes.",
            response.text,
        )

    def test_page_route_renders_markdown_and_relations(self):
        response = self.client.get("/agent/wiki/strategies/retrieval-first")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Retrieval First", response.text)
        self.assertIn("Outgoing Links", response.text)
        self.assertIn("Backlinks", response.text)

    def test_edit_save_creates_page_and_history(self):
        response = self.client.post(
            "/agent/edit/tests/route-save",
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
        page = self.client.get("/agent/wiki/tests/route-save")
        self.assertEqual(page.status_code, 200)
        self.assertIn("Route Save", page.text)
        history = self.client.get("/agent/history/tests/route-save")
        self.assertIn("Updated tests/route-save.", history.text)

    def test_invalid_okf_returns_editor_error(self):
        response = self.client.post(
            "/agent/edit/tests/bad-okf",
            data={"document": "# Missing frontmatter"},
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("OKF validation", response.text)

    def test_graph_and_lint_routes(self):
        graph = self.client.get("/agent/graph.json")
        self.assertEqual(graph.status_code, 200)
        self.assertIn("nodes", graph.json())
        graph_page = self.client.get("/agent/graph")
        self.assertEqual(graph_page.status_code, 200)
        self.assertIn("Wiki Graph", graph_page.text)
        lint = self.client.get("/agent/lint")
        self.assertEqual(lint.status_code, 200)
        self.assertIn("Lint Report", lint.text)

    def test_source_ingest(self):
        response = self.client.post(
            "/agent/sources",
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
        sources = self.client.get("/agent/sources")
        self.assertIn("Test Source", sources.text)

    def test_download_zip_route(self):
        response = self.client.get("/agent/download-zip")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["content-type"], "application/zip")
        self.assertIn(
            "attachment; filename=the_agent_knowledge_base.zip",
            response.headers["content-disposition"],
        )


class ReadOnlyRouteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.wiki_tmp = tempfile.TemporaryDirectory()
        os.environ["AGENT_REBEL_DB_PATH"] = f"{self.tmp.name}/agent_rebel.db"
        os.environ["AGENT_REBEL_WIKI_DIR"] = self.wiki_tmp.name
        os.environ["LLM_PROXY_DB_PATH"] = f"{self.tmp.name}/llm_proxy.db"
        os.environ["LLM_PROXY_WIKI_DIR"] = f"{self.wiki_tmp.name}/llm-proxy"
        os.environ.pop("AGENT_REBEL_EDITABLE", None)
        self.client = TestClient(app)
        self.client.__enter__()

    def tearDown(self):
        self.client.__exit__(None, None, None)
        self.tmp.cleanup()
        self.wiki_tmp.cleanup()
        os.environ.pop("AGENT_REBEL_DB_PATH", None)
        os.environ.pop("AGENT_REBEL_WIKI_DIR", None)
        os.environ.pop("LLM_PROXY_DB_PATH", None)
        os.environ.pop("LLM_PROXY_WIKI_DIR", None)

    def test_page_keeps_disabled_edit_button(self):
        response = self.client.get("/agent/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'type="button" disabled title="Editing is disabled"', response.text
        )
        self.assertIn(">Edit</button>", response.text)

    def test_sources_keeps_disabled_ingest_button(self):
        response = self.client.get("/agent/sources")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Source OKF", response.text)
        self.assertIn('disabled title="Source ingest is disabled"', response.text)
        self.assertIn(">Ingest Source</button>", response.text)

    def test_edit_route_still_forbidden(self):
        response = self.client.get("/agent/edit/index")
        self.assertEqual(response.status_code, 403)

    def test_fastapi_docs_are_hidden_by_default(self):
        self.assertEqual(self.client.get("/docs").status_code, 404)
        self.assertEqual(self.client.get("/redoc").status_code, 404)
        self.assertEqual(self.client.get("/openapi.json").status_code, 404)


if __name__ == "__main__":
    unittest.main()
