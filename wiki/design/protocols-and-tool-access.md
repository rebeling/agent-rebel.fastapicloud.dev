---
title: Protocols and Tool Access
type: protocol
section: Design
section_title: Design
section_order: 2
nav_order: 5
description: A compact overview of MCP, A2A, tool calling, and handoffs.
tags: [agents, protocols, tools]
status: starter
---

# Protocols and Tool Access

Protocols define how agent systems connect to tools, data, and other agents.

The important distinction:

- **Tool calling** lets a model request a function call.
- **MCP** standardizes access to external systems such as tools, resources, and prompts.
- **A2A** supports agent-to-agent communication and delegation.
- **Handoffs** pass control from one agent or specialist to another inside an application.

## Tool calling

Tool calling is the basic pattern: the model chooses a function, fills arguments, receives the result, and continues. It is simple and useful, but each application still defines its own tool interface.

Use it for small apps with a few stable functions.

## MCP

Model Context Protocol standardizes how AI applications connect to external systems. An MCP server can expose tools, resources, and prompts to a client. This reduces one-off integrations.

Use MCP when tools or resources should be reusable across clients or models.

## A2A

Agent-to-Agent is for communication between agents. An agent can discover another agent’s capabilities and delegate work.

Use A2A when independent agents need to coordinate across systems, teams, or platforms.

## Handoffs

A handoff transfers the task to a more specialized agent. This can be internal to one app and does not require an external protocol.

Use handoffs when specialization improves quality or safety.

## Warning

Protocols move information. They do not guarantee that the information is correct, current, safe, or useful. Context quality still has to be designed.

## Related pages

- [[design/core-capabilities]]
- [[design/retrieval-and-grounding]]
- [[operate/failure-modes]]

## References

- MCP docs: https://modelcontextprotocol.io/docs/getting-started/intro
- Google A2A announcement: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- IBM A2A overview: https://www.ibm.com/think/topics/agent2agent-protocol
