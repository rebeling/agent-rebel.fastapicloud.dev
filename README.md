# Agent Rebel

Agent Rebel is a small writable wiki for AI-agent strategy knowledge.

The MVP is intentionally boring:

- SQLite storage in `data/agent_rebel.db`
- server-rendered FastAPI UI
- editable OKF wiki pages
- page revisions on every save
- `[[wikilink]]` extraction
- outgoing links and backlinks
- broken-link warnings
- lint report
- source ingest records
- graph visualization and graph JSON

There are no LLM calls, chat endpoints, vector databases, login flows, or multi-user permissions yet.

## Run Locally

```bash
uv run python -m fastapi dev
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
- `/sources` - raw source ingest records
- `/graph` - visual page graph
- `/graph.json` - page graph data

## Tests

```bash
uv run python -m unittest discover -s tests -v
```

Tests use a temporary SQLite database and do not modify `data/agent_rebel.db`.
