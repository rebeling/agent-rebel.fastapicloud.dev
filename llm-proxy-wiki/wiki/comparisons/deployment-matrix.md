---
title: "LLM Proxy Deployment Matrix"
type: comparison
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 2
summary: "A comparison centered on data-plane ownership, managed operation, and infrastructure fit."
status: reviewed
updated: 2026-07-14
tags: ["comparison", "deployment", "kubernetes"]
related: ["wiki/architecture/deployment-patterns.md", "wiki/comparisons/feature-matrix.md"]
sources: ["source:litellm-official", "source:portkey-official", "source:helicone-official", "source:openrouter-official", "source:cloudflare-official", "source:vercel-official", "source:kong-official", "source:envoy-official", "source:aisix-official", "source:truefoundry-official", "source:zuplo-official", "source:apisix-official"]
---

| Product | SaaS data plane | Self-hosted data plane | Hybrid | Docker/simple service | Kubernetes-native | Private model servers |
|---|---:|---:|---:|---:|---:|---:|
| LiteLLM | — | ✓ | △ | ✓ | ✓ | ✓ |
| Portkey | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Helicone | ✓ | ✓ | △ | ✓ | ✓ | ✓ |
| OpenRouter | ✓ | — | BYOK only | — | — | — |
| Cloudflare AI Gateway | ✓ | — | custom HTTPS upstreams | — | — | △ |
| Vercel AI Gateway | ✓ | — | provider/BYOK options | — | — | △ |
| Kong AI Gateway | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Envoy AI Gateway | — | ✓ | ✓ | — | ✓ | ✓ |
| AISIX | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| TrueFoundry | ✓ | ✓ | ✓ | △ | ✓ | ✓ |
| Zuplo | ✓ | commercial | ✓ | △ | commercial | ✓ |
| Apache APISIX | API7 path | ✓ | ✓ | ✓ | ✓ | ✓ |

## Decision rule

Choose the least complex deployment that satisfies:

1. data residency and privacy
2. network access to private models
3. availability target
4. identity and policy integration
5. operator capability
6. procurement and support requirements

Self-hosting is not automatically safer. Managed SaaS is not automatically simpler once enterprise network and compliance requirements are included.
