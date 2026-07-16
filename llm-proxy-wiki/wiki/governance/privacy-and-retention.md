---
title: "Privacy, Retention, and Data Residency"
type: governance
section: Governance
section_title: Governance
section_order: 3
nav_order: 3
summary: "The gateway adds another processor and possible storage layer to every model request."
status: reviewed
updated: 2026-07-14
tags: ["privacy", "retention", "data-residency", "zdr"]
related: ["wiki/architecture/caching.md"]
sources: []
---

Evaluate four separate paths:

1. application to gateway
2. gateway processing and storage
3. gateway to model provider
4. telemetry export to external systems

## Questions to answer

- Are prompts or outputs stored?
- Is logging opt-in or opt-out?
- What is the retention period?
- Can payloads be omitted while metadata remains?
- Where are gateway logs, caches, and backups stored?
- Can traffic be restricted to an approved region?
- Does the selected upstream provider retain or train on data?
- Can zero-data-retention requirements be enforced by route?
- Can customer-controlled storage receive logs?
- Can deletion requests be fulfilled across every copy?

A managed gateway's privacy controls do not override the upstream provider's policy. Route policy should include provider and deployment attributes, not only model name.
