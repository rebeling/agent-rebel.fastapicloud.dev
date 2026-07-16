---
title: "AISIX AI Gateway"
type: provider
section: Providers
section_title: Providers
section_order: 7
nav_order: 2
summary: "A Rust-native open-source gateway from API7 for LLM and agent traffic."
status: reviewed
updated: 2026-07-14
tags: ["provider", "llm-proxy", "aisix"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:aisix-official"]
---

## Positioning

A Rust-native open-source gateway from API7 for LLM and agent traffic.

## Deployment

Self-hosted single binary and managed cloud options.

## License and commercial model

Open-source core with commercial managed service.

## Capability snapshot

| Capability | Assessment |
|---|---|
| Self-hosted | Yes |
| Managed option | Yes |
| Routing/fallback | Yes |
| Caching | Yes/documented capabilities |
| Budgets/keys | Rate and policy controls |
| Observability | Logs/audit/metrics |
| Kubernetes | Supported |

## Strengths

- Low-overhead Rust data plane and simple binary deployment.
- Stable model API, provider routing, security configuration, logging, and auditing.
- Published performance and sizing guidance.
- Attractive for teams that want a focused gateway without a Python runtime.

## Limitations and risks

- Younger project and smaller ecosystem than established gateways.
- Feature depth and extension ecosystem should be validated against production requirements.
- The relationship between open-source and managed capabilities may evolve quickly.

## Best fit

Promising for performance-sensitive self-hosting and teams willing to adopt a newer gateway.

## Evaluation questions

- Does the exact endpoint you need preserve streaming, tools, structured outputs, and usage data?
- Which capabilities are open source, managed-only, or enterprise-only?
- Where do prompts, responses, cache entries, and telemetry live?
- How are provider prices, model capabilities, and security advisories updated?
- What happens when the gateway database, control plane, or analytics backend fails?
- Can the route decision and resolved provider be audited for every request?

## Official links

- [Documentation](https://docs.api7.ai/ai-gateway)
- [Product](https://api7.ai/ai-gateway)
- [Security](https://docs.api7.ai/ai-gateway/deployment/network-and-security)
- [GitHub](https://github.com/api7/aisix)

## Related pages

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Decision Guide](../comparisons/decision-guide.md)
