---
title: Agent Decision Checklist
type: guide
section: Start
section_title: Start
section_order: 1
nav_order: 3
description: A short checklist for deciding whether a task should be solved with an agent.
tags: [agents, decision, checklist]
status: starter
---

Use this before building an agent. Most systems do not need full agency. Many need a boring workflow, a search UI, or a normal API call.

## Start with the boring option

Choose a workflow when:

- the steps are known in advance
- the input and output formats are stable
- the task must be highly repeatable
- failures should be easy to reproduce
- a normal rules engine or queue can solve the problem

A workflow is easier to test, cheaper to run, and easier to explain.

## Consider an agent when

Use an agent when:

- the system must decide the next step dynamically
- the task requires discovery or investigation
- the task may need different tools depending on intermediate results
- user intent is vague and needs clarification
- the system has to recover from incomplete or unexpected information
- the result depends on fresh or project-specific knowledge

The key question is not “can an LLM do this?” The key question is: **does the control flow need to be dynamic?**

## Require human confirmation when

Put a human in the loop when the agent might:

- send messages or emails
- change data
- delete files
- spend money
- expose private information
- affect legal, medical, financial, or employment outcomes

## Minimum design before implementation

Before writing code, define:

1. the goal
2. the allowed tools
3. the stop condition
4. what the agent may never do
5. what evidence it should use
6. how success will be evaluated

## Related pages

- [[start/agent-vs-workflow]]
- [[design/design-strategies]]
- [[operate/failure-modes]]
