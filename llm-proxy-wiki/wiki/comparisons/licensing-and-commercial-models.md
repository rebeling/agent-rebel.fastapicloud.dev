---
title: "Licensing and Commercial Models"
type: comparison
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 3
summary: "How open-source cores, managed services, enterprise editions, and model aggregators create different cost structures."
status: reviewed
updated: 2026-07-14
tags: ["licensing", "pricing", "commercial"]
related: ["wiki/governance/rate-limits-and-budgets.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:litellm-official", "source:portkey-official", "source:helicone-official", "source:openrouter-official", "source:cloudflare-official", "source:vercel-official", "source:kong-official", "source:envoy-official", "source:aisix-official", "source:truefoundry-official", "source:zuplo-official", "source:apisix-official"]
---

## Open-source core plus enterprise

Examples: LiteLLM, Portkey, Kong, AISIX.

The software can be self-hosted, while advanced governance, support, dashboards, or organizational features may require a commercial license.

**Cost model:** infrastructure + operations + optional enterprise license.

## Open-source observability or gateway plus managed cloud

Example: Helicone.

**Cost model:** self-hosting effort or managed request/usage plan.

## Managed model aggregator

Example: OpenRouter.

The service may charge a platform fee or margin in addition to upstream model costs.

**Cost model:** model usage + aggregator fee, with lower internal operations cost.

## Managed platform gateway

Examples: Cloudflare AI Gateway, Vercel AI Gateway, Zuplo.

**Cost model:** platform plan, request or usage charges, optional billing fees, and upstream model spend.

## Enterprise AI platform

Example: TrueFoundry.

**Cost model:** negotiated platform license plus infrastructure and upstream model spend.

## Procurement questions

- Are gateway and model charges separate?
- Is BYOK cheaper or more governable?
- Which features require enterprise licensing?
- Are logs, traces, seats, or requests billed separately?
- Does self-hosted licensing scale by node, request, token, or organization?
- Can negotiated model prices be represented accurately?
- What support and security-response commitments are included?

Exact prices change quickly. Provider pages intentionally link to official pricing rather than treating this snapshot as a quote.
