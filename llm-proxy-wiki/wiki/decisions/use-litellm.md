---
title: "Decision: Use LiteLLM as the Self-Hosted Baseline"
type: decision
section: Decisions
section_title: Decisions
section_order: 8
nav_order: 1
summary: "Use LiteLLM when broad provider support and self-hosted control outweigh the cost of operating the gateway."
status: reviewed
updated: 2026-07-14
tags: ["decision", "litellm", "self-hosted"]
related: ["wiki/providers/litellm.md", "wiki/guides/production-readiness.md"]
sources: ["source:litellm-official"]
---

## Context

The organization needs one endpoint for multiple providers and private OpenAI-compatible model servers. It needs routing, fallbacks, virtual keys, cost tracking, and integrations without adopting a large API-management platform.

## Decision

Use LiteLLM as the initial self-hosted baseline.

## Consequences

### Positive

- fastest path to broad provider abstraction
- large ecosystem and documentation surface
- compatible with existing OpenAI clients
- suitable for Docker and Kubernetes
- supports incremental adoption

### Negative

- the team owns patching, scaling, database availability, and security response
- enterprise capabilities may require licensing
- provider-specific behavior still requires tests
- the gateway becomes production infrastructure

## Guardrails

- pin and verify release artifacts
- keep a provider-native escape hatch
- maintain endpoint compatibility tests
- reconcile cost estimates with invoices
- deploy high availability before making it a shared dependency
