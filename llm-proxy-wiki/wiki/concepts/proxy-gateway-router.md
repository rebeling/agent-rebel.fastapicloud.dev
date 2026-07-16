---
title: "Proxy, Gateway, Router, and Aggregator"
type: concept
section: Concepts
section_title: Concepts
section_order: 1
nav_order: 2
summary: "The terms overlap, but each emphasizes a different responsibility."
status: reviewed
updated: 2026-07-14
tags: ["terminology", "gateway", "router"]
related: ["wiki/catalog/landscape-map.md", "wiki/concepts/what-is-an-llm-proxy.md"]
sources: []
---

| Term | Primary emphasis | Typical capabilities |
|---|---|---|
| Proxy | Intermediating network calls | endpoint translation, authentication, forwarding |
| AI gateway | Central policy and governance boundary | auth, budgets, limits, routing, observability, guardrails |
| Model router | Choosing a backend or model | fallback, load balancing, latency or cost selection, semantic routing |
| Aggregator | One commercial account for many providers | unified billing, model marketplace, provider selection |
| API gateway with AI plugins | Applying existing API-management infrastructure to model traffic | plugins, policies, identity, audit, Kubernetes integration |

A product may belong to several categories. LiteLLM is a proxy and gateway. OpenRouter is an aggregator and router. Kong is an API gateway with AI-specific plugins. TrueFoundry combines gateway and enterprise platform functions.

Use architectural responsibilities, not vendor labels, when comparing products.
