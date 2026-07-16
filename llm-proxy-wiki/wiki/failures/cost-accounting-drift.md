---
title: "Cost Accounting Drift"
type: failure
section: Failure Modes
section_title: Failure Modes
section_order: 6
nav_order: 3
summary: "Gateway estimates can diverge from provider invoices because prices, token categories, and usage fields change."
status: reviewed
updated: 2026-07-14
tags: ["failure", "cost", "finops"]
related: ["wiki/governance/rate-limits-and-budgets.md", "wiki/architecture/observability.md"]
sources: []
---

## Causes

- stale model price maps
- provider aliases or version changes
- cached-token and reasoning-token differences
- streaming responses without complete usage fields
- retries and fallbacks counted incorrectly
- negotiated prices not represented
- provider-side minimums or batch discounts

## Prevention

- preserve raw provider usage metadata
- version price maps
- support custom prices
- reconcile gateway totals with invoices
- alert on material variance
- distinguish estimated, reported, and avoided cost
- include retry and fallback cost in request traces

The gateway is an operational cost-control system. The provider invoice remains the accounting source of truth.
