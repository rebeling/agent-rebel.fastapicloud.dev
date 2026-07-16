---
title: "Example: Minimal LiteLLM Configuration"
type: example
section: Examples
section_title: Examples
section_order: 9
nav_order: 1
summary: "A small configuration showing virtual model names and two provider deployments."
status: reviewed
updated: 2026-07-14
tags: ["example", "litellm", "yaml"]
related: ["wiki/providers/litellm.md", "wiki/architecture/routing-strategies.md"]
sources: ["source:litellm-official"]
---

```yaml
model_list:
  - model_name: general-fast
    litellm_params:
      model: openai/gpt-4.1-mini
      api_key: os.environ/OPENAI_API_KEY

  - model_name: general-fast
    litellm_params:
      model: anthropic/claude-sonnet-4-5
      api_key: os.environ/ANTHROPIC_API_KEY

router_settings:
  routing_strategy: simple-shuffle
  num_retries: 1
  timeout: 30

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

Run the proxy using the official LiteLLM deployment instructions.

## Production notes

- Do not keep secrets in the file.
- Use a database-backed deployment for shared key and spend state only after its availability design is understood.
- Add fallbacks explicitly rather than assuming same-name deployments are semantically identical.
- Pin a tested LiteLLM version.
- Add observability without making request success depend on the telemetry sink.
