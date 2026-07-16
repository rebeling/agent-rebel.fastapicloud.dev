---
title: Evaluation
type: evaluation
section: Operate
section_title: Operate
section_order: 3
nav_order: 2
description: Agent evaluation checks task success, trajectory, tool use, grounding, safety, cost, and latency.
tags: [agents, evaluation, observability]
status: starter
---

Agent evaluation must inspect both the final answer and the path used to produce it.

A normal LLM evaluation might ask: “Was the final answer correct?”

An agent evaluation also asks:

- Did the agent choose the right tools?
- Were the tool arguments correct?
- Were the steps necessary?
- Did it retrieve useful context?
- Did it stop at the right time?
- Did it avoid unsafe actions?
- Was the cost and latency acceptable?

## Minimal evaluation set

### Task success

Did the agent complete the user’s goal? Did the output meet the expected format and quality?

### Groundedness

Is the answer supported by retrieved sources, files, tool outputs, or explicit evidence?

### Tool-use quality

Did the agent pick the right tool, pass valid arguments, and interpret the result correctly?

### Trajectory quality

Was the sequence of steps efficient and logical, or did it loop, repeat, or wander?

### Safety

Did the agent avoid forbidden actions, privacy leaks, and risky side effects?

### Operational cost

How many model calls, tool calls, tokens, seconds, and retries were needed?

## Starter test set

Create 10–20 representative tasks:

- easy happy paths
- ambiguous user requests
- missing-context cases
- wrong-tool traps
- stale-knowledge traps
- high-risk action cases
- expected escalation cases

Run these repeatedly before changing models, prompts, tools, or memory logic.

## Related pages

- [[operate/failure-modes]]
- [[design/design-strategies]]
- [[operate/coding-agent]]

## References

- Databricks, “What is AI Agent Evaluation?”: https://www.databricks.com/blog/what-is-agent-evaluation
- OpenAI Agents SDK tracing concepts: https://openai.github.io/openai-agents-python/agents/
