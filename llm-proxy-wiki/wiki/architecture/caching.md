---
title: "LLM Gateway Caching"
type: architecture
section: Architecture
section_title: Architecture
section_order: 2
nav_order: 4
summary: "Caching can reduce latency and cost, but only when identity, privacy, and semantics are explicit."
status: reviewed
updated: 2026-07-14
tags: ["cache", "semantic-cache", "cost"]
related: ["wiki/governance/privacy-and-retention.md"]
sources: []
---

## Exact-response caching

The key is derived from model, parameters, and request content. It is predictable but only helps repeated identical calls.

## Semantic caching

A vector or similarity system reuses a previous answer for a similar prompt. It can save more cost but risks returning contextually wrong or stale answers.

## Provider prompt caching

Some providers discount repeated prompt prefixes. The gateway may expose or account for this without storing full responses itself.

## Cache-key requirements

Include every field that changes behavior:

- virtual and resolved model
- system and user content
- tools and tool schemas
- temperature and sampling parameters
- response format
- tenant and authorization scope
- retrieval context or knowledge version
- policy version when policy can transform content

## Safety rules

- never share cache entries across tenants unless explicitly safe
- do not cache sensitive prompts by default
- define TTL and invalidation
- mark cache hits in telemetry
- distinguish cached cost from avoided provider cost
- disable caching for non-deterministic, personalized, or high-risk tasks
