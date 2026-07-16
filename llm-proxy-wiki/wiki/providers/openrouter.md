---
title: "OpenRouter"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 9
summary: "A managed model aggregator that exposes hundreds of models and providers through one API and account."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "openrouter"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:openrouter-official"]
---

## Positioning

A managed model aggregator that exposes hundreds of models and providers through one API and account.

## Deployment

Managed SaaS.

## License and commercial model

Commercial service; client examples and documentation are open, but the routing service is not a self-hosted core.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | No |
| Managed option | Only |
| Routing/fallback | Strong |
| Caching | Yes |
| Budgets/keys | Account/workspace controls |
| Observability | Yes + broadcasts |
| Kubernetes | N/A |

## Strengths

- Very fast access to a broad model marketplace through an OpenAI-compatible endpoint.
- Provider selection, automatic fallbacks, response caching, BYOK options, and privacy controls.
- Useful routing metadata and integrations for external observability.
- Low setup cost for experiments and products that need many commercial models.

## Limitations and risks

- No self-hosted data plane for the core service.
- Adds an aggregator dependency and commercial fee model.
- Enterprise governance is less infrastructure-native than running a gateway inside the organization's network.

## Best fit

Best for fast multi-model experimentation and small teams that value breadth and convenience over infrastructure ownership.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Quickstart](https://openrouter.ai/docs/quickstart)
- [Models](https://openrouter.ai/docs/guides/overview/models)
- [Provider routing](https://openrouter.ai/docs/guides/routing/provider-selection)
- [Pricing](https://openrouter.ai/pricing)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
