---
title: "Authentication and Virtual Keys"
type: governance
section: Governance
section_title: Governance
section_order: 3
nav_order: 1
summary: "Applications should authenticate to the gateway without receiving raw provider credentials."
status: reviewed
updated: 2026-07-14
tags: ["authentication", "virtual-keys", "oidc"]
related: ["wiki/governance/rate-limits-and-budgets.md", "wiki/architecture/security-boundary.md"]
sources: []
---

A virtual key is a gateway-issued credential mapped to users, teams, projects, models, budgets, and policies.

## Benefits

- provider keys stay out of application configuration
- access can be revoked without rotating every provider account
- usage can be attributed to a team or service
- model allowlists and limits follow identity
- credentials can have expiration and scope

## Identity patterns

- gateway API keys for services
- OIDC or JWT for users and workloads
- cloud workload identity
- mTLS for internal service identity
- delegated identity where downstream audit requires the original user

## Key design rules

- separate administrative and inference credentials
- avoid one global key shared by all applications
- rotate provider and virtual keys independently
- store secrets in a secret manager
- make key creation, update, and deletion auditable
- define behavior when identity or policy services are unavailable
