---
title: "Cloudflare AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 4
summary: "A managed edge gateway for controlling and observing model traffic through Cloudflare infrastructure."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "cloudflare-ai-gateway"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:cloudflare-official"]
---

## Positioning

A managed edge gateway for controlling and observing model traffic through Cloudflare infrastructure.

## Deployment

Managed Cloudflare service, integrated with Workers and Cloudflare's edge.

## License and commercial model

Commercial managed platform with core gateway features available through Cloudflare plans.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | No |
| Managed option | Only |
| Routing/fallback | Strong |
| Caching | Yes |
| Budgets/keys | Spend/rate controls |
| Observability | Strong + OTEL |
| Kubernetes | N/A |

## Strengths

- Edge proximity, global network integration, and good fit with Workers applications.
- Provider-native and unified API options, custom providers, dynamic routing, fallbacks, caching, rate limits, and spend limits.
- Central logs, cost analytics, and OpenTelemetry export.
- BYOK and unified billing options.

## Limitations and risks

- Cloudflare-centric operations and configuration.
- Not a general self-hosted gateway.
- Teams must validate exact compatibility across unified and provider-native request paths.

## Best fit

Best for teams already building on Cloudflare Workers or wanting a globally managed edge control point.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Overview](https://developers.cloudflare.com/ai-gateway/)
- [Features](https://developers.cloudflare.com/ai-gateway/features/)
- [REST API](https://developers.cloudflare.com/ai-gateway/usage/rest-api/)
- [Custom providers](https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
