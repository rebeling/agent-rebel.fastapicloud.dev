---
title: "LLM Gateway Observability"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 5
summary: "A gateway is the natural telemetry boundary for model usage, but prompt logging is not automatically safe."
status: reviewed
updated: 2026-07-14
tags: ["observability", "opentelemetry", "cost-tracking"]
related: ["wiki/governance/privacy-and-retention.md", "wiki/failures/cost-accounting-drift.md"]
sources: []
---

## Minimum metrics

- request count and concurrency
- time to first token and total latency
- provider, deployment, region, and resolved model
- input, output, reasoning, cached, and total tokens where available
- provider errors, gateway errors, retries, and fallbacks
- estimated and provider-reported cost
- cache hit rate
- rate-limit and budget rejections
- policy and guardrail outcomes

## Tracing

OpenTelemetry is increasingly common. A useful trace connects:

application request → gateway policy → provider call → tool calls or downstream retrieval.

Record route decisions as structured attributes rather than only free-text logs.

## Prompt and response data

Full payload logging helps debugging and evaluation but creates a sensitive data store. Alternatives include:

- metadata-only logs
- configurable sampling
- redaction
- hashes or fingerprints
- short retention
- tenant-specific opt-in
- customer-controlled storage

Observability must remain useful during provider and gateway incidents. Avoid making the request path synchronously dependent on the analytics backend.
