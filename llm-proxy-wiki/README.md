# LLM Proxy Knowledge Base

A structured, Markdown-first field guide to LLM proxies, AI gateways, model routers, and multi-provider inference infrastructure.

This repository follows the same small-page approach as the Agent Knowledge Base:

- raw source notes preserve evidence
- typed wiki pages turn evidence into reusable knowledge
- frontmatter makes pages inspectable and graph-friendly
- comparison pages separate facts from recommendations
- decisions, guides, examples, and failure modes make the material operational

## Snapshot

Research snapshot: **2026-07-14**

Provider features, pricing, licenses, and security posture can change. Each provider page links to official documentation and a source note. Re-check current vendor documentation before procurement or production rollout.

## Start here

1. [`wiki/catalog/llm-proxy-knowledge-base.md`](wiki/catalog/llm-proxy-knowledge-base.md)
2. [`wiki/concepts/what-is-an-llm-proxy.md`](wiki/concepts/what-is-an-llm-proxy.md)
3. [`wiki/comparisons/feature-matrix.md`](wiki/comparisons/feature-matrix.md)
4. [`wiki/comparisons/decision-guide.md`](wiki/comparisons/decision-guide.md)

## Directory structure

```text
wiki/
  catalog/       Entry points and landscape maps
  concepts/      Stable definitions
  architecture/  Request flow and deployment patterns
  governance/    Auth, budgets, privacy, and policy
  providers/     One page per product or project
  comparisons/   Matrices and decision support
  decisions/     Explicit architectural choices
  guides/        Evaluation and migration playbooks
  failures/      Common operational and governance failures
  examples/      Minimal configurations and client patterns
  meta/          Methodology and maintenance rules
sources/         Raw official-source notes
schema.yaml      OKF-style frontmatter contract
```

## Page contract

Every wiki page contains YAML frontmatter with:

- `title`
- `type`
- `summary`
- `status`
- `updated`
- `tags`
- `related`
- `sources`

See [`schema.yaml`](schema.yaml) and [`wiki/meta/sources-wiki-schema.md`](wiki/meta/sources-wiki-schema.md).
