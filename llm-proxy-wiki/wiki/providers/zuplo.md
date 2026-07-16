---
title: "Zuplo AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 13
summary: "A programmable managed edge gateway covering API, AI, and MCP traffic."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "zuplo"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:zuplo-official"]
---

## Positioning

A programmable managed edge gateway covering API, AI, and MCP traffic.

## Deployment

Managed edge, dedicated managed environments, and self-hosted Kubernetes options.

## License and commercial model

Commercial platform.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Commercial option |
| Managed option | Yes |
| Routing/fallback | Yes |
| Caching | Yes |
| Budgets/keys | Strong API controls |
| Observability | Strong/integrations |
| Kubernetes | Self-hosted option |

## Strengths

- Developer-oriented GitOps workflow and programmable policy layer.
- Multi-provider gateway, fallbacks, caching, auth, rate limiting, spend controls, and tracing integrations.
- Combines general API management with AI and MCP governance.
- Clear path from managed edge to dedicated or self-hosted deployments.

## Limitations and risks

- Not an open-source gateway core.
- Custom-provider compatibility should be checked for non-OpenAI schemas.
- Best value comes from adopting Zuplo's broader API platform.

## Best fit

Best for teams wanting a programmable edge gateway that unifies conventional APIs, LLM APIs, and MCP endpoints.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Product](https://zuplo.com/ai-gateway)
- [Documentation](https://zuplo.com/docs/ai-gateway/introduction)
- [Fallbacks](https://zuplo.com/docs/ai-gateway/fallback)
- [Self-hosting](https://zuplo.com/docs/self-hosted/overview)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
