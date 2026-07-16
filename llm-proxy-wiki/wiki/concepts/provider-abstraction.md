---
title: "Provider Abstraction"
type: concept
section: Concepts
section_title: Concepts
section_order: 1
nav_order: 4
summary: "The benefits and limits of hiding model-provider differences behind one API."
status: reviewed
updated: 2026-07-14
tags: ["abstraction", "virtual-model", "provider"]
related: ["wiki/architecture/routing-strategies.md", "wiki/failures/silent-fallbacks.md"]
sources: []
---

Provider abstraction gives applications a stable contract while providers change underneath it.

## Benefits

- centralized credentials and provider onboarding
- cheaper model and provider switching
- consistent retries, timeouts, logging, and cost metadata
- common access controls and budget enforcement
- easier A/B tests and fallbacks
- simpler client code

## Limits

Models are not interchangeable compute instances. They differ in reasoning behavior, context windows, tool use, safety policies, multimodal formats, structured outputs, latency, and price.

A good abstraction exposes a stable baseline while preserving provider-specific capabilities through explicit options. A bad abstraction pretends all models are identical and silently discards unsupported parameters.

Use **virtual model names** such as `general-fast`, `general-strong`, or `private-eu` when the application should depend on a service class rather than a vendor model identifier.
