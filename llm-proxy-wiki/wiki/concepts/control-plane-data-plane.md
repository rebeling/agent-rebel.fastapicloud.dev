---
title: "Control Plane and Data Plane"
type: concept
section: Concepts
section_title: Concepts
section_order: 1
nav_order: 3
summary: "A useful split between configuration and the latency-sensitive request path."
status: reviewed
updated: 2026-07-14
tags: ["architecture", "control-plane", "data-plane"]
related: ["wiki/architecture/deployment-patterns.md", "wiki/architecture/security-boundary.md"]
sources: []
---

The **data plane** processes live model requests. It performs authentication, policy checks, routing, forwarding, streaming, and telemetry emission.

The **control plane** manages configuration: providers, credentials, virtual models, users, budgets, policies, dashboards, and audit data.

This distinction matters because a gateway can keep the data plane inside a private network while using a managed control plane. It also clarifies failure behavior:

- control-plane outage should not necessarily stop already configured traffic
- data-plane outage directly affects inference availability
- configuration propagation must be versioned and observable
- secrets should be available to the data plane without being exposed to every application

Kubernetes-native products such as Envoy AI Gateway emphasize declarative control. Enterprise platforms often offer hosted, hybrid, and fully self-hosted combinations.
