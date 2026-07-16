---
title: "The Proxy as a Single Point of Failure"
type: failure
section: Failure Modes
section_title: Failure Modes
section_order: 6
nav_order: 1
summary: "Centralizing every model call creates a new shared failure domain."
status: reviewed
updated: 2026-07-14
tags: ["failure", "availability", "sre"]
related: ["wiki/guides/production-readiness.md", "wiki/concepts/control-plane-data-plane.md"]
sources: []
---

## Failure

Applications that previously called providers independently all fail because the gateway, database, cache, DNS, certificate, or configuration plane is unavailable.

## Prevention

- stateless or horizontally scalable data plane
- highly available state stores
- cached configuration when the control plane is down
- explicit behavior when analytics systems fail
- provider-independent health checks
- capacity and load testing
- direct-provider or secondary-gateway emergency path for critical workloads
- staged rollout rather than immediate organization-wide cutover

Centralization increases leverage and blast radius at the same time.
