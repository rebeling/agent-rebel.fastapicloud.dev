---
title: "LLM Gateway Production Readiness"
type: guide
section: Guides
section_title: Guides
section_order: 5
nav_order: 3
summary: "A production gate for a service that becomes a dependency of every AI application."
status: reviewed
updated: 2026-07-14
tags: ["production", "sre", "readiness"]
related: ["wiki/architecture/security-boundary.md", "wiki/failures/proxy-single-point-of-failure.md"]
sources: []
---

## Availability

- at least two data-plane instances
- no single database or cache dependency without recovery
- readiness and liveness checks reflect provider-independent health
- graceful draining for streamed requests
- tested regional or direct-provider fallback where required

## Configuration

- version-controlled routes and policies
- staged rollout and rollback
- secret rotation without downtime
- environment separation
- audit trail for administrative changes

## Reliability

- bounded retries
- circuit breakers
- timeouts per provider and endpoint
- backpressure and concurrency limits
- queue avoidance unless asynchronous semantics are explicit

## Observability

- gateway and provider errors separated
- route and fallback labels
- token and cost metrics
- time to first token
- SLOs and alerts
- trace sampling strategy

## Security

- private admin surface
- least-privilege credentials
- pinned and scanned artifacts
- incident and patch procedure
- prompt/output logging policy
- cache and tenant isolation tests

## Ownership

A named team must own on-call response, upgrades, provider onboarding, policy changes, and cost reconciliation.
