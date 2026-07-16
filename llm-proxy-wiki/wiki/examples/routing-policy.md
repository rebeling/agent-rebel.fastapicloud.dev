---
title: "Example: Routing Policy"
type: example
section: Examples
section_title: Examples
section_order: 9
nav_order: 2
summary: "A vendor-neutral policy for capability, residency, cost, and fallback."
status: reviewed
updated: 2026-07-14
tags: ["example", "routing", "policy"]
related: ["wiki/architecture/routing-strategies.md", "wiki/governance/privacy-and-retention.md"]
sources: []
---

```yaml
virtual_model: private-eu-assistant

constraints:
  regions: [eu]
  zero_data_retention: required
  capabilities:
    tools: required
    structured_output: required

primary:
  provider: azure-openai
  deployment: eu-production

fallbacks:
  - provider: bedrock
    region: eu-central-1
    model_class: equivalent
    on:
      status_codes: [429, 500, 502, 503, 504]
      timeout: true

limits:
  max_input_tokens: 32000
  max_output_tokens: 4000
  retries: 1
  total_attempts: 2

telemetry:
  record_resolved_route: true
  record_prompt: false
  record_response: false
```

The important feature is not the YAML syntax. It is the explicit policy:

- capability constraints are evaluated before cost
- residency is non-negotiable
- fallback is bounded
- cross-class fallback is forbidden
- payload logging is disabled
- route decisions remain observable
