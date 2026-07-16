---
title: Agent Memory
type: memory
section: Design
section_title: Design
section_order: 2
nav_order: 3
description: Agent memory is persisted information that can be inspected, corrected, scoped, expired, and reused.
tags: [agents, memory, context, retrieval, llm-wiki]
status: starter
---

Agent memory is information an agent can store and recall later.

It is not the same as the context window. Context is what the model can see right now. Memory is what the surrounding system can keep, search, update, delete, and reuse across sessions.

A useful memory system is not just storage. It needs a way to decide what should be remembered, when it should be retrieved, when it is no longer valid, and how a human can correct it.

## Why it matters

Without memory, every agent starts from zero. The user has to repeat the same project details, preferences, constraints, decisions, and previous outcomes.

With bad memory, the agent becomes worse. It may retrieve stale facts, over-generalize from one conversation, expose private information, or keep using outdated assumptions.

Good memory gives the agent continuity without turning it into a black box.

## Context vs memory

**Context** is temporary working space.

It includes the system instructions, the current user request, recent conversation, retrieved pages, tool outputs, and intermediate state. It is limited by the model context window and must be selected carefully.

**Memory** is persisted knowledge.

It lives outside the model: in files, databases, vector stores, knowledge graphs, logs, or wiki pages. It can be recalled later, even after the current conversation ends.

The agent should not confuse the two:

```text
context = what the model can use now
memory  = what the system can store and recall later
```

A larger context window does not remove the need for memory. It only gives more temporary space. The system still needs to decide what matters.

## Memory types

### Short-term memory

Short-term memory is task-local state. It helps the agent keep track of the current task, active plan, recent decisions, and open questions.

This may live in the context window, a session store, or a short-lived cache.

### Long-term memory

Long-term memory persists across sessions. It stores facts, decisions, preferences, examples, and previous outcomes that may be useful later.

This can be implemented with Markdown files, a database, a vector index, a knowledge graph, or a combination of these.

### Episodic memory

Episodic memory stores events.

Examples:

- “The agent tried this migration on Friday and it failed because the schema was stale.”
- “The user rejected this answer because it was too generic.”
- “This support case was solved by checking the deployment logs.”

Episodic memory helps with learning from concrete experiences.

### Semantic memory

Semantic memory stores facts, concepts, rules, and definitions.

Examples:

- “MCP connects models to tools and resources.”
- “A2A is for agent-to-agent communication.”
- “A workflow is better than an agent when the steps are predictable.”

Semantic memory is what this wiki mostly contains.

### Procedural memory

Procedural memory stores reusable ways of doing things.

Examples:

- how to inspect a codebase before editing
- how to debug a tool failure
- how to evaluate a retrieval answer
- how to write a decision record

Procedural memory is close to a playbook or checklist.

## What should be remembered

Memory should be selective.

Good candidates:

- stable facts
- explicit user preferences
- project decisions
- reusable procedures
- recurring failure modes
- validated examples
- references and sources

Bad candidates:

- unverified guesses
- one-off intermediate thoughts
- private data without a clear purpose
- temporary task state that expires quickly
- tool outputs that are too large or noisy
- facts without source or timestamp

A simple rule:

> Store less, but make stored knowledge inspectable and useful.

## Memory metadata

Every important memory should carry metadata.

At minimum:

- **source**: where did this come from?
- **timestamp**: when was it created or observed?
- **scope**: who or what does it apply to?
- **confidence**: is this confirmed, inferred, or uncertain?
- **expiry**: when should it be reviewed or forgotten?
- **correction path**: how can a human fix it?

Without metadata, memory becomes context pollution.

## How The Agent Wiki fits

The Agent Wiki is not the agent's private memory. It is the shared knowledge layer between raw sources, human understanding, and future agent answers.

A task can still have short-lived runtime memory: current plan, tool results, temporary notes, and open questions. That kind of state may disappear when the task ends.

But durable knowledge is different. If something should affect future answers, future design choices, or future tool use, it should not live only in hidden memory. It should be promoted into a visible page, source note, or decision record.

```text
agent finds useful knowledge
-> proposes a page update
-> human reviews or edits it
-> wiki improves
-> future agents retrieve the improved page
```

This is where agent memory connects to the LLM Wiki / OKF idea: raw sources stay separate, the wiki becomes the maintained synthesis layer, and the agent helps keep that layer current.

The advantage is shared control:

- humans can inspect and correct what the agent relies on
- agents can retrieve curated pages instead of random chat history
- useful answers become reusable knowledge
- stale or weak claims can be edited instead of repeated
- the knowledge base improves through use

The practical rule:

> Hidden memory is acceptable for temporary task state. Durable knowledge should become visible, reviewable wiki knowledge.

## Failure modes

### Stale memory

The agent recalls something that used to be true but is no longer true.

Prevention: add timestamps, review dates, and freshness warnings.

### Over-generalization

The agent turns one event into a general rule.

Prevention: separate episodic memory from semantic memory.

### Memory bloat

The memory store grows without pruning. Retrieval becomes noisy and slow.

Prevention: add expiry, relevance scoring, and deletion.

### Hidden memory

The agent acts on information the human cannot see or correct.

Prevention: move important knowledge into visible pages or decision records.

### Privacy leakage

The agent stores or retrieves sensitive information too broadly.

Prevention: scope memory, redact private data, and avoid storing unnecessary details.

## Practical rule

Agent memory is useful only when it can be inspected, corrected, scoped, expired, and reused.

Hidden memory helps the agent once. Visible memory helps humans and agents together.

## Related pages

- [[reference/llm-wiki-and-okf]]
- [[design/retrieval-and-grounding]]
- [[operate/failure-modes]]
- [[design/design-strategies]]
- [[design/core-capabilities]]

## References

- Weaviate, “Context Engineering”: https://weaviate.io/blog/context-engineering
- Google Cloud, “What are AI agents?”: https://cloud.google.com/discover/what-are-ai-agents
- Andrej Karpathy, “LLM Wiki”: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Databricks, “What is AI Agent Evaluation?”: https://www.databricks.com/blog/what-is-agent-evaluation
