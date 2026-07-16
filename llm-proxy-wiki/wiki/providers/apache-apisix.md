---
title: "Apache APISIX AI Gateway Capabilities"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 3
summary: "AI-specific plugins on the Apache APISIX cloud-native API gateway."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "apache-apisix"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:apisix-official"]
---

## Positioning

AI-specific plugins on the Apache APISIX cloud-native API gateway.

## Deployment

Self-hosted, commonly with Docker or Kubernetes; commercial API7 offerings are also available.

## License and commercial model

Apache open source for APISIX; commercial API7 products are separate.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | API7 |
| Routing/fallback | Strong gateway routing |
| Caching | Gateway/plugin options |
| Budgets/keys | Rate/policy controls |
| Observability | Strong |
| Kubernetes | Strong |

## Strengths

- Mature dynamic API gateway with high-performance routing and a plugin architecture.
- AI proxy and multi-provider plugins, token-aware rate limiting, prompt guard, cost observability, content moderation, and RAG-related plugins.
- Strong fit when APISIX is already deployed.
- Open-source and infrastructure-oriented.

## Limitations and risks

- AI functionality is plugin-based rather than a single integrated AI-native product.
- Operational complexity includes APISIX and its configuration store.
- Provider coverage and schema normalization may be narrower than AI-native aggregators.

## Best fit

Best for APISIX users who want to govern model traffic without adding a separate gateway stack.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [APISIX](https://apisix.apache.org/)
- [AI Proxy](https://docs.api7.ai/hub/ai-proxy)
- [AI Proxy Multi](https://docs.api7.ai/hub/ai-proxy-multi)
- [Prompt Guard](https://apisix.apache.org/docs/apisix/plugins/ai-prompt-guard/)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
