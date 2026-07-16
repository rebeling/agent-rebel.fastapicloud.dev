---
title: "Silent Fallbacks"
type: failure
section: Failure Modes
section_title: Failure Modes
section_order: 6
nav_order: 2
summary: "A gateway can improve uptime while quietly changing model quality, safety, latency, or cost."
status: reviewed
updated: 2026-07-14
tags: ["failure", "fallback", "routing"]
related: ["wiki/architecture/routing-strategies.md", "wiki/concepts/provider-abstraction.md"]
sources: []
---

## Failure

A request to one model fails and the gateway returns a response from another model without making the substitution visible.

## Why it matters

- evaluation results no longer match production
- safety and residency guarantees may change
- tool or structured-output behavior may differ
- cost can increase
- users cannot explain inconsistent responses

## Prevention

- restrict fallback to capability-equivalent routes
- expose resolved model and provider in authorized metadata
- count and alert on fallback
- log trigger error and route policy version
- require explicit opt-in for cross-family fallback
- disable retry after partial streaming output unless the client can handle duplication
