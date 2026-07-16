---
title: The LLM Proxy Wiki
type: catalog
section: Home
section_title: Home
section_order: 0
nav_order: 0
description: A structured reference for choosing, designing, operating, and evaluating LLM proxies and AI gateways.
tags: [llm-proxy, ai-gateway, catalog]
status: reviewed
---

A structured reference for choosing, designing, operating, and evaluating LLM proxies and AI gateways.

LLM applications increasingly depend on several model providers, private model servers, and policy systems. An LLM proxy creates one controlled boundary between applications and those backends.

Use this wiki as a field manual rather than a vendor leaderboard. The key question is not simply which gateway has the most features. The key question is **where reliability, policy, cost control, and data governance should live**.

## Explore the field

### Concepts

- [[concepts/what-is-an-llm-proxy|What Is an LLM Proxy?]]
- [[concepts/proxy-gateway-router|Proxy, Gateway, Router, and Aggregator]]
- [[concepts/control-plane-data-plane|Control Plane and Data Plane]]
- [[concepts/provider-abstraction|Provider Abstraction]]

### Architecture and governance

- [[architecture/request-lifecycle|Request Lifecycle]]
- [[architecture/deployment-patterns|Deployment Patterns]]
- [[architecture/routing-strategies|Routing Strategies]]
- [[architecture/caching|Caching]]
- [[architecture/observability|Observability]]
- [[architecture/security-boundary|Security Boundary]]
- [[governance/authentication-and-keys|Authentication and Virtual Keys]]
- [[governance/rate-limits-and-budgets|Rate Limits and Budgets]]
- [[governance/privacy-and-retention|Privacy and Retention]]

### Compare and decide

- [[comparisons/feature-matrix|Feature Matrix]]
- [[comparisons/deployment-matrix|Deployment Matrix]]
- [[comparisons/licensing-and-commercial-models|Licensing and Commercial Models]]
- [[comparisons/decision-guide|Decision Guide]]
- [[catalog/landscape-map|Landscape Map]]

### Operate safely

- [[guides/evaluation-checklist|Evaluation Checklist]]
- [[guides/migration-from-direct-provider|Migration from Direct Provider Calls]]
- [[guides/production-readiness|Production Readiness]]
- [[failures/proxy-single-point-of-failure|Failure Modes]]

## Core position

A gateway should make provider changes cheaper, failures more visible, access more governable, and spend more attributable. If it merely inserts another opaque network hop, it has not earned its place.
