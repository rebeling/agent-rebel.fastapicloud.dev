---
title: "What Is an LLM Proxy?"
type: concept
section: Concepts
section_title: Concepts
section_order: 1
nav_order: 1
summary: "A practical definition of the intermediary between applications and one or more model providers."
status: reviewed
updated: 2026-07-14
tags: ["definition", "llm-proxy", "ai-gateway"]
related: ["wiki/concepts/proxy-gateway-router.md", "wiki/architecture/request-lifecycle.md"]
sources: []
---

An LLM proxy is a service that receives model requests from applications and forwards them to model providers or private model servers.

A minimal proxy changes an endpoint and injects credentials. A production gateway may additionally:

- normalize provider-specific request and response formats
- route across providers, regions, accounts, or models
- retry or fail over after quota, timeout, or service errors
- enforce authentication, model allowlists, budgets, and rate limits
- cache responses
- record tokens, latency, errors, cost, and traces
- redact or block sensitive content
- centralize provider credentials
- expose an OpenAI-compatible API to existing clients

The proxy is useful when applications should not know every provider's authentication, error model, pricing metadata, or deployment topology.

The proxy is harmful when it becomes an unobserved single point of failure, silently changes model behavior, logs sensitive prompts without policy, or promises compatibility it does not actually provide.
