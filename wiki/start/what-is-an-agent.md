---
title: What Is an Agent?
type: concept
section: Start
section_title: Start
section_order: 1
nav_order: 1
description: An agent is a goal-directed system that can choose actions, use tools, observe results, and adapt its next step.
tags: [agents, basics]
status: starter
---

# What Is an Agent?

An agent is a goal-directed software system that can choose actions, use tools, observe results, and adapt its next step.

A simple LLM call answers one prompt. An agent runs a loop: understand the goal, decide what to do, act, observe the result, update the state, and continue until it reaches a stop condition.

## Minimal agent loop

```text
Goal -> Reason -> Act -> Observe -> Update -> Stop or continue
```

The loop is what matters. If the system does not choose between possible next actions, it is probably not an agent. It may be a chatbot, assistant, workflow, or tool-using function call.

## Typical components

An agent usually has:

- **instructions**: what role it should follow
- **state**: what it knows right now
- **tools**: what actions it may take
- **memory**: what can persist or be retrieved later
- **policy**: when to act, ask, stop, or escalate
- **evaluation**: how we know it behaved well

## Why this distinction matters

Calling everything an agent creates bad architecture. If the task is predictable, make it a workflow. If the human should stay in control, make it an assistant. If the task is rule-based, make it a bot or service.

Agents are useful when the correct next step depends on what the system discovers during execution.

## Related pages

- [[start/agent-vs-workflow]]
- [[design/core-capabilities]]
- [[start/decision-checklist]]

## References

- Google Cloud, “What is an AI agent?”: https://cloud.google.com/discover/what-are-ai-agents
- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
