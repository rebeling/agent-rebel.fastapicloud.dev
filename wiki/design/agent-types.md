---
title: Agent Types
type: concept
section: Design
section_title: Design
section_order: 2
nav_order: 1
description: A compact map of common agent types by interaction style, task, and system shape.
tags: [agents, types]
status: starter
---

There is no single perfect taxonomy for agents. Use types as design hints, not as strict boxes.

## By interaction style

### Interactive agents

Interactive agents work directly with a user. They answer, ask clarifying questions, propose actions, and may act with confirmation.

Examples:

- support assistant
- coding assistant
- personal productivity assistant
- data analysis assistant

Main risk: the user may trust fluent answers even when the agent is missing evidence.

### Background agents

Background agents run from events, queues, schedules, or monitoring signals. They may not have a user watching every step.

Examples:

- incident monitor
- inbox triage agent
- data-quality watcher
- automated report agent

Main risk: silent wrong action. Background agents need stronger limits, logging, and escalation rules.

## By task domain

### Coding agent

Inspects a codebase, edits files, runs tests, and explains changes. Needs repository context, safe file access, version control, and strong rollback habits.

### Research agent

Searches, reads, compares, and summarizes sources. Needs source grounding, citation discipline, recency checks, and uncertainty handling.

### Support agent

Uses product docs, tickets, customer context, and operational tools. Needs escalation paths and strict privacy boundaries.

### Data agent

Queries data, builds analysis, explains results. Needs schema knowledge, query safety, and validation against source data.

## By system shape

### Single agent

One agent controls the loop and tools. Simpler to debug. Prefer this first.

### Multi-agent system

Multiple agents cooperate or delegate tasks. Useful for specialization, but harder to evaluate. Add multi-agent coordination only when one agent becomes too broad.

## Related pages

- [[operate/coding-agent]]
- [[design/protocols-and-tool-access]]
- [[operate/evaluation]]

## References

- Google Cloud AI agent categories: https://cloud.google.com/discover/what-are-ai-agents
- IBM AI agents overview: https://www.ibm.com/think/topics/ai-agents
