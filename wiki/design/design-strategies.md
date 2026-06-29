---
title: Design Strategies
type: strategy
section: Design
section_title: Design
section_order: 2
nav_order: 6
description: Practical strategies for building small, safer, more testable agents.
tags: [agents, strategy, design]
status: starter
---

# Design Strategies

Start with control. Add autonomy only where it clearly improves the task.

## 1. Narrow the scope

A small agent is easier to test and trust. Give it a limited goal, limited tools, and clear boundaries.

Bad:

> Help with all operations.

Better:

> Triage incoming support tickets and suggest one of five known next actions.

## 2. Retrieve before planning

When the task depends on project-specific information, retrieve the relevant context before the agent starts planning. Planning without evidence produces confident guesses.

## 3. Make stop conditions explicit

Every agent should know when to stop. Define max iterations, max cost, max time, and success criteria.

Examples:

- stop after 5 tool calls
- stop when tests pass
- stop when confidence is low and ask the user
- stop before destructive actions

## 4. Separate read and write tools

Read tools should be easy to use. Write tools should require stronger validation or confirmation.

Example:

- read repository files freely
- ask before deleting files
- ask before sending external messages

## 5. Prefer checkpoints over long context

For long tasks, write checkpoints: summary, decisions, current state, next step. Then continue with a fresh context instead of dragging the entire trace forward.

## 6. Design escalation

The safest agent is not the one that always finishes. It is the one that knows when to ask for help.

Escalate when:

- evidence conflicts
- tool output is ambiguous
- risk is high
- required permissions are missing
- success criteria are unclear

## Related pages

- [[start/decision-checklist]]
- [[operate/evaluation]]
- [[operate/failure-modes]]
