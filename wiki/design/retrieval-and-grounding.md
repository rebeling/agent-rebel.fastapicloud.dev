---
title: Retrieval and Grounding
type: concept
section: Design
section_title: Design
section_order: 2
nav_order: 4
description: Retrieval gives the agent relevant evidence; grounding ties answers and actions back to that evidence.
tags: [agents, retrieval, rag, grounding]
status: starter
---

# Retrieval and Grounding

Retrieval is how an agent gets relevant knowledge before it reasons, answers, or acts.

Grounding is how the system keeps the output tied to visible evidence.

## Why retrieval matters

Models know general patterns, but many agent tasks depend on information that is private, recent, project-specific, or changing. Examples:

- current codebase state
- internal policies
- product documentation
- open incidents
- customer tickets
- previous decisions
- calendar or email context

Without retrieval, the agent fills gaps from memory or training data. That is where hallucination starts.

## Retrieval-first strategy

Use retrieval before planning when the task depends on specific knowledge.

```text
User goal -> retrieve relevant knowledge -> plan -> act -> cite or explain evidence
```

This does not mean retrieving everything. Too much context can be as harmful as too little context.

## What to retrieve

Good retrieval returns:

- the smallest useful context
- source path or URL
- timestamp or version
- confidence signal
- related decisions
- warnings about stale information

## OKF as a knowledge layer

OKF is useful here because each page is plain Markdown with YAML frontmatter. It can be read by people, indexed by search, loaded into an LLM context, and versioned in git.

## Bad grounding smell

If the agent says “according to the documentation” but cannot point to the page, chunk, or source, the grounding is weak.

## Related pages

- [[design/agent-memory]]
- [[design/design-strategies]]
- [[reference/sources]]

## References

- Weaviate, “Context Engineering”: https://weaviate.io/blog/context-engineering
- Google Cloud OKF blog: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
