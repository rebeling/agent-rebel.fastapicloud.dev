---
title: "Helicone"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 6
summary: "An observability-first LLM platform that also provides an OpenAI-compatible multi-provider gateway."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "helicone"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:helicone-official"]
---

## Positioning

An observability-first LLM platform that also provides an OpenAI-compatible multi-provider gateway.

## Deployment

Managed cloud and self-hosted deployments.

## License and commercial model

Open-source components plus paid managed plans.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Yes |
| Routing/fallback | Yes |
| Caching | Yes |
| Budgets/keys | Rate limits/controls |
| Observability | Excellent |
| Kubernetes | Yes |

## Strengths

- Strong request analytics, cost tracking, prompt and session analysis, and operational visibility.
- Gateway routing, caching, custom rate limits, and prompt integration.
- Useful when observability is the first problem and gateway consolidation is the second.
- Self-hosting remains possible.

## Limitations and risks

- Some teams may still pair it with another gateway if they need deeper enterprise policy or platform networking.
- Payload logging and retention require deliberate privacy configuration.
- Feature boundaries between gateway and broader observability platform should be tested.

## Best fit

Best for product teams that want gateway and observability in one system with low integration friction.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Gateway overview](https://docs.helicone.ai/gateway/overview)
- [Platform overview](https://docs.helicone.ai/getting-started/platform-overview)
- [Self-hosting](https://docs.helicone.ai/getting-started/self-host/overview)
- [GitHub](https://github.com/helicone/helicone)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
