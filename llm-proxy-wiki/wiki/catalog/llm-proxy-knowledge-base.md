---
title: "The LLM Proxy Knowledge Base"
type: catalog
section: Compare & Decide
section_title: Compare & Decide
section_order: 4
nav_order: 6
summary: "A structured reference for choosing, designing, operating, and evaluating LLM proxies and AI gateways."
status: reviewed
updated: 2026-07-14
tags: ["llm-proxy", "ai-gateway", "catalog"]
related: ["wiki/catalog/landscape-map.md", "wiki/comparisons/decision-guide.md"]
sources: []
---

LLM applications increasingly depend on several model providers, private model servers, and policy systems. An LLM proxy creates one controlled boundary between applications and those backends.

Use this wiki as a field manual rather than a vendor leaderboard. The key question is not simply which gateway has the most features. The key question is **where reliability, policy, cost control, and data governance should live**.

## Explore the field

### Concepts

- [What Is an LLM Proxy?](../concepts/what-is-an-llm-proxy.md)
- [Proxy, Gateway, Router, and Aggregator](../concepts/proxy-gateway-router.md)
- [Control Plane and Data Plane](../concepts/control-plane-data-plane.md)
- [Provider Abstraction](../concepts/provider-abstraction.md)

### Architecture and governance

- [Request Lifecycle](../architecture/request-lifecycle.md)
- [Deployment Patterns](../architecture/deployment-patterns.md)
- [Routing Strategies](../architecture/routing-strategies.md)
- [Caching](../architecture/caching.md)
- [Observability](../architecture/observability.md)
- [Security Boundary](../architecture/security-boundary.md)
- [Authentication and Virtual Keys](../governance/authentication-and-keys.md)
- [Rate Limits and Budgets](../governance/rate-limits-and-budgets.md)
- [Privacy and Retention](../governance/privacy-and-retention.md)

### Compare and decide

- [Feature Matrix](../comparisons/feature-matrix.md)
- [Deployment Matrix](../comparisons/deployment-matrix.md)
- [Licensing and Commercial Models](../comparisons/licensing-and-commercial-models.md)
- [Decision Guide](../comparisons/decision-guide.md)
- [Landscape Map](landscape-map.md)

### Operate safely

- [Evaluation Checklist](../guides/evaluation-checklist.md)
- [Migration from Direct Provider Calls](../guides/migration-from-direct-provider.md)
- [Production Readiness](../guides/production-readiness.md)
- [Failure Modes](../failures/proxy-single-point-of-failure.md)

## Core position

A gateway should make provider changes cheaper, failures more visible, access more governable, and spend more attributable. If it merely inserts another opaque network hop, it has not earned its place.
