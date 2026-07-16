---
title: "LLM Proxy Decision Guide"
type: comparison
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 4
summary: "A use-case-driven way to shortlist gateways before running a proof of concept."
status: reviewed
updated: 2026-07-14
tags: ["decision", "selection", "recommendation"]
related: ["wiki/comparisons/feature-matrix.md"]
sources: ["source:litellm-official", "source:portkey-official", "source:helicone-official", "source:openrouter-official", "source:cloudflare-official", "source:vercel-official", "source:kong-official", "source:envoy-official", "source:aisix-official", "source:truefoundry-official", "source:zuplo-official", "source:apisix-official"]
---

## Choose LiteLLM when

- self-hosting is required
- provider breadth is the main requirement
- a Python-based gateway is operationally acceptable
- virtual keys, budgets, routing, and integrations are needed in one baseline

See [Use LiteLLM](../decisions/use-litellm.md).

## Choose Portkey when

- managed AI-native governance is preferred
- guardrails, routing, virtual keys, and observability should be one product
- the team wants an OSS gateway path plus a managed platform

## Choose Helicone when

- the immediate pain is visibility into requests, cost, latency, prompts, and sessions
- gateway consolidation is useful but deep platform networking is not the first requirement

## Choose OpenRouter when

- model breadth and time-to-first-request dominate
- self-hosting is not required
- one account and API should reach many commercial models

## Choose Cloudflare or Vercel when

- the application platform is already Cloudflare Workers or Vercel
- a managed gateway should fit existing deployment, identity, and telemetry workflows

## Choose Kong or APISIX when

- the organization already operates that API gateway
- shared identity, policy, networking, and audit standards matter more than a lightweight AI-only service

## Choose Envoy AI Gateway when

- Kubernetes Gateway API is already part of the platform
- private inference pools and declarative cluster routing are central

## Choose AISIX when

- a small, low-overhead Rust data plane is attractive
- the team accepts a newer ecosystem and will benchmark its required features

## Choose TrueFoundry when

- private models, public providers, hybrid deployment, and enterprise policy must be unified

## Choose Zuplo when

- a programmable edge gateway should cover conventional APIs, LLM APIs, and MCP traffic

## Do not choose yet

Do not select a gateway from a feature matrix alone. Run a proof of concept with real streaming, tools, structured output, failure, privacy, and cost-accounting tests.
