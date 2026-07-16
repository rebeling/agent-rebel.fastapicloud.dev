from typing import Any, TypedDict

from app.lint import lint_all
from app.repository import rebuild_all_links, save_page, create_source


class SeedSource(TypedDict):
    slug: str
    title: str
    source_type: str
    content: str
    metadata: dict[str, Any]


SEED_SOURCES: list[SeedSource] = [
    {
        "slug": "source/google-cloud-agents",
        "title": "Google Cloud: AI agents definition and features",
        "source_type": "article",
        "content": "Google Cloud's official documentation defines AI agents as autonomous entities that leverage Large Language Models to interact with their environment, make decisions, plan workflows, and execute tasks using tools. It highlights reasoning, planning, memory, and tool integration as foundational capabilities for production-ready agents.",
        "metadata": {"url": "https://cloud.google.com/use-cases/ai-agents"},
    },
    {
        "slug": "source/ibm-agents-a2a",
        "title": "IBM: AI agents and A2A protocol",
        "source_type": "article",
        "content": "IBM Think's coverage on AI agents details the emerging Agent-to-Agent (A2A) protocol. It emphasizes how multi-agent collaboration requires standard communication protocols so that agents can register capabilities, discover each other, delegate subtasks, and exchange structured artifacts asynchronously.",
        "metadata": {"url": "https://www.ibm.com/think/topics/ai-agents"},
    },
    {
        "slug": "source/anthropic-mcp",
        "title": "Anthropic: Model Context Protocol (MCP)",
        "source_type": "spec",
        "content": "Anthropic's Model Context Protocol (MCP) defines an open standard for connecting large language models to data sources and tools. MCP establishes client-server boundaries, standardizing how models retrieve context from databases, filesystems, and APIs, avoiding custom integration code.",
        "metadata": {"url": "https://modelcontextprotocol.io/"},
    },
    {
        "slug": "source/openai-agents-sdk",
        "title": "OpenAI Agents SDK concepts",
        "source_type": "documentation",
        "content": "OpenAI's Agents SDK architecture details tool calling, handoffs, and session execution loops. It emphasizes narrow scoping, structured tool definition schemas, and human-in-the-loop triggers for destructive actions to ensure predictable runtime execution.",
        "metadata": {"url": "https://github.com/openai/openai-agents"},
    },
    {
        "slug": "source/databricks-evaluation",
        "title": "Databricks: Agent Evaluation",
        "source_type": "documentation",
        "content": "Databricks' agent evaluation guidelines emphasize assessing the full execution trajectory, not just the final model output. Key metrics include task success, groundedness against retrieved sources, tool parameter accuracy, latency, and cost analysis across iterations.",
        "metadata": {
            "url": "https://www.databricks.com/blog/introducing-agent-evaluation"
        },
    },
    {
        "slug": "source/galileo-failure-modes",
        "title": "Galileo: Agent Failure Modes",
        "source_type": "report",
        "content": "Galileo's research on agent failures outlines classic failure modes including context drift, tool overuse, hallucination cascades, infinite execution loops, and data leakage. It advocates for active logging and automated tests to capture regressions.",
        "metadata": {
            "url": "https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging"
        },
    },
    {
        "slug": "source/weaviate-retrieval-memory",
        "title": "Weaviate: Context Engineering, Retrieval, and Memory",
        "source_type": "documentation",
        "content": "Weaviate's developers guide explores context engineering, RAG, and memory persistence. It draws sharp distinctions between transient context windows (short-term) and external memory indexes (long-term, episodic, semantic, procedural) to optimize search.",
        "metadata": {"url": "https://weaviate.io/developers/weaviate/concepts/rag"},
    },
    {
        "slug": "source/okf-knowledge-catalog",
        "title": "OKF / Google Cloud: Knowledge Catalog",
        "source_type": "spec",
        "content": "The Operational Knowledge Format (OKF) specification details structure for human-readable, machine-parsable documents. Frontmatter metadata combined with semantic wikilinks enables static analyzers and models to traverse knowledge graphs safely.",
        "metadata": {"url": "https://cloud.google.com/knowledge-catalog"},
    },
]

SEED_PAGES = [
    {
        "slug": "index",
        "title": "The Agent Wiki",
        "page_type": "catalog",
        "description": "A practical map of agent concepts, types, capabilities, memory, protocols, evaluation, and failure modes.",
        "tags": ["catalog", "agent-strategy"],
        "body_markdown": """# The Agent Wiki

A practical map for understanding, designing, and evaluating AI agents.

This wiki is for builders. It explains what agents are, when not to use them, how they use tools and memory, which protocols matter, how to evaluate them, and how they fail.

### Start here
- [[basics/what-is-an-agent|What is an agent?]]
- [[basics/agent-vs-workflow|Agent vs workflow]]
- [[basics/agent-vs-assistant-vs-bot|Agent vs assistant vs bot]]
- [[start/agent-decision-checklist|Agent decision checklist]]
- [[start/reading-path|Reading path]]

### Build the model
- [[types/agent-types-overview|Agent types]]
- [[capabilities/capabilities-overview|Core capabilities]]
- [[memory/context-vs-memory|Memory and context]]
- [[protocols/protocols-overview|Tools and protocols]]
- [[knowledge/knowledge-overview|Knowledge and retrieval]]

### Operate safely
- [[strategies/strategies-overview|Strategies and patterns]]
- [[evaluation/evaluation-overview|Evaluation]]
- [[failures/failure-modes-overview|Failure modes]]
- [[examples/examples-overview|Examples]]

### Core idea
Use an agent when the next useful step cannot be fully known in advance.

Use a workflow when the process is predictable.

Use an assistant when the human should stay in control.

Use a bot when the task is simple and rule-based.

### Main warnings
- **Tool access turns a model into an actor.**
- **Memory is only useful if it can be inspected, corrected, expired, and forgotten.**
- **Retrieval should happen before planning when the answer depends on specific or changing knowledge.**
- **Agent evaluation must check the path, not only the final answer.**
- **If success criteria are unclear, agents loop.**
""",
    },
    {
        "slug": "start/reading-path",
        "title": "Reading Path",
        "page_type": "guide",
        "description": "A guided sequence for learning about AI agents.",
        "tags": ["guide", "learning"],
        "body_markdown": """# Reading Path
A guided sequence for learning about AI agents.

Builders should follow a logical path to avoid common pitfalls like over-engineering, unsafe tool access, and uninspectable memory. Jumping straight to coding without understanding these principles leads to fragile, expensive systems that fail non-deterministically.

## Why it matters
Following a structured reading path ensures you learn core safety and architecture concepts before coding. It separates the hype of autonomous agents from the practical, bounded reality of production-grade software engineering.

## Use when
- You are designing an agentic system from scratch.
- Your current prototype is running into non-deterministic loop failures.
- You need to educate team members on agent limitations.

## Avoid when
- You are implementing a simple, single-prompt text completion API.

## Failure modes
- Skipping safety and evaluation chapters to implement broad tool write-access immediately.

## Related pages
- [[basics/what-is-an-agent]]
- [[basics/agent-vs-workflow]]
- [[start/agent-decision-checklist]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "start/agent-decision-checklist",
        "title": "Agent Decision Checklist",
        "page_type": "guide",
        "description": "A checklist to determine whether you need an agent or a simpler system.",
        "tags": ["guide", "architecture"],
        "body_markdown": """# Agent Decision Checklist
A checklist to determine whether you need an agent or a simpler system.

Before implementing a dynamic loop, evaluate predictability, safety bounds, and costs. Most tasks described as needing an agent can be handled more reliably and cheaply using a deterministic workflow. A workflow is easier to test than an agent. Prefer the workflow until flexibility is necessary.

## Why it matters
Choosing the wrong architecture wastes tokens, increases latency, and introduces hard-to-test bugs. This checklist acts as a sanity check before adding runtime complexity.

## Use when
- Evaluating new product requirements.
- Reviewing architectural designs for automation pipelines.

## Avoid when
- The task is inherently creative and requires free-form exploratory dialogue.

## Failure modes
- Answering yes to autonomy when the business rules are fully predictable, leading to unnecessary complexity.

## Related pages
- [[basics/agent-vs-workflow]]
- [[strategies/narrow-agent-scope]]

## References
- Google Cloud: AI agents. [URL](https://cloud.google.com/use-cases/ai-agents)
""",
    },
    {
        "slug": "basics/what-is-an-agent",
        "title": "What Is an Agent",
        "page_type": "concept",
        "description": "A software system that uses AI to dynamically pursue a user-specified goal.",
        "tags": ["concept", "basics"],
        "body_markdown": """# What Is an Agent
A software system that uses AI to dynamically pursue a user-specified goal.

An agent chooses the next step dynamically. It may reason, plan, observe, use tools, collaborate with humans or other agents, revise its approach, and stop when the goal is satisfied. Use an agent when the next useful step depends on what the system discovers during the task.

## Why it matters
Understanding that an agent is a dynamic, goal-driven control loop prevents developers from building rigid pipelines that fail under unexpected data conditions.

## Use when
- The execution path cannot be predicted at compile time.
- The system must discover resources or interact with external environments dynamically.

## Avoid when
- The steps are known, the inputs are structured, and the outputs are narrow.

## Failure modes
- Ambiguous success criteria lead to infinite execution loops.

## Related pages
- [[basics/agent-vs-workflow]]
- [[capabilities/capabilities-overview]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "basics/agent-vs-workflow",
        "title": "Agent vs Workflow",
        "page_type": "concept",
        "description": "The boundary between dynamic control loops and deterministic sequences.",
        "tags": ["concept", "basics"],
        "body_markdown": """# Agent vs Workflow
The boundary between dynamic control loops and deterministic sequences.

A workflow follows known steps; an agent chooses the next step dynamically. A workflow is easier to test than an agent. Prefer the workflow until flexibility is necessary. Most production systems should mix both: deterministic workflow outside, narrow agent loop inside.

## Why it matters
Mixing up these paradigms results in either overly rigid systems that break, or overly chaotic loops that cannot be tested or audited.

## Use when
- Determining control structures for data ingestion or code analysis.

## Avoid when
- No structural or deterministic sequence exists at all.

## Failure modes
- Building a complex agent loop for a standard form-filling task.

## Related pages
- [[basics/what-is-an-agent]]
- [[strategies/narrow-agent-scope]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "basics/agent-vs-assistant-vs-bot",
        "title": "Agent vs Assistant vs Bot",
        "page_type": "concept",
        "description": "Classifying AI systems by autonomy and interaction style.",
        "tags": ["concept", "basics"],
        "body_markdown": """# Agent vs Assistant vs Bot
Classifying AI systems by autonomy and interaction style.

Use a bot when the task is simple and rule-based. Use an assistant when the human should stay in control. Use an agent when the next useful step cannot be fully known in advance. Each requires different security models.

## Why it matters
Mismatched expectations lead to either critical security breaches (giving agents too much trust) or user frustration (treating assistants like bots).

## Use when
- Designing user permissions and tool validation thresholds.

## Avoid when
- Discussing pure model-level capabilities without interface constraints.

## Failure modes
- Deploying an autonomous agent in a high-risk user support setting without human oversight.

## Related pages
- [[basics/what-is-an-agent]]
- [[strategies/human-in-the-loop]]

## References
- Google Cloud: AI agents. [URL](https://cloud.google.com/use-cases/ai-agents)
""",
    },
    {
        "slug": "basics/the-illusion-of-agents",
        "title": "The Illusion of Agents",
        "page_type": "concept",
        "description": "The mismatch between human perception of model cognition and actual next-token generation.",
        "tags": ["concept", "basics"],
        "body_markdown": """# The Illusion of Agents
The mismatch between human perception of model cognition and actual next-token generation.

An agent is not a thinking being. It is a next-token generator wrapped in a loop with tools. Its "thinking" is generated text, not introspection. It does not know what it knows. Fluent reasoning patterns trick humans into over-trusting outputs.

## Why it matters
Over-trusting generated reasoning leads developers to bypass automated validations, inheriting errors when the model asserts incorrect plans confidently.

## Use when
- Designing user-facing explanations, debugging tools, or logs.

## Avoid when
- Implementing backend database triggers.

## Failure modes
- Accepting a model's output stating 'I have verified this code' without running tests.

## Related pages
- [[failures/hallucination-cascade]]
- [[basics/what-is-an-agent]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "types/agent-types-overview",
        "title": "Agent Types Overview",
        "page_type": "catalog",
        "description": "An overview of different agent specializations and roles.",
        "tags": ["catalog", "types"],
        "body_markdown": """# Agent Types Overview
An overview of different agent specializations and roles.

Classifying agents into roles helps developers design appropriate tools, establish safety rails, and build specialized evaluation frameworks. General-purpose agents fail under complex constraints; specialized types excel when given narrow scopes.

### Available Agent Types
- [[types/coding-agent|Coding Agent]] - Modifies and validates source code.
- [[types/research-agent|Research Agent]] - Gathers and synthesizes info.
- [[types/support-agent|Support Agent]] - Interfaces with users.
- [[types/data-agent|Data Agent]] - Handles database queries and analysis.
- [[types/background-agent|Background Agent]] - Performs asynchronous audits.
- [[types/multi-agent-system|Multi-Agent System]] - Coordinates multiple specialized agents.

## Why it matters
Giving an agent too many tools or too broad a mandate increases the likelihood of tool misuse, planning failures, and infinite loops. Defining strict roles limits potential damage.

## Use when
- You are designing a multi-agent workforce or defining tool subsets.

## Avoid when
- The application only requires single-turn static generation.

## Failure modes
- Expecting a support agent to handle software engineering tasks without dedicated tools.

## Related pages
- [[types/coding-agent]]
- [[types/multi-agent-system]]
""",
    },
    {
        "slug": "types/coding-agent",
        "title": "Coding Agent",
        "page_type": "concept",
        "description": "An agent designed to generate, refactor, edit, and test software.",
        "tags": ["concept", "types"],
        "body_markdown": """# Coding Agent
An agent designed to generate, refactor, edit, and test software.

Coding agents require strict file read/write controls, local execution environments, and testing hooks. Never let an agent edit files without immediate automated compilation and verification tests.

## Why it matters
Unchecked code generation creates broken dependencies, syntax errors, and security vulnerabilities. Local validation is the primary line of defense.

## Use when
- Automating code refactoring or regression repair.
- Building autonomous dev tools.

## Avoid when
- Changes can be addressed with simple templates.

## Failure modes
- Rewriting working code blocks due to lack of local validation.

## Related pages
- [[types/agent-types-overview]]
- [[examples/coding-agent-example]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "types/research-agent",
        "title": "Research Agent",
        "page_type": "concept",
        "description": "An agent that aggregates, summarizes, and synthesizes information.",
        "tags": ["concept", "types"],
        "body_markdown": """# Research Agent
An agent that aggregates, summarizes, and synthesizes information.

Research agents rely heavily on search, browser capabilities, and strict source grounding to avoid hallucinations. They extract key facts and merge them into coherent documents while preserving citations.

## Why it matters
Unverified research outputs propagate false facts. Building strict grounding checks prevents the agent from synthesizing incorrect summaries.

## Use when
- Preparing market analysis or summarizing scientific papers.

## Avoid when
- Seeking precise mathematical calculations.

## Failure modes
- Confidently citing non-existent web sources.

## Related pages
- [[types/agent-types-overview]]
- [[examples/research-agent-example]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "types/support-agent",
        "title": "Support Agent",
        "page_type": "concept",
        "description": "A customer-facing agent that resolves user queries.",
        "tags": ["concept", "types"],
        "body_markdown": """# Support Agent
A customer-facing agent that resolves user queries.

Support agents need narrow write scopes and human-in-the-loop triggers for high-impact actions. They query knowledge catalogs and escalate issues when confidence falls below safety thresholds.

## Why it matters
A rogue support agent can delete customer accounts, leak private details, or promise false financial benefits. Strict tool gating is mandatory.

## Use when
- Triaging customer tickets and resolving basic queries.

## Avoid when
- The user requires complex, custom system troubleshooting.

## Failure modes
- Violating customer policies or leaking internal documentation.

## Related pages
- [[types/agent-types-overview]]
- [[examples/support-agent-example]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "types/data-agent",
        "title": "Data Agent",
        "page_type": "concept",
        "description": "An agent specializing in structured data queries and analysis.",
        "tags": ["concept", "types"],
        "body_markdown": """# Data Agent
An agent specializing in structured data queries and analysis.

Data agents write and execute SQL or Python code to extract insights from databases. They require read-only connection limits and query timeout safety valves to avoid server performance degradation.

## Why it matters
Poorly constrained SQL generation can cause table locks, leak sensitive datasets, or exhaust database connections.

## Use when
- Generating dynamic reports or aggregating spreadsheet datasets.

## Avoid when
- Standard BI dashboards provide the same data.

## Failure modes
- Executing an expensive nested query that exhausts server resources.

## Related pages
- [[types/agent-types-overview]]
- [[failures/infinite-loops]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "types/background-agent",
        "title": "Background Agent",
        "page_type": "concept",
        "description": "An agent running asynchronously to monitor or process systems.",
        "tags": ["concept", "types"],
        "body_markdown": """# Background Agent
An agent running asynchronously to monitor or process systems.

Background agents require strict time-out bounds, execution logging, and automated failure notifications. They execute tasks without direct human supervision.

## Why it matters
Undetected errors in background agents can run up huge API bills or corrupt databases silently before developers notice.

## Use when
- Running periodic system audits or data cleanup scripts.

## Avoid when
- Active, synchronous user dialogue is required to solve the task.

## Failure modes
- Getting stuck in infinite loops while running silently.

## Related pages
- [[types/agent-types-overview]]
- [[failures/infinite-loops]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "types/multi-agent-system",
        "title": "Multi-Agent System",
        "page_type": "concept",
        "description": "An architecture consisting of multiple collaborating agents.",
        "tags": ["concept", "types"],
        "body_markdown": """# Multi-Agent System
An architecture consisting of multiple collaborating agents.

Agents delegate tasks, share artifacts, and communicate using structured protocols. Multi-agent systems reduce complexity by separating concerns, but introduce coordination latency.

## Why it matters
Dividing complex goals among specialized agents prevents context window bloating and isolates tool permissions.

## Use when
- Goals require separate domains of expertise (e.g., coding + security auditing).

## Avoid when
- The task is straightforward and easily handled by a single agent.

## Failure modes
- Cyclic delegation loops between agents.

## Related pages
- [[types/agent-types-overview]]
- [[protocols/agent2agent]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "capabilities/capabilities-overview",
        "title": "Capabilities Overview",
        "page_type": "catalog",
        "description": "An overview of the core capabilities that power AI agents.",
        "tags": ["catalog", "capabilities"],
        "body_markdown": """# Capabilities Overview
An overview of the core capabilities that power AI agents.

Agents require capabilities beyond basic text completion. These include reasoning, planning, observation, tool use, retrieval, memory, and collaboration. Understanding how these components interact is key to building modular runtimes.

### Core Capabilities
- [[capabilities/reasoning|Reasoning]] - Logic and state analysis.
- [[capabilities/planning|Planning]] - Goal decomposition and adjustment.
- [[capabilities/observation|Observation]] - Processing feedback from the environment.
- [[capabilities/tool-use|Tool Use]] - Interacting with external systems.
- [[capabilities/retrieval|Retrieval]] - Fetching grounded facts.
- [[capabilities/memory|Memory]] - State persistence.
- [[capabilities/collaboration|Collaboration]] - Agent-to-agent coordination.

## Why it matters
An agent runtime is only as robust as its weakest capability. Separating and measuring each capability individually prevents untraceable failures.

## Use when
- Structuring your agent runtime software layers.

## Avoid when
- Calling raw API endpoints for basic text outputs.

## Failure modes
- Treating planning and execution as a single un-instrumented step.

## Related pages
- [[capabilities/planning]]
- [[capabilities/tool-use]]
""",
    },
    {
        "slug": "capabilities/reasoning",
        "title": "Reasoning",
        "page_type": "capability",
        "description": "The capacity to analyze information, draw conclusions, and handle logic.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Reasoning
The capacity to analyze information, draw conclusions, and handle logic.

Reasoning guides the agent's choice of tools and validates intermediate state transitions. It is the logical engine of the control loop.

## Why it matters
Without reasoning, the agent simply matches patterns without verifying if they make logical sense in the context of the user's goal.

## Use when
- Evaluating user inputs and planning logical dependencies.

## Avoid when
- Performing simple classification tasks.

## Failure modes
- Inventing false logical constraints.

## Related pages
- [[capabilities/capabilities-overview]]
- [[basics/the-illusion-of-agents]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "capabilities/planning",
        "title": "Planning",
        "page_type": "capability",
        "description": "Decomposing a primary goal into executable subtasks.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Planning
Decomposing a primary goal into executable subtasks.

Planning allows the agent to organize its execution sequence and update its plan dynamically as observations arrive. It is critical for managing long tasks.

## Why it matters
Unplanned execution leads to repetitive actions, high costs, and task failures.

## Use when
- Goals require multi-step operations over long periods.

## Avoid when
- The task can be solved in a single prompt step.

## Failure modes
- Rigid plans that fail to adapt to tool errors.

## Related pages
- [[capabilities/capabilities-overview]]
- [[strategies/plan-and-execute]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "capabilities/observation",
        "title": "Observation",
        "page_type": "capability",
        "description": "Processing feedback from the execution environment.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Observation
Processing feedback from the execution environment.

Observations include tool outputs, console errors, user inputs, and changes in database states. They close the loop of the agent's actions.

## Why it matters
Without accurate observation parsing, the agent cannot determine if its last action succeeded or failed.

## Use when
- The agent's next action depends on the outcome of the previous action.

## Avoid when
- Running blind fire-and-forget scripts.

## Failure modes
- Ignoring tool error codes and assuming success.

## Related pages
- [[capabilities/capabilities-overview]]
- [[failures/context-drift]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "capabilities/tool-use",
        "title": "Tool Use",
        "page_type": "capability",
        "description": "Interacting with the external world through executable code.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Tool Use
Interacting with the external world through executable code.

Tool use enables the agent to fetch data, write files, and perform actions. Tool access turns a model into an actor.

## Why it matters
Tool access is what transforms a language model from a generator into an active agent.

## Use when
- The task requires real-world data or system changes.

## Avoid when
- The task is strictly analytical and uses static text.

## Failure modes
- Executing destructive operations without validation.

## Related pages
- [[capabilities/capabilities-overview]]
- [[protocols/tool-calling]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "capabilities/retrieval",
        "title": "Retrieval",
        "page_type": "capability",
        "description": "Fetching relevant documents from external stores.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Retrieval
Fetching relevant documents from external stores.

Retrieval feeds the agent's context window with relevant evidence. RAG keeps agent decisions grounded in facts rather than model parameters.

## Why it matters
Grounded retrieval avoids hallucinations. Retrieval should happen before planning when the answer depends on specific or changing knowledge.

## Use when
- Answering questions about dynamic or private data.

## Avoid when
- The model's general knowledge is sufficient and verified.

## Failure modes
- Retrieving outdated or irrelevant documents.

## Related pages
- [[capabilities/capabilities-overview]]
- [[knowledge/okf-and-rag]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "capabilities/memory",
        "title": "Memory",
        "page_type": "capability",
        "description": "Persisting information across user sessions and system turns.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Memory
Persisting information across user sessions and system turns.

Memory tracks context, user preferences, and history. Memory is not the context window. The context window is temporary working space; memory is persisted information that can be recalled later.

## Why it matters
Without memory, agents treat every user session as starting from scratch.

## Use when
- Building long-running assistants or collaborative agents.

## Avoid when
- Processing isolated, stateless requests.

## Failure modes
- Bloated context windows leading to high costs.

## Related pages
- [[capabilities/capabilities-overview]]
- [[memory/context-vs-memory]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "capabilities/collaboration",
        "title": "Collaboration",
        "page_type": "capability",
        "description": "Coordinating work with humans or other agents.",
        "tags": ["capability", "capabilities"],
        "body_markdown": """# Collaboration
Coordinating work with humans or other agents.

Collaboration involves task delegation, feedback loops, and joint planning. It turns a single loop into a team.

## Why it matters
Complex tasks require coordination between specialized entities.

## Use when
- Solving multi-disciplinary problems.

## Avoid when
- Single-agent execution is faster and cheaper.

## Failure modes
- Miscommunication and conflicting actions.

## Related pages
- [[capabilities/capabilities-overview]]
- [[protocols/agent2agent]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "memory/context-vs-memory",
        "title": "Memory and Context Overview",
        "page_type": "catalog",
        "description": "How temporary context differs from persistent memory, and how both can fail.",
        "tags": ["catalog", "memory"],
        "body_markdown": """# Memory and Context Overview
How temporary context differs from persistent memory, and how both can fail.

Memory is not the context window. The context window is temporary working space; memory is persisted information that can be recalled later. Memory is only useful if it can be inspected, corrected, expired, and forgotten.

### Memory Concepts
- [[memory/context-window|Context Window]] - The immediate input limit.
- [[memory/short-term-memory|Short-Term Memory]] - Session history.
- [[memory/long-term-memory|Long-Term Memory]] - Cross-session storage.
- [[memory/episodic-memory|Episodic Memory]] - Record of events.
- [[memory/semantic-memory|Semantic Memory]] - Fact memory.
- [[memory/procedural-memory|Procedural Memory]] - Action patterns.
- [[memory/memory-risks|Memory Risks]] - Storage problems.

## Why it matters
Failing to split context and memory leads to bloated prompts, slow models, high bills, and stale information poisoning the reasoning engine.

## Use when
- Designing the data architecture of persistent assistants.

## Avoid when
- Deploying purely stateless completion APIs.

## Failure modes
- Letting memory grow without bounds until the model fails to process instructions.

## Related pages
- [[memory/context-window]]
- [[memory/long-term-memory]]
""",
    },
    {
        "slug": "memory/context-window",
        "title": "Context Window",
        "page_type": "memory",
        "description": "The immediate input limit a model can process in a single turn.",
        "tags": ["memory"],
        "body_markdown": """# Context Window
The immediate input limit a model can process in a single turn.

Context windows hold prompt instructions, recent history, and retrieved context. It is temporary working space.

## Why it matters
Model attention degrades when the context window is full, causing critical instructions to be ignored.

## Use when
- Setting prompt token budgets.

## Avoid when
- Persisting state across separate billing cycles.

## Failure modes
- Truncating system-level instructions silently.

## Related pages
- [[memory/context-vs-memory]]
- [[failures/context-drift]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/short-term-memory",
        "title": "Short-Term Memory",
        "page_type": "memory",
        "description": "Transient session state and conversation history.",
        "tags": ["memory"],
        "body_markdown": """# Short-Term Memory
Transient session state and conversation history.

Short-term memory tracks the active conversation turns. It preserves context during a single dialog thread.

## Why it matters
Ensures conversational continuity without requiring database fetches every single turn.

## Use when
- Maintaining dialog state during a chat session.

## Avoid when
- Saving settings that must persist across login events.

## Failure modes
- Memory loss upon page refreshes.

## Related pages
- [[memory/context-vs-memory]]
- [[memory/context-window]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/long-term-memory",
        "title": "Long-Term Memory",
        "page_type": "memory",
        "description": "Persistent storage for historical interactions and preferences.",
        "tags": ["memory"],
        "body_markdown": """# Long-Term Memory
Persistent storage for historical interactions and preferences.

Long-term memory spans multiple sessions and relies on external databases. It enables personalization.

## Why it matters
Allows systems to recall historical constraints, preventing redundant configurations and setup questions.

## Use when
- Persisting custom workflow settings.

## Avoid when
- Storing temporary scratch variables.

## Failure modes
- Out-of-date preferences poisoning current tasks.

## Related pages
- [[memory/context-vs-memory]]
- [[memory/memory-risks]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/episodic-memory",
        "title": "Episodic Memory",
        "page_type": "memory",
        "description": "Storing and recalling specific past events and experiences.",
        "tags": ["memory"],
        "body_markdown": """# Episodic Memory
Storing and recalling specific past events and experiences.

Episodic memory records "what happened when" in agent runs. It allows agents to avoid repeating mistakes.

## Why it matters
Enables agents to learn from past errors by looking up identical problem contexts.

## Use when
- Tracking task executions for regression prevention.

## Avoid when
- Storing static factual resources.

## Failure modes
- Poisoning future plans with outdated execution records.

## Related pages
- [[memory/context-vs-memory]]
- [[memory/long-term-memory]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/semantic-memory",
        "title": "Semantic Memory",
        "page_type": "memory",
        "description": "General facts and domain knowledge stored by the agent.",
        "tags": ["memory"],
        "body_markdown": """# Semantic Memory
General facts and domain knowledge stored by the agent.

Semantic memory acts as the agent's internal encyclopedia, separating facts from active conversation flows.

## Why it matters
Keeps domain knowledge separated from conversational chat history, simplifying retrieval paths.

## Use when
- Storing static domain facts.

## Avoid when
- Storing temporary state indicators.

## Failure modes
- Retaining outdated domain facts.

## Related pages
- [[memory/context-vs-memory]]
- [[memory/long-term-memory]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/procedural-memory",
        "title": "Procedural Memory",
        "page_type": "memory",
        "description": "Memory of instructions and workflow execution patterns.",
        "tags": ["memory"],
        "body_markdown": """# Procedural Memory
Memory of instructions and workflow execution patterns.

Procedural memory tells the agent "how" to do things, saving them from re-learning tool chains every turn.

## Why it matters
Allows agents to execute complex, multi-tool tasks efficiently by recalling successful action sequences.

## Use when
- Caching common multi-step sequences.

## Avoid when
- Saving static records or parameters.

## Failure modes
- Executing obsolete sequences against modified tool APIs.

## Related pages
- [[memory/context-vs-memory]]
- [[memory/long-term-memory]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "memory/memory-risks",
        "title": "Memory Risks",
        "page_type": "memory",
        "description": "Security, performance, and correctness issues in persistent agent memory.",
        "tags": ["memory"],
        "body_markdown": """# Memory Risks
Security, performance, and correctness issues in persistent agent memory.

Risks include memory bloat, stale context, and data leakage. Memory must be inspectable, correctable, and purgeable.

## Why it matters
Unmanaged memory turns agents into compliance risks and inflates API token costs.

## Use when
- Establishing memory cleanup cron jobs.

## Avoid when
- Running transient stateless pipelines.

## Failure modes
- Leaking PII from historical logs into a different user's session.

## Related pages
- [[memory/context-vs-memory]]
- [[failures/stale-memory]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "protocols/protocols-overview",
        "title": "Protocols Overview",
        "page_type": "catalog",
        "description": "Standardized communication systems connecting models, tools, and agents.",
        "tags": ["catalog", "protocols"],
        "body_markdown": """# Protocols Overview
Standardized communication systems connecting models, tools, and agents.

Protocols replace ad-hoc integration code with structured schemas for tool execution and multi-agent coordination. MCP standardizes model-to-tool and model-to-data access. A2A is for agent-to-agent coordination. They solve different problems.

### Core Protocols
- [[protocols/model-context-protocol|Model Context Protocol (MCP)]] - Model-to-tool standards.
- [[protocols/agent2agent|Agent-to-Agent (A2A)]] - Agent delegation standards.
- [[protocols/agent-communication-protocol|Agent Communication Protocol (ACP)]] - Message transports.
- [[protocols/tool-calling|Tool Calling]] - Schema conventions.
- [[protocols/handoffs|Handoffs]] - Escalation methods.

## Why it matters
Without structured protocols, multi-agent systems devolve into custom glue code that breaks whenever an API changes.

## Use when
- Designing the API contracts between different microservices or models.

## Avoid when
- Scripting simple single-file scripts.

## Failure modes
- Hand-writing custom JSON parsers for every new tool integration.

## Related pages
- [[protocols/model-context-protocol]]
- [[protocols/agent2agent]]
""",
    },
    {
        "slug": "protocols/model-context-protocol",
        "title": "Model Context Protocol",
        "page_type": "protocol",
        "description": "A protocol standardizing tool and data source access for models.",
        "tags": ["protocol"],
        "body_markdown": """# Model Context Protocol
A protocol standardizing tool and data source access for models.

MCP establishes client-server boundaries, standardizing how models retrieve context from databases, filesystems, and APIs, avoiding custom integration code.

## Why it matters
Standardizing access allows a model to use any server-compatible tool without writing integration-specific middleware.

## Use when
- Designing modular tool repositories.

## Avoid when
- Coordinating two separate autonomous agents.

## Failure modes
- Protocol version mismatches breaking tool executions.

## Related pages
- [[protocols/protocols-overview]]
- [[protocols/tool-calling]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "protocols/agent2agent",
        "title": "Agent to Agent Protocol",
        "page_type": "protocol",
        "description": "Protocols for agent discovery, delegation, and coordination.",
        "tags": ["protocol"],
        "body_markdown": """# Agent to Agent Protocol
Protocols for agent discovery, delegation, and coordination.

A2A enables agents to register capabilities, discover each other, delegate subtasks, and exchange structured artifacts.

## Why it matters
Enables complex, distributed workflows where specialized agents handle sub-problems.

## Use when
- Designing multi-agent systems.

## Avoid when
- A single agent has all required capabilities.

## Failure modes
- Cyclic delegation loops causing high token consumption.

## Related pages
- [[protocols/protocols-overview]]
- [[types/multi-agent-system]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "protocols/agent-communication-protocol",
        "title": "Agent Communication Protocol",
        "page_type": "protocol",
        "description": "Transport and messaging standard for asynchronous agent systems.",
        "tags": ["protocol"],
        "body_markdown": """# Agent Communication Protocol
Transport and messaging standard for asynchronous agent systems.

ACP defines envelope formats and metadata tags for message passing, ensuring messages remain delivery-guaranteed.

## Why it matters
Ensures reliable message delivery and tracing across asynchronous systems.

## Use when
- Running distributed background agent pools.

## Avoid when
- Implementing simple synchronous APIs.

## Failure modes
- Out-of-order message executions.

## Related pages
- [[protocols/protocols-overview]]
- [[protocols/agent2agent]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "protocols/tool-calling",
        "title": "Tool Calling",
        "page_type": "protocol",
        "description": "The structured format for model-to-environment action schemas.",
        "tags": ["protocol"],
        "body_markdown": """# Tool Calling
The structured format for model-to-environment action schemas.

Tool calling maps model outputs to function execution arguments. It ensures inputs pass validation before reaching target APIs.

## Why it matters
Strict schemas prevent arbitrary text inputs from hitting backend databases or APIs.

## Use when
- Integrating models with system APIs.

## Avoid when
- Outputs are pure markdown logs.

## Failure modes
- Parameter hallucination.

## Related pages
- [[protocols/protocols-overview]]
- [[protocols/model-context-protocol]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "protocols/handoffs",
        "title": "Handoffs",
        "page_type": "protocol",
        "description": "Relocating active session context between agents or human operators.",
        "tags": ["protocol"],
        "body_markdown": """# Handoffs
Relocating active session context between agents or human operators.

Handoffs require serializing memory state and context logs, preventing context loss.

## Why it matters
Smooth handoffs prevent user frustration and keep operations safe.

## Use when
- Escalating problems to human support staff.

## Avoid when
- A single agent has all required capabilities.

## Failure modes
- Losing conversation history during transitions.

## Related pages
- [[protocols/protocols-overview]]
- [[strategies/human-in-the-loop]]

## References
- Google Cloud: AI agents. [URL](https://cloud.google.com/use-cases/ai-agents)
""",
    },
    {
        "slug": "knowledge/knowledge-overview",
        "title": "Knowledge and Retrieval Overview",
        "page_type": "catalog",
        "description": "How agents store, retrieve, and ground operational knowledge.",
        "tags": ["catalog", "knowledge"],
        "body_markdown": """# Knowledge and Retrieval Overview
How agents store, retrieve, and ground operational knowledge.

Retrieval should happen before planning when the answer depends on specific or changing knowledge. A structured reference library keeps the agent grounded.

### Knowledge Subtopics
- [[knowledge/okf-and-rag|OKF and RAG]] - Documentation formats.
- [[knowledge/source-grounding|Source Grounding]] - Citing evidence.
- [[knowledge/stale-knowledge|Stale Knowledge]] - Document decay.
- [[knowledge/decision-records|Decision Records]] - ADR structures.
- [[knowledge/knowledge-ingestion|Knowledge Ingestion]] - Parsing pipelines.

## Why it matters
Relying on model parameters for specific software logic leads to code drift and broken builds. Grounding decisions in current documents is mandatory.

## Use when
- Implementing retrieval-augmented generation.

## Avoid when
- The agent does not need access to external resources.

## Failure modes
- Grounding outputs against unverified sources.

## Related pages
- [[knowledge/okf-and-rag]]
- [[knowledge/source-grounding]]
""",
    },
    {
        "slug": "knowledge/okf-and-rag",
        "title": "OKF and RAG",
        "page_type": "concept",
        "description": "Operational Knowledge Format structure supporting retrieval.",
        "tags": ["concept", "knowledge"],
        "body_markdown": """# OKF and RAG
Operational Knowledge Format structure supporting retrieval.

OKF enforces frontmatter schemas (title, type, tags) alongside markdown content, ensuring pages are easily indexed.

## Why it matters
Standardizing schemas allows tools to easily parse metadata and verify document integrity.

## Use when
- Organizing team wikis.

## Avoid when
- Storing temporary scratch notes.

## Failure modes
- Broken frontmatter formatting.

## Related pages
- [[knowledge/knowledge-overview]]
- [[meta/use-okf]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "knowledge/source-grounding",
        "title": "Source Grounding",
        "page_type": "concept",
        "description": "Ensuring agent claims map directly to indexed sources.",
        "tags": ["concept", "knowledge"],
        "body_markdown": """# Source Grounding
Ensuring agent claims map directly to indexed sources.

Grounding tracks citation paths from outputs back to raw sources, reducing hallucination risks.

## Why it matters
Grounded claims allow humans to audit agent suggestions instantly.

## Use when
- Compiling reports or policies.

## Avoid when
- Generating creative content.

## Failure modes
- Confidently citing incorrect documents.

## Related pages
- [[knowledge/knowledge-overview]]
- [[evaluation/groundedness]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "knowledge/stale-knowledge",
        "title": "Stale Knowledge",
        "page_type": "concept",
        "description": "The decay of cached or indexed documents over time.",
        "tags": ["concept", "knowledge"],
        "body_markdown": """# Stale Knowledge
The decay of cached or indexed documents over time.

Stale knowledge represents outdated policies or decommissioned tools. Old knowledge is worse than missing knowledge.

## Why it matters
Confidently wrong outputs are worse than admitting ignorance.

## Use when
- Reviewing wiki cache indexes.

## Avoid when
- Storing static archive records.

## Failure modes
- Recommending retired library APIs.

## Related pages
- [[knowledge/knowledge-overview]]
- [[failures/stale-memory]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "knowledge/decision-records",
        "title": "Decision Records",
        "page_type": "concept",
        "description": "Persisting architectural and design choices within the knowledge base.",
        "tags": ["concept", "knowledge"],
        "body_markdown": """# Decision Records
Persisting architectural and design choices within the knowledge base.

ADRs explain the context, decision, and consequences of choices. They prevent agents from violating project rules.

## Why it matters
Keeps agents from proposing changes that violate established project decisions.

## Use when
- Documenting team design choices.

## Avoid when
- Writing code-level comments.

## Failure modes
- Rule conflicts from outdated ADRs.

## Related pages
- [[knowledge/knowledge-overview]]
- [[meta/use-okf]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "knowledge/knowledge-ingestion",
        "title": "Knowledge Ingestion",
        "page_type": "concept",
        "description": "The pipeline for parsing, tagging, and indexing raw files.",
        "tags": ["concept", "knowledge"],
        "body_markdown": """# Knowledge Ingestion
The pipeline for parsing, tagging, and indexing raw files.

Ingestion extracts text and builds OKF metadata. A garbage-in garbage-out pipeline ruins retrieval quality.

## Why it matters
Ensures standard tags are created, allowing models to search precisely.

## Use when
- Indexing external repositories.

## Avoid when
- Appending runtime session entries.

## Failure modes
- Tagging files incorrectly.

## Related pages
- [[knowledge/knowledge-overview]]
- [[knowledge/okf-and-rag]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "strategies/strategies-overview",
        "title": "Strategies and Patterns Overview",
        "page_type": "catalog",
        "description": "Standard patterns and control loops for managing agent behavior.",
        "tags": ["catalog", "strategies"],
        "body_markdown": """# Strategies and Patterns Overview
Standard patterns and control loops for managing agent behavior.

Agent execution strategies determine how the model interacts with tools, planning steps, and human operators. The right control loop ensures high success rates and low token consumption.

### Core Strategies
- [[strategies/retrieval-first|Retrieval First]] - Pull facts before planning.
- [[strategies/narrow-agent-scope|Narrow Agent Scope]] - Constrain tool scopes.
- [[strategies/human-in-the-loop|Human in the Loop]] - Escalate before writing.
- [[strategies/plan-and-execute|Plan and Execute]] - Split task steps.
- [[strategies/react-loop|ReAct Loop]] - Alternate thinking and acting.
- [[strategies/fail-safe-actions|Fail-Safe Actions]] - Handle errors gracefully.

## Why it matters
Without clear loop boundaries, agents will default to unbounded execution, generating infinite tool loops and wasting resources.

## Use when
- Designing the main loop runtime.

## Avoid when
- Coding simple APIs.

## Failure modes
- Over-complicating predictable tasks.

## Related pages
- [[strategies/retrieval-first]]
- [[strategies/human-in-the-loop]]
""",
    },
    {
        "slug": "strategies/retrieval-first",
        "title": "Retrieval First",
        "page_type": "strategy",
        "description": "Performing retrieval before planning or generating answers.",
        "tags": ["strategy", "retrieval"],
        "body_markdown": """# Retrieval First
Performing retrieval before planning or generating answers.

Retrieval should happen before planning when the answer depends on specific or changing knowledge. This keeps the agent grounded.

## Why it matters
Planning from memory leads to obsolete steps. Fetching facts first guarantees accurate workflows.

## Use when
- Tasks depend on dynamic codebase references.

## Avoid when
- Running static statistical evaluations.

## Failure modes
- Planning based on outdated assumptions.

## Related pages
- [[strategies/strategies-overview]]
- [[capabilities/retrieval]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "strategies/narrow-agent-scope",
        "title": "Narrow Agent Scope",
        "page_type": "strategy",
        "description": "Restricting agent goals, tools, and permissions.",
        "tags": ["strategy"],
        "body_markdown": """# Narrow Agent Scope
Restricting agent goals, tools, and permissions.

Narrow agent scopes make testing and validation predictable. Give agents a single job, limited tools, and clear stop conditions.

## Why it matters
Broad scopes lead to tool misuse, planning drift, and infinite execution loops.

## Use when
- Architecting microservices.

## Avoid when
- Testing model capability limits.

## Failure modes
- Rogue file deletions.

## Related pages
- [[strategies/strategies-overview]]
- [[basics/agent-vs-workflow]]

## References
- Google Cloud: AI agents. [URL](https://cloud.google.com/use-cases/ai-agents)
""",
    },
    {
        "slug": "strategies/human-in-the-loop",
        "title": "Human in the Loop",
        "page_type": "strategy",
        "description": "Inserting human gates for destructive or expensive actions.",
        "tags": ["strategy"],
        "body_markdown": """# Human in the Loop
Inserting human gates for destructive or expensive actions.

Ask for confirmation when an action is destructive, expensive, externally visible, legally sensitive, or hard to reverse. Use an assistant when the human should stay in control.

## Why it matters
Prevents irreversible losses (deleting files, moving money) before human validation.

## Use when
- Modifying production servers or performing financial operations.

## Avoid when
- Executing read-only queries.

## Failure modes
- Human fatigue from too many approvals.

## Related pages
- [[strategies/strategies-overview]]
- [[protocols/handoffs]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "strategies/plan-and-execute",
        "title": "Plan and Execute",
        "page_type": "strategy",
        "description": "Separating execution planning from task execution.",
        "tags": ["strategy"],
        "body_markdown": """# Plan and Execute
Separating execution planning from task execution.

The agent drafts a static plan, then executes tasks sequentially.

## Why it matters
Saves tokens by avoiding planning overhead at every single step.

## Use when
- Tasks are long and predictable.

## Avoid when
- Action environment changes constantly.

## Failure modes
- Continuing execution on broken subtasks.

## Related pages
- [[strategies/strategies-overview]]
- [[capabilities/planning]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "strategies/react-loop",
        "title": "ReAct Loop",
        "page_type": "strategy",
        "description": "Interleaving reasoning and action steps dynamically.",
        "tags": ["strategy"],
        "body_markdown": """# ReAct Loop
Interleaving reasoning and action steps dynamically.

ReAct loops allow immediate adaptation to environment feedback by repeating reasoning-acting-observation sequences.

## Why it matters
Required for exploring volatile systems where actions change the target state.

## Use when
- Debugging system failures.

## Avoid when
- Budgets and latency need tight caps.

## Failure modes
- Tool overuse loops.

## Related pages
- [[strategies/strategies-overview]]
- [[capabilities/reasoning]]

## References
- OpenAI Agents SDK. [URL](https://github.com/openai/openai-agents)
""",
    },
    {
        "slug": "strategies/fail-safe-actions",
        "title": "Fail-Safe Actions",
        "page_type": "strategy",
        "description": "Handling tool errors and validation failures gracefully.",
        "tags": ["strategy"],
        "body_markdown": """# Fail-Safe Actions
Handling tool errors and validation failures gracefully.

Define fallback behaviors when tools fail or validation rejects outputs, preventing agent crashes.

## Why it matters
Prevents runaway retries from running up bills.

## Use when
- Interfacing with third-party APIs.

## Avoid when
- Failures represent critical system blocks.

## Failure modes
- Infinite retry loops.

## Related pages
- [[strategies/strategies-overview]]
- [[failures/infinite-loops]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "evaluation/evaluation-overview",
        "title": "Evaluation Overview",
        "page_type": "catalog",
        "description": "Metrics and strategies for evaluating agent systems.",
        "tags": ["catalog", "evaluation"],
        "body_markdown": """# Evaluation Overview
Metrics and strategies for evaluating agent systems.

Agent evaluation must check the path, not only the final answer. Inspecting the trajectory checks what the agent did, which tools it called, and whether it stopped at the right time.

### Evaluation Metrics
- [[evaluation/task-success|Task Success]] - Completion rates.
- [[evaluation/groundedness|Groundedness]] - Fact checks.
- [[evaluation/tool-use-quality|Tool-Use Quality]] - API parameter audits.
- [[evaluation/trajectory-evaluation|Trajectory Evaluation]] - Path audits.
- [[evaluation/cost-and-latency|Cost and Latency]] - Budget checks.
- [[evaluation/regression-tests|Regression Tests]] - Scenario validation.

## Why it matters
Evaluating only final answers hides loop errors, tool parameter hallucinations, and cost overhead. Trajectory checking is mandatory.

## Use when
- Defining CI/CD testing gates.

## Avoid when
- Designing mock UI layouts.

## Failure modes
- Overlooking high costs because the final answer was correct.

## Related pages
- [[evaluation/trajectory-evaluation]]
- [[evaluation/regression-tests]]
""",
    },
    {
        "slug": "evaluation/task-success",
        "title": "Task Success",
        "page_type": "evaluation",
        "description": "Measuring whether the agent successfully resolved the goal.",
        "tags": ["evaluation"],
        "body_markdown": """# Task Success
Measuring whether the agent successfully resolved the goal.

Task success metrics use binary passes or user satisfaction ratings.

## Why it matters
Provides the primary baseline metric for user experience.

## Use when
- Reviewing client satisfaction logs.

## Avoid when
- Profiling execution bottlenecks.

## Failure modes
- Marking incomplete tasks as successful due to polite wording.

## Related pages
- [[evaluation/evaluation-overview]]
- [[evaluation/trajectory-evaluation]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "evaluation/groundedness",
        "title": "Groundedness",
        "page_type": "evaluation",
        "description": "Verifying that outputs are supported by retrieved sources.",
        "tags": ["evaluation"],
        "body_markdown": """# Groundedness
Verifying that outputs are supported by retrieved sources.

Groundedness checks detect hallucinated information.

## Why it matters
Ungrounded statements lead to system distrust.

## Use when
- Deploying search engines.

## Avoid when
- Generating creative content.

## Failure modes
- Confidently wrong outputs passing syntax checks.

## Related pages
- [[evaluation/evaluation-overview]]
- [[knowledge/source-grounding]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "evaluation/tool-use-quality",
        "title": "Tool Use Quality",
        "page_type": "evaluation",
        "description": "Auditing the selection and parameters of tool calls.",
        "tags": ["evaluation"],
        "body_markdown": """# Tool Use Quality
Auditing the selection and parameters of tool calls.

Measure if correct tools were called with appropriate inputs.

## Why it matters
Prevents tool over-use and parameter drift.

## Use when
- Optimizing integration layers.

## Avoid when
- Developing agents with no tools.

## Failure modes
- Missing invalid JSON payloads in tests.

## Related pages
- [[evaluation/evaluation-overview]]
- [[protocols/tool-calling]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "evaluation/trajectory-evaluation",
        "title": "Trajectory Evaluation",
        "page_type": "evaluation",
        "description": "Inspecting the full step-by-step path of the agent.",
        "tags": ["evaluation"],
        "body_markdown": """# Trajectory Evaluation
Inspecting the full step-by-step path of the agent.

Evaluate each reasoning step, tool call, and state transition. Agent evaluation must check the path, not only the final answer.

## Why it matters
Essential for detecting infinite loops and redundant work.

## Use when
- Analyzing performance bottlenecks.

## Avoid when
- Doing simple single-prompt completions.

## Failure modes
- Ignoring long, expensive loops that happen to finish.

## Related pages
- [[evaluation/evaluation-overview]]
- [[failures/infinite-loops]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "evaluation/cost-and-latency",
        "title": "Cost and Latency",
        "page_type": "evaluation",
        "description": "Monitoring token spend and execution duration.",
        "tags": ["evaluation"],
        "body_markdown": """# Cost and Latency
Monitoring token spend and execution duration.

Track overhead from planning runs and tool calls.

## Why it matters
High costs or slow runs render agents commercially useless.

## Use when
- Budgeting operations.

## Avoid when
- Evaluating raw capability bounds.

## Failure modes
- Unbounded loops inflating API bills.

## Related pages
- [[evaluation/evaluation-overview]]
- [[failures/infinite-loops]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "evaluation/regression-tests",
        "title": "Regression Tests",
        "page_type": "evaluation",
        "description": "Running historical failure scenarios to check for regressions.",
        "tags": ["evaluation"],
        "body_markdown": """# Regression Tests
Running historical failure scenarios to check for regressions.

Compile fixed datasets of failure logs and verify behavior.

## Why it matters
Ensures updates do not reintroduce old bugs.

## Use when
- Committing system changes.

## Avoid when
- Gathering general user feedback.

## Failure modes
- Tests becoming stale when APIs change.

## Related pages
- [[evaluation/evaluation-overview]]
- [[meta/error-book]]

## References
- Databricks: Agent Evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation)
""",
    },
    {
        "slug": "failures/failure-modes-overview",
        "title": "Failure Modes Overview",
        "page_type": "catalog",
        "description": "Cataloging common pitfalls in autonomous agent executions.",
        "tags": ["catalog", "failures"],
        "body_markdown": """# Failure Modes Overview
Cataloging common pitfalls in autonomous agent executions.

Failure modes should be named so they can be detected, tested, and repaired. Understanding failure types prevents deployment of unstable pipelines.

### Classical Failure Modes
- [[failures/context-drift|Context Drift]] - Goal focus decay.
- [[failures/tool-overuse|Tool Overuse]] - Runaway API calls.
- [[failures/hallucination-cascade|Hallucination Cascade]] - Compounding logic errors.
- [[failures/hallucinated-tools|Hallucinated Tools]] - Fictional API calls.
- [[failures/stale-memory|Stale Memory]] - Out-of-date states.
- [[failures/infinite-loops|Infinite Loops]] - Repetitive execution.
- [[failures/data-leakage|Data Leakage]] - Privacy breaches.

## Why it matters
Identifying failure signatures allows developers to write automated validators and circuit breakers.

## Use when
- Reviewing trace logs of failed system runs.

## Avoid when
- Structuring basic data tables.

## Failure modes
- Failing to detect infinite loops until credit limits are hit.

## Related pages
- [[failures/infinite-loops]]
- [[failures/context-drift]]
""",
    },
    {
        "slug": "failures/context-drift",
        "title": "Context Drift",
        "page_type": "failure-mode",
        "description": "The agent losing focus of the original goal over long runs.",
        "tags": ["failure-mode"],
        "body_markdown": """# Context Drift
The agent losing focus of the original goal over long runs.

Conversation logs fill with intermediate findings, drowning out instructions.

## Why it matters
Leads to irrelevant actions and task abandonment.

## Use when
- Designing long task loops.

## Avoid when
- Processing single queries.

## Failure modes
- Abandoning the user's primary task.

## Related pages
- [[failures/failure-modes-overview]]
- [[memory/context-window]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "failures/tool-overuse",
        "title": "Tool Overuse",
        "page_type": "failure-mode",
        "description": "Repeatedly calling tools without making progress.",
        "tags": ["failure-mode"],
        "body_markdown": """# Tool Overuse
Repeatedly calling tools without making progress.

The agent queries the same tool with minor variants.

## Why it matters
Inflates token costs and execution time.

## Use when
- Auditing trace logs.

## Avoid when
- Using static code execution.

## Failure modes
- Calling the same search API 20 times.

## Related pages
- [[failures/failure-modes-overview]]
- [[capabilities/tool-use]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "failures/hallucination-cascade",
        "title": "Hallucination Cascade",
        "page_type": "failure-mode",
        "description": "An initial false assumption compounding into a complete failure.",
        "tags": ["failure-mode"],
        "body_markdown": """# Hallucination Cascade
An initial false assumption compounding into a complete failure.

One wrong observation leads to a wrong plan, which yields wrong tools.

## Why it matters
Output appears logical but is completely detached from reality.

## Use when
- Reviewing multi-step failures.

## Avoid when
- Inspecting single prompt outputs.

## Failure modes
- Generating fictional plans.

## Related pages
- [[failures/failure-modes-overview]]
- [[basics/the-illusion-of-agents]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "failures/hallucinated-tools",
        "title": "Hallucinated Tools",
        "page_type": "failure-mode",
        "description": "The model attempting to invoke tools that do not exist.",
        "tags": ["failure-mode"],
        "body_markdown": """# Hallucinated Tools
The model attempting to invoke tools that do not exist.

The planner invents function names or uses wrong schemas.

## Why it matters
Causes immediate code crashes unless schema validation blocks them.

## Use when
- Debugging tool schemas.

## Avoid when
- No external tools are provided.

## Failure modes
- Invoking fictional functions.

## Related pages
- [[failures/failure-modes-overview]]
- [[protocols/tool-calling]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "failures/stale-memory",
        "title": "Stale Memory",
        "page_type": "failure-mode",
        "description": "The agent acting on outdated user state or preferences.",
        "tags": ["failure-mode"],
        "body_markdown": """# Stale Memory
The agent acting on outdated user state or preferences.

Outdated variables poison the reasoning engine.

## Why it matters
Keeps agents from adopting new directions.

## Use when
- Defining memory eviction strategies.

## Avoid when
- Working in transient stateless contexts.

## Failure modes
- Applying old rules to new projects.

## Related pages
- [[failures/failure-modes-overview]]
- [[memory/memory-risks]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "failures/infinite-loops",
        "title": "Infinite Loops",
        "page_type": "failure-mode",
        "description": "The agent repeating a sequence of actions without stopping.",
        "tags": ["failure-mode"],
        "body_markdown": """# Infinite Loops
The agent repeating a sequence of actions without stopping.

Usually caused by missing or ambiguous success criteria.

## Why it matters
Exhausts rate limits and budgets.

## Use when
- Enforcing runtime guards.

## Avoid when
- Running deterministic chains.

## Failure modes
- Stuck retrying the same failing tool.

## Related pages
- [[failures/failure-modes-overview]]
- [[strategies/fail-safe-actions]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "failures/data-leakage",
        "title": "Data Leakage",
        "page_type": "failure-mode",
        "description": "Inadvertently exposing sensitive context or logs.",
        "tags": ["failure-mode"],
        "body_markdown": """# Data Leakage
Inadvertently exposing sensitive context or logs.

Retrieval grabs private documents and sends them to API providers.

## Why it matters
Violates privacy policies and data regulations.

## Use when
- Securing database retrieval paths.

## Avoid when
- Using completely local runtimes.

## Failure modes
- Leaking customer PII in outbound queries.

## Related pages
- [[failures/failure-modes-overview]]
- [[memory/memory-risks]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "examples/examples-overview",
        "title": "Examples Overview",
        "page_type": "catalog",
        "description": "A collection of representative agent implementations.",
        "tags": ["catalog", "examples"],
        "body_markdown": """# Examples Overview
A collection of representative agent implementations.

Real-world examples demonstrate how capabilities, memory, and protocols combine to build functional agents.

### Example Guides
- [[examples/coding-agent-example|Coding Agent Example]] - Local code repair.
- [[examples/research-agent-example|Research Agent Example]] - Grounded web search.
- [[examples/support-agent-example|Support Agent Example]] - Customer ticket triage.

## Why it matters
Concrete layouts teach configuration patterns better than abstract strategies.

## Use when
- Designing the software interface layer.

## Avoid when
- Coding isolated arithmetic scripts.

## Failure modes
- Copying permissions models directly without custom audit bounds.

## Related pages
- [[examples/coding-agent-example]]
- [[types/agent-types-overview]]
""",
    },
    {
        "slug": "examples/coding-agent-example",
        "title": "Coding Agent Example",
        "page_type": "example",
        "description": "Example walkthrough of a local software maintenance agent.",
        "tags": ["example"],
        "body_markdown": """# Coding Agent Example
Example walkthrough of a local software maintenance agent.

Details how the agent reads files, edits, runs tests, and logs revisions.

## Why it matters
Shows practical integration of tool boundaries.

## Use when
- Building developer automation tools.

## Avoid when
- Designing chat assistants.

## Failure modes
- Missing build checks.

## Related pages
- [[examples/examples-overview]]
- [[types/coding-agent]]

## References
- Anthropic: MCP. [URL](https://modelcontextprotocol.io/)
""",
    },
    {
        "slug": "examples/research-agent-example",
        "title": "Research Agent Example",
        "page_type": "example",
        "description": "Example walkthrough of a web-researching synthesis agent.",
        "tags": ["example"],
        "body_markdown": """# Research Agent Example
Example walkthrough of a web-researching synthesis agent.

Explains search scraping, source grounding, and markdown synthesis.

## Why it matters
Demonstrates source grounding in action.

## Use when
- Building summarization bots.

## Avoid when
- Writing direct database connectors.

## Failure modes
- Scraping duplicate sites.

## Related pages
- [[examples/examples-overview]]
- [[types/research-agent]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "examples/support-agent-example",
        "title": "Support Agent Example",
        "page_type": "example",
        "description": "Example walkthrough of a ticket triage agent.",
        "tags": ["example"],
        "body_markdown": """# Support Agent Example
Example walkthrough of a ticket triage agent.

Details intent classification, policy lookup, and escalation rules.

## Why it matters
Teaches how to build human gates.

## Use when
- Implementing helpdesk bots.

## Avoid when
- Writing developer scripts.

## Failure modes
- Wrong intent classification.

## Related pages
- [[examples/examples-overview]]
- [[types/support-agent]]

## References
- IBM: AI agents. [URL](https://www.ibm.com/think/topics/ai-agents)
""",
    },
    {
        "slug": "meta/use-okf",
        "title": "Use OKF",
        "page_type": "decision",
        "description": "The rationale and rules behind using Operational Knowledge Format.",
        "tags": ["decision", "meta"],
        "body_markdown": """# Use OKF
The rationale and rules behind using Operational Knowledge Format.

OKF enforces structure, tag constraints, and link checks over documentation, making it readable for both models and humans.

## Why it matters
Keeps pages auditable, preventing knowledge decay.

## Use when
- Adding design decisions.

## Avoid when
- Recording temporary chat scripts.

## Failure modes
- Broken frontmatter tags.

## Related pages
- [[knowledge/okf-and-rag]]
- [[meta/wiki-workflow]]
- [[meta/okf-internals]]
- [[meta/self-describing-wiki]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "meta/wiki-workflow",
        "title": "Wiki Workflow",
        "page_type": "guide",
        "description": "The process of ingesting raw sources and writing wiki pages.",
        "tags": ["guide", "meta"],
        "body_markdown": """# Wiki Workflow
The process of ingesting raw sources and writing wiki pages.

Defines the loop of ingesting, checking link structures, and running lint.

## Why it matters
Ensures the knowledge base remains healthy and up to date.

## Use when
- Training team members.

## Avoid when
- Modifying system code files.

## Failure modes
- Adding orphan pages.

## Related pages
- [[meta/use-okf]]
- [[meta/lint-rules]]
- [[meta/sources]]
- [[meta/operation-log]]
- [[meta/error-book]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "meta/lint-rules",
        "title": "Lint Rules",
        "page_type": "guide",
        "description": "Structural rules checked by the wiki linter.",
        "tags": ["guide", "meta"],
        "body_markdown": """# Lint Rules
Structural rules checked by the wiki linter.

Lints find broken links, missing metadata fields, and invalid types.

## Why it matters
Prevents structural decay of the knowledge graph.

## Use when
- Editing validation scripts.

## Avoid when
- Formatting Python source code.

## Failure modes
- Ignoring lint outputs.

## Related pages
- [[meta/wiki-workflow]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "meta/sources",
        "title": "Sources Catalog",
        "page_type": "catalog",
        "description": "The catalog of reference sources grounding the wiki content.",
        "tags": ["catalog", "meta"],
        "body_markdown": """# Sources Catalog
The catalog of reference sources grounding the wiki content.

Contains references to Google, IBM, Anthropic, Databricks, and other industry standards. Grounding content in established research ensures the advice is practical.

### Industry Standards
- **Google Cloud**: AI agents definition and features. [URL](https://cloud.google.com/use-cases/ai-agents) (Related: [[basics/what-is-an-agent]], [[basics/agent-vs-assistant-vs-bot]])
- **IBM**: AI agents and A2A protocol. [URL](https://www.ibm.com/think/topics/ai-agents) (Related: [[basics/what-is-an-agent]], [[protocols/agent2agent]])
- **Anthropic**: MCP specification. [URL](https://modelcontextprotocol.io/) (Related: [[protocols/model-context-protocol]], [[capabilities/tool-use]])
- **OpenAI**: Agents SDK concepts. [URL](https://github.com/openai/openai-agents) (Related: [[basics/agent-vs-workflow]], [[protocols/tool-calling]])
- **Databricks**: Agent evaluation. [URL](https://www.databricks.com/blog/introducing-agent-evaluation) (Related: [[evaluation/evaluation-overview]], [[knowledge/source-grounding]])
- **Galileo**: Agent failure modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging) (Related: [[failures/failure-modes-overview]], [[failures/infinite-loops]])
- **Weaviate**: Context engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag) (Related: [[memory/context-vs-memory]], [[capabilities/retrieval]])
- **OKF**: Knowledge catalog specification. [URL](https://cloud.google.com/knowledge-catalog) (Related: [[knowledge/okf-and-rag]], [[meta/use-okf]])

## Why it matters
Auditable citations ensure that developers can trace wiki recommendations back to raw evidence.

## Use when
- Fact-checking page guidelines.

## Related pages
- [[meta/wiki-workflow]]
""",
    },
    {
        "slug": "tools/qdrant",
        "title": "Qdrant",
        "page_type": "tool",
        "description": "A vector database tool for semantic retrieval.",
        "tags": ["tool"],
        "body_markdown": """# Qdrant
A vector database tool for semantic retrieval.

Stores numeric embeddings representing text meaning to support semantic queries.

## Why it matters
Crucial for scaling retrieval over large datasets, though simple wikis can use basic keyword search.

## Use when
- Scaling RAG pipelines beyond single databases.

## Avoid when
- Keyword matching handles all user queries.

## Failure modes
- Out-of-sync vector indices.

## Related pages
- [[knowledge/okf-and-rag]]
- [[tools/cognee]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "tools/cognee",
        "title": "Cognee",
        "page_type": "tool",
        "description": "A framework giving agents persistent memory using knowledge graphs.",
        "tags": ["tool"],
        "body_markdown": """# Cognee
A framework giving agents persistent memory using knowledge graphs.

Cognee extracts, cognifies, and loads data entities and relationships.

## Why it matters
Keeps agents from losing complex relational state.

## Use when
- Storing rich entity graphs across sessions.

## Avoid when
- Flat key-value stores are sufficient.

## Failure modes
- Entity definition drift.

## Related pages
- [[memory/context-vs-memory]]
- [[tools/qdrant]]

## References
- Weaviate: Context Engineering. [URL](https://weaviate.io/developers/weaviate/concepts/rag)
""",
    },
    {
        "slug": "meta/okf-internals",
        "title": "OKF Internals",
        "page_type": "meta",
        "description": "Technical parsing details for the OKF parser.",
        "tags": ["meta"],
        "body_markdown": """# OKF Internals
Technical parsing details for the OKF parser.

Explains how split and metadata regex extract fields and body content.

## Why it matters
Helps developers debug database insertions.

## Use when
- Extending the metadata schema.

## Avoid when
- Just writing new content pages.

## Failure modes
- Regex failures on weird character inputs.

## Related pages
- [[meta/use-okf]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "meta/self-describing-wiki",
        "title": "Self-Describing Wiki",
        "page_type": "meta",
        "description": "Documentation explaining the self-referential nature of Agent Rebel.",
        "tags": ["meta"],
        "body_markdown": """# Self-Describing Wiki
Documentation explaining the self-referential nature of Agent Rebel.

The wiki operates as both a user reference and a blueprint for structured knowledge stores.

## Why it matters
Showcases how models interact with structured knowledge nodes.

## Use when
- Analyzing the architecture of the wiki.

## Avoid when
- Writing simple content pages.

## Failure modes
- Circular definitions.

## Related pages
- [[meta/use-okf]]

## References
- OKF Catalog. [URL](https://cloud.google.com/knowledge-catalog)
""",
    },
    {
        "slug": "meta/error-book",
        "title": "Error Book",
        "page_type": "meta",
        "description": "A queue to record repeated wiki layout and behavior errors.",
        "tags": ["meta"],
        "body_markdown": """# Error Book
A queue to record repeated wiki layout and behavior errors.

Used to identify areas of knowledge decay.

## Why it matters
Ensures continuous improvement of content.

## Use when
- Resolving recurring user bugs.

## Avoid when
- Writing code logs.

## Failure modes
- Log spam.

## Related pages
- [[meta/wiki-workflow]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
    {
        "slug": "meta/operation-log",
        "title": "Operation Log",
        "page_type": "meta",
        "description": "Human-readable mirror of wiki operations.",
        "tags": ["meta"],
        "body_markdown": """# Operation Log
Human-readable mirror of wiki operations.

Logs creations, edits, and in-app actions.

## Why it matters
Critical for trace audits.

## Use when
- Reviewing editor history.

## Avoid when
- Inspecting code runtime logs.

## Failure modes
- Bloated log tables.

## Related pages
- [[meta/wiki-workflow]]

## References
- Galileo: Agent Failure Modes. [URL](https://www.rungalileo.io/blog/mastering-agent-evaluation-and-debugging)
""",
    },
]


def sync_wiki_from_disk(conn) -> None:
    from app.config import wiki_directory
    from app.okf import page_to_okf, parse_okf

    wiki_dir = wiki_directory()
    wiki_dir.mkdir(parents=True, exist_ok=True)

    from app.config import current_wiki_id

    is_agent_wiki = current_wiki_id() == "agent"

    md_files = list(wiki_dir.glob("**/*.md"))
    if not md_files and is_agent_wiki:
        for page in SEED_PAGES:
            slug = page["slug"]
            file_path = wiki_dir / f"{slug}.md"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            okf_content = page_to_okf(page)
            file_path.write_text(okf_content, encoding="utf-8")
        md_files = list(wiki_dir.glob("**/*.md"))

    conn.execute("DELETE FROM pages")
    conn.execute("DELETE FROM links")

    for file_path in md_files:
        try:
            rel_path = file_path.relative_to(wiki_dir)
            slug = str(rel_path.with_suffix("")).replace("\\", "/")
            content = file_path.read_text(encoding="utf-8")
            okf = parse_okf(content)
            save_page(
                conn,
                slug=slug,
                title=okf.title,
                page_type=okf.page_type,
                section=okf.section,
                section_title=okf.section_title,
                section_order=okf.section_order,
                nav_order=okf.nav_order,
                description=okf.description,
                body_markdown=okf.body_markdown,
                tags=okf.tags,
                change_summary="Synced from disk.",
                actor="system",
                write_to_disk=False,
            )
        except Exception as e:
            print(f"Error syncing {file_path}: {e}")

    conn.execute("DELETE FROM sources")
    if is_agent_wiki:
        for source in SEED_SOURCES:
            create_source(conn, **source)
    else:
        sources_dir = wiki_dir.parent / "sources"
        if sources_dir.is_dir():
            for file_path in sorted(sources_dir.glob("*.md")):
                try:
                    okf = parse_okf(file_path.read_text(encoding="utf-8"))
                    create_source(
                        conn,
                        slug=f"source/{file_path.stem}",
                        title=okf.title,
                        source_type=okf.page_type,
                        content=okf.body_markdown,
                    )
                except Exception as e:
                    print(f"Error ingesting source {file_path}: {e}")

    rebuild_all_links(conn)
    lint_all(conn)
    conn.commit()


def seed_if_empty(conn) -> None:
    sync_wiki_from_disk(conn)
