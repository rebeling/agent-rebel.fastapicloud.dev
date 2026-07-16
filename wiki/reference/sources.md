---
title: Sources
type: catalog
section: Reference
section_title: Reference
section_order: 4
nav_order: 2
description: Source catalog for the compact starter wiki.
tags: [sources, meta]
status: starter
---

This starter uses a small set of current, useful sources. Keep this page short and curated.

## Core definitions

### Google Cloud — What are AI agents?

URL: https://cloud.google.com/discover/what-are-ai-agents

Useful for: agent definition, key features, difference between agents, assistants, and bots, and high-level use-case categories.

Related pages:

- [[start/what-is-an-agent]]
- [[design/agent-types]]
- [[design/core-capabilities]]

### IBM — What are AI agents?

URL: https://www.ibm.com/think/topics/ai-agents

Useful for: agent lifecycle, planning, reasoning with tools, learning, and memory.

Related pages:

- [[start/what-is-an-agent]]
- [[design/agent-memory]]

## Protocols

### Model Context Protocol documentation

URL: https://modelcontextprotocol.io/docs/getting-started/intro

Useful for: MCP as a standard way to connect AI applications to external systems, including tools, data sources, and prompts.

Related pages:

- [[design/protocols-and-tool-access]]
- [[design/retrieval-and-grounding]]

### Google Developers Blog — A2A announcement

URL: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

Useful for: A2A as a protocol for agent interoperability and coordination.

Related pages:

- [[design/protocols-and-tool-access]]
- [[design/agent-types]]

### IBM — A2A protocol overview

URL: https://www.ibm.com/think/topics/agent2agent-protocol

Useful for: agent cards, tasks, messages, artifacts, and agent-to-agent communication concepts.

Related pages:

- [[design/protocols-and-tool-access]]

## Building agents

### OpenAI Agents SDK docs

URL: https://developers.openai.com/api/docs/guides/agents

Useful for: agents, tools, handoffs, guardrails, sessions, tracing, and multi-step work.

Related pages:

- [[start/agent-vs-workflow]]
- [[operate/evaluation]]

## Context, memory, and knowledge

### Weaviate — Context Engineering

URL: https://weaviate.io/blog/context-engineering

Useful for: context windows, retrieval, memory, tools, and why reliable agents need context architecture.

Related pages:

- [[design/agent-memory]]
- [[design/retrieval-and-grounding]]
- [[operate/failure-modes]]


### Andrej Karpathy — LLM Wiki

URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Useful for: the core pattern of raw sources, an LLM-maintained Markdown wiki, and a schema/instructions file. The most important idea is that knowledge should compound through ingest, query, and lint loops instead of being rediscovered from raw chunks on every question.

Related pages:

- [[reference/llm-wiki-and-okf]]
- [[design/agent-memory]]
- [[design/retrieval-and-grounding]]

### Google Cloud — Introducing the Open Knowledge Format

URL: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing

Useful for: OKF as Markdown files with YAML frontmatter, readable by humans and agents.

Related pages:

- [[reference/llm-wiki-and-okf]]
- [[design/retrieval-and-grounding]]

## Evaluation and failure modes

### Databricks — What is AI Agent Evaluation?

URL: https://www.databricks.com/blog/what-is-agent-evaluation

Useful for: component-level and end-to-end evaluation, tool-use evaluation, trajectories, accuracy, safety, cost, and latency.

Related pages:

- [[operate/evaluation]]

### Galileo — How to Debug AI Agents

URL: https://galileo.ai/blog/debug-ai-agents

Useful for: practical failure modes such as hallucination cascades, tool misfires, context truncation, loops, leakage, output drift, and memory bloat.

Related pages:

- [[operate/failure-modes]]
- [[operate/evaluation]]
