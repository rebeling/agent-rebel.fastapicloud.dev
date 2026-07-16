---
title: Failure Modes
type: failure-mode
section: Operate
section_title: Operate
section_order: 3
nav_order: 3
description: The main ways agents fail in practice: missing context, wrong tools, loops, stale memory, leakage, and drift.
tags: [agents, failure-modes, safety]
status: starter
---

Agents fail differently from normal software. The code may work, the API may respond, and the final answer may still be wrong because the agent chose the wrong path.

## 1. Missing context

The agent acts without the knowledge it needs. It guesses, invents facts, or ignores a relevant decision.

Prevention: retrieve before planning; require source links for knowledge-dependent answers.

## 2. Wrong tool

The agent calls the wrong tool or passes the wrong arguments.

Prevention: use strict schemas, tool descriptions, validation, dry-runs, and tool-call tests.

## 3. Infinite loop

The agent repeats the same step or keeps searching because “done” is unclear.

Prevention: max iterations, explicit stop rules, and success criteria.

## 4. Stale memory

The agent recalls outdated facts or old preferences and treats them as current.

Prevention: timestamps, expiry, source tracking, and correction flows.

## 5. Context drift

Long traces bury the original goal or constraints. The agent starts solving a different problem.

Prevention: short checkpoints, re-injected goals, and compact state summaries.

## 6. Tool overuse

The agent keeps using tools when it already has enough information.

Prevention: cost budgets, “answer now” rules, and trajectory evaluation.

## 7. Data leakage

The agent retrieves or reveals information it should not expose.

Prevention: least-privilege retrieval, PII filtering, scoped tools, and human confirmation for sensitive actions.

## 8. Hallucinated capability

The agent claims it can do something it cannot do, or invents a tool that does not exist.

Prevention: explicit tool registry, refusal rules, and tool availability checks.

## Related pages

- [[operate/evaluation]]
- [[design/agent-memory]]
- [[design/design-strategies]]

## References

- Galileo, agent debugging and failure modes: https://galileo.ai/blog/debug-ai-agents
- Weaviate, context engineering failure patterns: https://weaviate.io/blog/context-engineering
