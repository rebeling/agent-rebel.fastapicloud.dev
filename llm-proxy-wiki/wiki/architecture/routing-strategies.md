---
title: "LLM Routing Strategies"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 3
summary: "How gateways choose provider deployments, accounts, regions, or model classes."
status: reviewed
updated: 2026-07-14
tags: ["routing", "fallback", "load-balancing"]
related: ["wiki/failures/silent-fallbacks.md", "wiki/examples/routing-policy.md"]
sources: []
---

## Static routing

A virtual model always maps to one backend. It is simple, predictable, and easy to audit.

## Weighted load balancing

Traffic is distributed across deployments or providers by configured weights. Use it for quota distribution and controlled migration.

## Health and error-aware fallback

The gateway switches after timeouts, quota errors, or selected 5xx responses. Fallback rules must distinguish transient infrastructure failure from invalid requests.

## Latency-aware routing

The gateway selects a backend based on recent latency. This can reduce response time but may oscillate without smoothing and minimum sample sizes.

## Cost-aware routing

The gateway prefers cheaper backends that satisfy capability and policy constraints. It requires reliable, current pricing metadata.

## Region and residency routing

Routes are constrained by geography, provider region, or data policy.

## Capability routing

A request is sent only to models supporting required features such as tools, vision, JSON schema, long context, or zero data retention.

## Semantic routing

A classifier or model chooses a model class based on prompt difficulty or topic. This can save cost but introduces another model, another evaluation problem, and possible misrouting.

## Rule

Routing should be observable. Every response should reveal the chosen backend, route reason, fallback count, and policy version to authorized operators.
