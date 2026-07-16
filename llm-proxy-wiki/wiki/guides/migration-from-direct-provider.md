---
title: "Migration from Direct Provider Calls"
type: guide
section: Guides
section_title: Guides
section_order: 5
nav_order: 2
summary: "A low-risk sequence for introducing a gateway without coupling the application to new hidden behavior."
status: reviewed
updated: 2026-07-14
tags: ["migration", "rollout", "direct-provider"]
related: ["wiki/failures/silent-fallbacks.md"]
sources: []
---

## 1. Inventory current behavior

Record endpoints, models, parameters, tool schemas, timeouts, retries, streaming behavior, and error handling.

## 2. Introduce a client abstraction

Move endpoint and credential configuration behind one application interface before changing providers.

## 3. Run the gateway in pass-through mode

Use one provider and one model. Disable caching, fallback, prompt transformation, and semantic routing.

## 4. Compare responses and telemetry

Run contract tests and shadow traffic where permitted. Compare latency, errors, usage fields, and structured output.

## 5. Move credentials and identity

Replace provider keys in applications with gateway-issued credentials.

## 6. Add controls incrementally

Add rate limits, budgets, routing, caching, and guardrails one at a time.

## 7. Preserve rollback

Keep a tested direct-provider configuration until the gateway is highly available and operationally owned.

## Principle

First centralize. Then observe. Then govern. Only then optimize.
