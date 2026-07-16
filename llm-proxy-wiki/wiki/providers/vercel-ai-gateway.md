---
title: "Vercel AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 12
summary: "A managed unified model API designed around Vercel deployments and the AI SDK ecosystem."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "vercel-ai-gateway"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:vercel-official"]
---

## Positioning

A managed unified model API designed around Vercel deployments and the AI SDK ecosystem.

## Deployment

Managed Vercel service.

## License and commercial model

Commercial managed service; the surrounding AI SDK is open source.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | No |
| Managed option | Only |
| Routing/fallback | Strong |
| Caching | Provider-oriented/limited gateway role |
| Budgets/keys | Spend and auth controls |
| Observability | Strong |
| Kubernetes | N/A |

## Strengths

- Excellent developer experience for Vercel and AI SDK users.
- Unified access to many models, provider routing and fallbacks, spend visibility, and observability.
- Support for OpenAI- and Anthropic-oriented client patterns plus Vercel-native authentication.
- Security controls include provider allowlists and zero-data-retention options.

## Limitations and risks

- No general self-hosted gateway data plane.
- Most compelling inside the Vercel ecosystem.
- Less suited than infrastructure gateways for private network model servers and deep custom policy.

## Best fit

Best for application teams already standardized on Vercel and the AI SDK.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Documentation](https://vercel.com/docs/ai-gateway)
- [Models and providers](https://vercel.com/docs/ai-gateway/models-and-providers)
- [Observability and spend](https://vercel.com/docs/ai-gateway/observability-and-spend)
- [Security](https://vercel.com/docs/ai-gateway/security-and-compliance)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
