---
title: "TrueFoundry AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 11
summary: "An enterprise AI gateway and governance platform for public, private, and hybrid model infrastructure."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "truefoundry"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:truefoundry-official"]
---

## Positioning

An enterprise AI gateway and governance platform for public, private, and hybrid model infrastructure.

## Deployment

SaaS, hybrid, and fully self-hosted modes.

## License and commercial model

Commercial enterprise platform.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Yes |
| Routing/fallback | Strong |
| Caching | Yes |
| Budgets/keys | Strong |
| Observability | Strong + OTEL |
| Kubernetes | Strong |

## Strengths

- Strong hybrid and private-model story with self-hosted gateway planes.
- Virtual models, routing, caching, prompt management, request logging, guardrails, rate limits, and OpenTelemetry export.
- Enterprise identity and policy integrations.
- Good fit for organizations operating both provider APIs and internal inference.

## Limitations and risks

- Heavier platform commitment than a thin proxy.
- Pricing and procurement are enterprise oriented.
- Teams should separate required gateway functions from optional platform features.

## Best fit

Best for enterprises needing one governance layer across private model clusters and external providers.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Product](https://www.truefoundry.com/ai-gateway)
- [Introduction](https://www.truefoundry.com/docs/ai-gateway/intro-to-llm-gateway)
- [Deployment modes](https://www.truefoundry.com/docs/ai-gateway/modes-of-deployment)
- [Self-hosted models](https://www.truefoundry.com/docs/ai-gateway/self-hosted-models)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
