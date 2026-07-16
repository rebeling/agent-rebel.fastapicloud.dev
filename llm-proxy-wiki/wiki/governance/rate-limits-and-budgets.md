---
title: "Rate Limits and Budgets"
type: governance
section: Governance
section_title: Governance
section_order: 3
nav_order: 2
summary: "LLM traffic needs request, token, concurrency, and spend controls rather than only classic requests-per-second limits."
status: reviewed
updated: 2026-07-14
tags: ["rate-limit", "budget", "finops"]
related: ["wiki/failures/cost-accounting-drift.md", "wiki/architecture/observability.md"]
sources: []
---

## Useful limit dimensions

- requests per minute
- input or output tokens per minute
- concurrent requests
- daily or monthly spend
- model-specific spend
- user, team, project, or tenant
- provider account or deployment quota
- maximum prompt or output size

## Hard and soft controls

A hard limit rejects requests. A soft threshold emits alerts or changes routing. Both are useful:

- warn at 70% of budget
- route to a cheaper model at 85%
- reject nonessential traffic at 100%
- reserve capacity for priority workloads

## Accuracy caveat

Gateway cost is often an estimate based on token counts and a model price map. Provider invoices remain the financial source of truth. Track discrepancies and support negotiated pricing overrides.

## Denial of wallet

Authentication alone does not prevent accidental or malicious cost explosions. Enforce maximum tokens, concurrency, retries, recursive agent actions, and total spend.
