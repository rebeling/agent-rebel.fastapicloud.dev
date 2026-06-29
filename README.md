# Agent Rebel

Agent Rebel is a small OKF wiki for AI-agent strategy knowledge. It is a field manual, not a chat app.

The app stores structured knowledge pages, source notes, links, backlinks, revisions, lint results, and graph data in SQLite. It renders pages with FastAPI/Jinja and uses Cytoscape.js for the visual graph.

## Current Scope

- SQLite storage in `data/agent_rebel.db`
- server-rendered FastAPI UI
- OKF document editor
- source ingest as OKF
- page revisions on every save
- `[[wikilink]]` extraction
- outgoing links and backlinks
- broken-link warnings
- lint report
- operation log
- Cytoscape graph visualization
- `/graph.json` graph data

Not included yet:

- LLM calls
- `/ask` endpoint
- vector database
- login or multi-user permissions
- remote publishing
- git-backed content sync

## OKF Page Format

Wiki pages are edited as one OKF document:

```markdown
---
title: Retrieval First
type: strategy
description: Retrieve relevant knowledge before answering or planning.
tags:
  - retrieval
  - context
---

# Retrieval First

Use retrieval before planning when the answer depends on project-specific knowledge.

See [[failures/tool-overuse]].
```

The slug comes from the route, for example `/edit/strategies/retrieval-first`.

## Source OKF Format

Sources are also submitted as OKF:

```markdown
---
title: Test Source
type: note
---

Raw source material.
```

The source slug is derived from `type/title`, for example `note/test-source`.

## Run Locally

Read-only mode:

```bash
uv run python -m fastapi dev
```

Writable local mode:

```bash
AGENT_REBEL_EDITABLE=true uv run python -m fastapi dev
```

Visit http://localhost:8000.

On first startup, the app creates `data/agent_rebel.db` and seeds practical Agent Rebel sample pages.

## Useful Routes

- `/` - wiki homepage and catalog
- `/wiki/{slug}` - rendered page
- `/edit/{slug}` - OKF document editor
- `/history/{slug}` - page revision history
- `/diff/{revision}/{slug}` - revision diff against current page
- `/lint` - validation report
- `/log` - operation log
- `/sources` - source ingest records
- `/graph` - Cytoscape page graph
- `/graph.json` - graph data

## Security Notes

Editing is disabled by default. Set `AGENT_REBEL_EDITABLE=true` only for local development or trusted private deployments.

This MVP does not include login, authorization, CSRF protection, or per-user permissions. Do not expose writable mode on a public internet domain.

The database path can be overridden with `AGENT_REBEL_DB_PATH`. Keep it inside an application data directory and do not point it at sensitive system paths.

No API keys are required. There are no OpenAI, Anthropic, vector database, or cloud provider credentials in the app.

## Vendored Assets

Cytoscape.js is vendored in `app/static/vendor/cytoscape/`.

- version: `3.34.0`
- license: MIT
- runtime path: `/static/vendor/cytoscape/cytoscape.min.js`

## Tests

```bash
uv run python -m unittest discover -s tests -v
```

Tests use a temporary SQLite database and do not modify `data/agent_rebel.db`.
