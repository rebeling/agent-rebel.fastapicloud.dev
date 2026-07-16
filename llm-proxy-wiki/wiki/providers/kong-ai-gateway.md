---
title: "Kong AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 7
summary: "AI-specific plugins and patterns built on the mature Kong API gateway platform."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "kong-ai-gateway"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:kong-official"]
---

## Positioning

AI-specific plugins and patterns built on the mature Kong API gateway platform.

## Deployment

Self-hosted, Kubernetes, hybrid, or managed through Kong Konnect depending on edition.

## License and commercial model

Open-source Kong Gateway core plus enterprise and managed products; AI capabilities vary by plugin and edition.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Yes |
| Routing/fallback | Strong |
| Caching | Semantic cache |
| Budgets/keys | Strong platform controls |
| Observability | Strong |
| Kubernetes | Excellent |

## Strengths

- Mature API gateway, identity, policy, networking, and plugin ecosystem.
- AI proxying, model routing, semantic caching, prompt templates, prompt and response guards, logging, and OpenTelemetry.
- Strong fit when Kong is already an organizational platform standard.
- Supports public providers and private/OpenAI-compatible backends.

## Limitations and risks

- Higher platform complexity than a thin AI-native proxy.
- The full value often depends on enterprise or Konnect capabilities.
- Plugin compatibility and edition boundaries require careful evaluation.

## Best fit

Best for platform teams that want AI traffic governed through an existing Kong API-management estate.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [AI Gateway](https://developer.konghq.com/ai-gateway/)
- [AI providers](https://developer.konghq.com/ai-gateway/ai-providers/)
- [Cookbooks](https://developer.konghq.com/cookbooks/)
- [GitHub](https://github.com/Kong/kong)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
