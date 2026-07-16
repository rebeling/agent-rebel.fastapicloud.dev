---
title: "LLM Proxy Landscape Map"
type: catalog
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 5
summary: "A category map of AI-native proxies, managed aggregators, API gateway platforms, and enterprise governance layers."
status: reviewed
updated: 2026-07-14
tags: ["landscape", "categories", "providers"]
related: ["wiki/comparisons/feature-matrix.md", "wiki/providers/adjacent-watchlist.md"]
sources: []
---

## AI-native open-source or hybrid gateways

These products began with model APIs rather than general API management.

- [LiteLLM](../providers/litellm.md): broad provider normalization, self-hosting, routing, budgets, and virtual keys.
- [Portkey](../providers/portkey.md): open-source gateway plus managed governance, guardrails, and observability.
- [Helicone](../providers/helicone.md): observability-first gateway with routing and cost analytics.
- [Envoy AI Gateway](../providers/envoy-ai-gateway.md): Kubernetes and Gateway API oriented.
- [AISIX](../providers/aisix.md): Rust-native data plane focused on low overhead.

## Managed model aggregators and developer gateways

These minimize setup and often centralize provider billing.

- [OpenRouter](../providers/openrouter.md): broad commercial model marketplace and routing layer.
- [Cloudflare AI Gateway](../providers/cloudflare-ai-gateway.md): edge-based gateway integrated with Cloudflare.
- [Vercel AI Gateway](../providers/vercel-ai-gateway.md): tightly integrated with Vercel AI SDK and platform workflows.

## API gateway platforms with AI capabilities

These treat model traffic as another governed API class.

- [Kong AI Gateway](../providers/kong-ai-gateway.md): mature gateway plugins, governance, and enterprise platform integration.
- [Apache APISIX](../providers/apache-apisix.md): general API gateway with AI proxy, prompt guard, token limiting, and related plugins.
- [Zuplo AI Gateway](../providers/zuplo.md): programmable edge gateway spanning API, AI, and MCP traffic.

## Enterprise AI platform gateways

- [TrueFoundry](../providers/truefoundry.md): hybrid and self-hosted enterprise gateway for public and private models.

## Adjacent and watchlist products

Security-first AI gateways, agent/MCP gateways, and model distribution platforms overlap with the category. Examples include NeuralTrust TrustGate, Netskope AI Gateway, WSO2 AI Gateway capabilities, agentgateway, New API, and Zenlayer AI Gateway. They are listed in [Adjacent Projects and Watchlist](../providers/adjacent-watchlist.md) but are not scored in the primary matrices.
