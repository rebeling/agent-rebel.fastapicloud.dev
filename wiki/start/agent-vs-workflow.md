---
title: Agent vs Workflow
type: concept
section: Start
section_title: Start
section_order: 1
nav_order: 2
description: A workflow follows predefined steps; an agent chooses the next step dynamically.
tags: [agents, workflows, architecture]
status: starter
---

# Agent vs Workflow

A workflow follows predefined steps. An agent chooses the next step dynamically.

This is the most important distinction in the wiki.

## Workflow

A workflow is a known sequence:

```text
Input -> Step A -> Step B -> Step C -> Output
```

Use a workflow when the path is stable. Workflows are easier to test because you know what should happen at each step. They are also easier to monitor because every branch is explicit.

Examples:

- validate a form
- generate an invoice
- run an ETL pipeline
- classify a support ticket using fixed categories
- extract fields from a known document type

## Agent

An agent is a dynamic controller:

```text
Goal -> choose next action -> observe -> choose again -> stop
```

Use an agent when the path cannot be fully known upfront. The agent may need to search, inspect, call tools, ask a question, revise the plan, or stop early.

Examples:

- investigate a production incident
- research a topic across changing sources
- modify a codebase after inspecting existing files
- help a user with a vague operational request
- coordinate multiple specialist tools or agents

## Rule of thumb

Prefer the workflow until flexibility is required.

Agents are powerful, but they add uncertainty. More autonomy means more surface area for wrong tool calls, loops, hidden assumptions, and expensive traces.

## Related pages

- [[start/decision-checklist]]
- [[design/design-strategies]]
- [[operate/evaluation]]

## References

- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
- Google Cloud AI agents overview: https://cloud.google.com/discover/what-are-ai-agents
