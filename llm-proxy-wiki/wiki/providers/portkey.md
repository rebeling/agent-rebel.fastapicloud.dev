---
title: "Portkey"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 10
summary: "An AI-native gateway with an open-source data path and a managed platform for routing, guardrails, observability, and governance."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "portkey"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:portkey-official"]
---

## Positioning

An AI-native gateway with an open-source data path and a managed platform for routing, guardrails, observability, and governance.

## Deployment

Hosted service or self-hosted open-source gateway; enterprise deployment options are available.

## License and commercial model

Open-source gateway plus commercial managed and enterprise capabilities.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Yes |
| Routing/fallback | Strong |
| Caching | Yes |
| Budgets/keys | Strong |
| Observability | Strong |
| Kubernetes | Yes/enterprise |

## Strengths

- Composable routing with retries, fallbacks, load balancing, conditional logic, and caching.
- Virtual keys, rate limits, budgets, guardrails, and organization-level governance.
- Large provider/model catalog and production-oriented managed experience.
- Good balance between AI-specific features and reduced operational burden.

## Limitations and risks

- The complete platform experience extends beyond the open-source gateway.
- Teams should verify which controls are available in self-hosted, managed, and enterprise plans.
- A richer policy surface creates more configuration and testing work.

## Best fit

Strong managed-governance choice for organizations that want AI-native controls without building a platform around an OSS proxy.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Introduction](https://docs.portkey.ai/docs/introduction/what-is-portkey)
- [AI Gateway](https://docs.portkey.ai/docs/product/ai-gateway)
- [Feature overview](https://docs.portkey.ai/docs/introduction/feature-overview)
- [GitHub](https://github.com/Portkey-AI/gateway)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
