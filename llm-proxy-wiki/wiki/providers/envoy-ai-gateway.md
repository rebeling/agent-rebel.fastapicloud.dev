---
title: "Envoy AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 5
summary: "An open-source AI traffic layer built on Envoy Gateway and Kubernetes Gateway API."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "envoy-ai-gateway"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:envoy-official"]
---

## Positioning

An open-source AI traffic layer built on Envoy Gateway and Kubernetes Gateway API.

## Deployment

Self-hosted, primarily Kubernetes-native.

## License and commercial model

Open source.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Ecosystem/vendor dependent |
| Routing/fallback | Strong platform routing |
| Caching | Available through gateway capabilities |
| Budgets/keys | Policy/rate focus |
| Observability | Metrics/OTEL ecosystem |
| Kubernetes | Native |

## Strengths

- Clean integration with Envoy Gateway, Gateway API, and platform-engineering workflows.
- OpenAI- and Anthropic-compatible interfaces, provider routing, metrics, token-aware rate controls, and extensible policy.
- Good fit for shared cluster infrastructure and private inference pools.
- Separates application integration from provider topology.

## Limitations and risks

- Requires Kubernetes and Gateway API expertise for the intended deployment model.
- Younger ecosystem than Kong or LiteLLM.
- Less turnkey for teams seeking a hosted dashboard and billing aggregation.

## Best fit

Best open-source choice for Kubernetes platform teams that already use Envoy or Gateway API.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Documentation](https://aigateway.envoyproxy.io/docs/)
- [Architecture](https://aigateway.envoyproxy.io/blog/envoy-ai-gateway-reference-architecture/)
- [Security](https://aigateway.envoyproxy.io/docs/capabilities/security/)
- [GitHub](https://github.com/envoyproxy/ai-gateway)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
