---
title: "LLM Gateway Request Lifecycle"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 1
summary: "A reference flow from client authentication to provider response and telemetry."
status: reviewed
updated: 2026-07-14
tags: ["request-flow", "architecture", "routing"]
related: ["wiki/architecture/routing-strategies.md", "wiki/architecture/observability.md"]
sources: []
---

A production request commonly follows this path:

```mermaid
flowchart TD
    A[Client request] --> B[Authenticate]
    B --> C[Normalize API schema]
    C --> D[Apply model allowlist, budget, rate and content policies]
    D --> E{Cache hit?}
    E -- yes --> F[Return cached response]
    E -- no --> G[Select route and credentials]
    G --> H[Call provider or private model]
    H --> I{Retry or fallback condition?}
    I -- yes --> G
    I -- no --> J[Stream or return response]
    J --> K[Emit logs, metrics, traces and cost]
    F --> K
```

## Required design decisions

- Does authentication happen before request-body parsing?
- Which errors trigger retries, and which trigger fallback?
- Can a fallback change the model family?
- Are streamed responses retried after partial output?
- Is cost based on provider usage fields, local tokenization, or estimates?
- Are prompts and outputs logged, redacted, hashed, or omitted?
- What happens when the telemetry sink is unavailable?
- Which policy version handled the request?

The request path should be deterministic enough to audit even when routing is dynamic.
