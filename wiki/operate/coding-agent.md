---
title: Coding Agent
type: example
section: Operate
section_title: Operate
section_order: 3
nav_order: 1
description: A concrete use case for designing, operating, and evaluating a code-editing agent.
tags: [agents, coding, example]
status: starter
---

A coding agent helps modify a codebase. It can inspect files, plan changes, edit code, run tests, and explain the result.

## Goal

Help a developer make small, reviewable code changes safely.

## Useful capabilities

- read repository files
- search code
- inspect tests
- edit files
- run tests or linters
- summarize diffs
- ask before risky changes

## Needed knowledge

A coding agent needs project-specific context:

- architecture overview
- coding rules
- test commands
- dependency rules
- deployment constraints
- known traps
- recent decisions

This is where a small OKF wiki is useful. The agent can retrieve project knowledge before editing code.

## Safe workflow

```text
Understand task
-> inspect relevant files
-> retrieve project rules
-> propose small plan
-> edit
-> run tests
-> summarize diff
-> stop
```

## Boundaries

A coding agent should not:

- rewrite large parts of the system without a plan
- add dependencies casually
- delete files without confirmation
- ignore failing tests
- hide uncertainty
- modify unrelated code

## Evaluation

Check:

- Did the change solve the requested problem?
- Was the diff small and focused?
- Were tests added or updated when needed?
- Did the agent run the right checks?
- Did it explain what changed?
- Did it avoid unrelated cleanup?

## Common failure

The agent starts with an edit before understanding the existing design. Prevent this by requiring “inspect first, edit second.”

## Related pages

- [[design/agent-types]]
- [[design/design-strategies]]
- [[operate/evaluation]]
