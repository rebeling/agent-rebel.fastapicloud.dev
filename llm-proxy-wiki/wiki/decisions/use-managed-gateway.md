---
title: "Decision: Use a Managed LLM Gateway"
type: decision
section: Decisions
section_title: Decisions
section_order: 8
nav_order: 2
summary: "Use a managed gateway when operational simplicity and fast provider access matter more than owning the data plane."
status: reviewed
updated: 2026-07-14
tags: ["decision", "managed", "saas"]
related: ["wiki/providers/openrouter.md", "wiki/providers/cloudflare-ai-gateway.md", "wiki/providers/vercel-ai-gateway.md"]
sources: []
---

## Good conditions

- small platform team
- public model APIs dominate
- managed data processing is acceptable
- rapid model experimentation matters
- existing application platform offers a native gateway

## Candidate patterns

- OpenRouter for broad aggregation
- Cloudflare AI Gateway for Workers and edge workloads
- Vercel AI Gateway for Vercel and AI SDK applications
- Portkey or Helicone for managed AI-native gateway and observability

## Required controls

- document subprocessors and retention
- test zero-data-retention routing
- export telemetry to organization-owned systems
- retain a direct-provider emergency path
- understand fees and billing reconciliation
- test service and control-plane outages
