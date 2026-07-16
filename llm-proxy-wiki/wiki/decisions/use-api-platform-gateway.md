---
title: "Decision: Extend the Existing API Gateway"
type: decision
section: Decisions
section_title: Decisions
section_order: 8
nav_order: 3
summary: "Use Kong, APISIX, or a similar platform when AI traffic should inherit established API governance."
status: reviewed
updated: 2026-07-14
tags: ["decision", "api-gateway", "platform"]
related: ["wiki/providers/kong-ai-gateway.md", "wiki/providers/apache-apisix.md", "wiki/providers/envoy-ai-gateway.md"]
sources: []
---

## Good conditions

- the organization already operates a shared gateway
- identity, audit, network, and policy standards are mature
- platform teams can build and maintain AI-specific plugins and policies
- Kubernetes or hybrid connectivity is important

## Benefits

- fewer infrastructure stacks
- consistent service identity and audit
- reuse of deployment and incident processes
- integration with existing observability and security systems

## Risks

- AI semantics may be forced into generic API abstractions
- plugin and edition boundaries can be complex
- model metadata, token accounting, streaming, and prompt policies require specialized testing
- application teams may experience slower onboarding than with an AI-native SaaS
