---
title: "LiteLLM"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 8
summary: "An open-source Python SDK and self-hosted OpenAI-compatible proxy with very broad provider support."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "litellm"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:litellm-official"]
---

## Positioning

An open-source Python SDK and self-hosted OpenAI-compatible proxy with very broad provider support.

## Deployment

Self-hosted with local process, Docker, or Kubernetes/Helm; enterprise controls are available separately.

## License and commercial model

Open-source core with commercial enterprise features and support.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Enterprise/support |
| Routing/fallback | Strong |
| Caching | Yes |
| Budgets/keys | Strong |
| Observability | Strong |
| Kubernetes | Yes |

## Strengths

- Very broad provider and model-server coverage, including public clouds and OpenAI-compatible private backends.
- Routing, load balancing, retries, fallbacks, caching, virtual keys, spend tracking, and observability integrations.
- Strong fit for teams that want one self-hosted API across many providers.
- Supports both proxy-server and Python-SDK usage.

## Limitations and risks

- The operator owns availability, database operation, upgrades, security patching, and cost-map accuracy.
- Some governance and organizational features belong to enterprise editions.
- Provider normalization can hide differences unless applications preserve native escape hatches.

## Best fit

Best open-source baseline for a provider-agnostic, self-hosted gateway when Python operations are acceptable.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Documentation](https://docs.litellm.ai/docs/)
- [Proxy](https://docs.litellm.ai/docs/simple_proxy)
- [Providers](https://docs.litellm.ai/docs/providers)
- [GitHub](https://github.com/BerriAI/litellm)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
