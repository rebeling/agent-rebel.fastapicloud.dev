---
title: "LLM Proxy Feature Matrix"
type: comparison
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 1
summary: "A high-level capability comparison; it is a screening tool, not a substitute for endpoint-level testing."
status: reviewed
updated: 2026-07-14
tags: ["comparison", "features", "matrix"]
related: ["wiki/comparisons/deployment-matrix.md", "wiki/comparisons/decision-guide.md"]
sources: ["source:litellm-official", "source:portkey-official", "source:helicone-official", "source:openrouter-official", "source:cloudflare-official", "source:vercel-official", "source:kong-official", "source:envoy-official", "source:aisix-official", "source:truefoundry-official", "source:zuplo-official", "source:apisix-official"]
---

| Product | Category | Self-host | Managed | Unified/OpenAI API | Routing & fallback | Cache | Keys / budgets | Observability | K8s fit |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [LiteLLM](../providers/litellm.md) | AI-native OSS/hybrid | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Portkey](../providers/portkey.md) | AI-native OSS/managed | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Helicone](../providers/helicone.md) | Observability-first | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | ✓ |
| [OpenRouter](../providers/openrouter.md) | Managed aggregator | — | ✓ | ✓ | ✓ | ✓ | △ | ✓ | — |
| [Cloudflare](../providers/cloudflare-ai-gateway.md) | Managed edge | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| [Vercel](../providers/vercel-ai-gateway.md) | Managed developer gateway | — | ✓ | ✓ | ✓ | △ | △ | ✓ | — |
| [Kong](../providers/kong-ai-gateway.md) | API platform gateway | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Envoy AI Gateway](../providers/envoy-ai-gateway.md) | K8s-native OSS | ✓ | △ | ✓ | ✓ | △ | △ | ✓ | ✓ |
| [AISIX](../providers/aisix.md) | Rust-native OSS/hybrid | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | ✓ |
| [TrueFoundry](../providers/truefoundry.md) | Enterprise AI platform | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| [Zuplo](../providers/zuplo.md) | Programmable edge/API platform | ✓* | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓* |
| [Apache APISIX](../providers/apache-apisix.md) | API platform with AI plugins | ✓ | ✓* | ✓ | ✓ | △ | ✓ | ✓ | ✓ |

Legend: ✓ strong or clearly documented; △ partial, edition-dependent, indirect, or requires integration; — not a core option; `*` commercial or related product path.


## What this matrix does not prove

A check mark does not establish equal depth. Two gateways may both support fallback while differing in:

- trigger conditions
- nested routing logic
- streaming behavior
- cross-model compatibility
- state and health propagation
- audit metadata
- user interface and API coverage
- open-source versus enterprise availability

The most important proof is an executable test suite against your actual request shapes.

## Broad conclusions

- **LiteLLM** remains the broad self-hosted baseline for provider normalization.
- **Portkey** is strong when managed governance and AI-native routing matter.
- **Helicone** is strongest when observability is the entry point.
- **OpenRouter** optimizes for breadth and speed of access.
- **Cloudflare** and **Vercel** are compelling inside their developer platforms.
- **Kong**, **Envoy**, and **APISIX** fit platform teams that treat AI traffic as shared infrastructure.
- **TrueFoundry** emphasizes private and hybrid enterprise model estates.
- **AISIX** is a newer low-overhead option worth benchmarking.
