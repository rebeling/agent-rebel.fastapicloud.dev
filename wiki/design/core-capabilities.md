---
title: Core Capabilities
type: capability
section: Design
section_title: Design
section_order: 2
nav_order: 2
description: The minimal capability model for practical agents: reason, plan, observe, use tools, retrieve, remember, and stop.
tags: [agents, capabilities]
status: starter
---

An agent is not defined by one feature. It is a combination of capabilities arranged in a loop.

## 1. Reasoning

Reasoning is the ability to interpret the goal, compare options, and decide what to do next. Reasoning without evidence becomes guessing, so strong agents combine reasoning with retrieval and observation.

## 2. Planning

Planning turns a goal into steps. Planning is useful for complex tasks, but overplanning can become expensive and brittle. Small agents often work better with short plans and frequent observations.

## 3. Observation

Observation means reading the result of an action: a tool output, file diff, API response, search result, user reply, or error message. Without observation, an agent cannot adapt.

## 4. Tool use

Tools let the agent act: search, query data, edit files, send messages, create tickets, or call APIs. Tool use is the moment the agent stops being only a text generator.

## 5. Retrieval

Retrieval brings in relevant knowledge before the agent answers or acts. It is essential when the task depends on project docs, recent information, private data, or previous decisions.

## 6. Memory

Memory lets the system preserve useful information beyond the current step or session. Memory should have rules for writing, reading, correction, expiry, and deletion.

## 7. Stop control

Stopping is a capability. An agent needs a clear definition of done, retry limits, cost limits, and escalation rules.

## Design note

Start with the smallest set of capabilities that solves the task. A narrow agent with good stop rules beats a broad agent with vague autonomy.

## Related pages

- [[design/agent-memory]]
- [[design/retrieval-and-grounding]]
- [[operate/failure-modes]]

## References

- Google Cloud AI agent features: https://cloud.google.com/discover/what-are-ai-agents
- OpenAI Agents SDK concepts: https://openai.github.io/openai-agents-python/agents/
