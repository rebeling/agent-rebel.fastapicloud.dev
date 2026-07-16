---
title: "LLM Gateway Evaluation Checklist"
type: guide
section: Guides
section_title: Guides
section_order: 5
nav_order: 1
summary: "A procurement and engineering checklist for comparing gateway candidates."
status: reviewed
updated: 2026-07-14
tags: ["evaluation", "checklist", "procurement"]
related: ["wiki/comparisons/decision-guide.md"]
sources: []
---

## API compatibility

- chat completions and responses endpoints
- streaming event shape and usage fields
- tools and parallel tool calls
- structured outputs and JSON schema
- embeddings, image, audio, and batch endpoints if required
- native provider passthrough
- error-code and retry semantics

## Providers and routing

- required providers, regions, accounts, and private servers
- weighted routing
- health checks and circuit breaking
- retry and fallback rules
- capability and residency constraints
- route-decision metadata
- model alias or virtual model support

## Governance

- service and user authentication
- virtual keys and expiration
- model allowlists
- request, token, concurrency, and spend limits
- organization, team, project, and tenant hierarchy
- audit logs and policy versioning

## Privacy and security

- prompt and output storage defaults
- retention and deletion
- zero-data-retention controls
- region selection
- customer-managed keys or storage
- cache isolation
- signed artifacts and advisories
- admin-interface separation

## Operations

- high availability
- database and cache dependencies
- horizontal scaling
- configuration rollout and rollback
- metrics and OpenTelemetry
- degraded behavior when telemetry fails
- upgrade path and support

## Commercial

- open-source versus enterprise boundaries
- managed fees or model markup
- seats, requests, tokens, logs, and retention pricing
- support SLA
- security-response commitments
