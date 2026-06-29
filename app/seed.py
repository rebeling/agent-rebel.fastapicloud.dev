from app.lint import lint_all
from app.repository import rebuild_all_links, save_page


SEED_PAGES = [
    {
        "slug": "index",
        "title": "The Agent Knowledge Base",
        "page_type": "catalog",
        "description": "A structured reference for understanding, designing, and evaluating AI agents.",
        "tags": ["catalog", "agent-strategy"],
        "body_markdown": """# The Agent Knowledge Base

Agent Rebel is a structured reference for understanding, designing, and evaluating AI agents.

Explore agent types, capabilities, protocols, memory systems, knowledge strategies, evaluation methods, and common failure modes.

The knowledge base draws on open research, technical documentation, and field practice to explain how agents differ from assistants or chatbots, what kinds of agents exist, which protocols let agents access tools or collaborate, what capabilities and memory systems they need, how to evaluate them, and which failure modes to avoid.

Use it as a field manual, not a chat app. The first job is to make agent knowledge readable, browsable, editable, and structured.

The wiki idea is simple:

- raw sources hold evidence and notes
- OKF pages turn that material into reusable knowledge
- schema and lint rules keep the knowledge inspectable
- humans curate the judgment
- future LLM tools can maintain pages, but they do not own the truth

The operating loop is [[guides/ingest-query-lint|Ingest, Query, Lint]]. Ingest raw material, query the wiki while working, then lint the structure so links, types, and missing context stay visible.

Start here:

- [[concepts/okf-wiki|OKF wiki]]
- [[concepts/sources-wiki-schema|Sources, wiki, schema]]
- [[guides/ingest-query-lint|Ingest, query, lint]]
- [[guides/wiki-workflow|Wiki workflow]]
- [[concepts/what-is-an-agent|What is an agent]]
- [[concepts/agent-vs-workflow|Agent vs workflow]]
- [[concepts/agent-categories|Agent categories]]
- [[protocols/agent-protocols|Agent protocols]]
- [[capabilities/core-agent-capabilities|Core agent capabilities]]
- [[memory/context-and-memory|Context and memory]]
- [[strategies/retrieval-first|Retrieval first]]
- [[strategies/human-in-the-loop|Human in the loop]]
- [[strategies/narrow-agent-scope|Narrow agent scope]]
- [[strategies/agent-design-patterns|Agent design patterns]]
- [[tools/safe-tool-use|Safe tool use]]
- [[tools/qdrant|Qdrant]]
- [[tools/cognee|Cognee]]
- [[knowledge/okf-and-rag|OKF and RAG]]
- [[decisions/use-okf|Use OKF]]
- [[evaluation/agent-evaluation|Agent evaluation]]
- [[evaluation/source-grounding|Source grounding]]
- [[concepts/illusion-of-agents|The illusion of agents]]
- [[patterns/streaming-and-thinking|Streaming and thinking]]
- [[failures/agent-failure-modes|Agent failure modes]]
- [[failures/tool-overuse|Tool overuse]]
- [[failures/context-drift|Context drift]]
- [[examples/coding-agent|Coding agent example]]
- [[meta/self-describing-wiki|Self-describing wiki]]
""",
    },
    {
        "slug": "concepts/okf-wiki",
        "title": "OKF Wiki",
        "page_type": "concept",
        "description": "How Agent Rebel uses OKF pages as structured operational knowledge.",
        "tags": ["concept", "okf", "wiki"],
        "body_markdown": """# OKF Wiki

An OKF wiki is a set of structured knowledge pages with enough metadata for humans, software, and future agents to inspect.

Each page has:

- a stable slug
- a title
- a type
- a short description
- tags
- Markdown body content
- outgoing links to related pages
- backlinks from pages that depend on it

The point is not to make documents fancy. The point is to make knowledge reusable under pressure.

Agent Rebel uses OKF for agent strategy because agent advice gets dangerous when it is vague. A page should say what it is for, what can go wrong, and what related idea should be read next.

The current wiki is edited by humans. Future LLM features can propose edits, but the human remains the curator. See [[guides/wiki-workflow]].
""",
    },
    {
        "slug": "concepts/sources-wiki-schema",
        "title": "Sources, Wiki, Schema",
        "page_type": "concept",
        "description": "The three-layer architecture behind Agent Rebel.",
        "tags": ["concept", "architecture", "okf"],
        "body_markdown": """# Sources, Wiki, Schema

Agent Rebel separates knowledge into three layers.

Raw sources are evidence. They are notes, examples, decisions, transcripts, or source material. They should be preserved with minimal interpretation.

Wiki pages are working knowledge. They explain what the source material means for agent design.

Schema is discipline. It defines required fields, allowed page types, and lint rules.

The separation matters:

- do not bury raw evidence inside polished advice
- do not make every source a strategy
- do not trust a page that cannot be linted
- do not let future automation rewrite the rules silently

This is why the core workflow is [[guides/ingest-query-lint]].
""",
    },
    {
        "slug": "guides/ingest-query-lint",
        "title": "Ingest, Query, Lint",
        "page_type": "guide",
        "description": "The core workflow for maintaining and using Agent Rebel.",
        "tags": ["guide", "workflow", "operations"],
        "body_markdown": """# Ingest, Query, Lint

Agent Rebel has three core operations.

Ingest stores raw material. Do this when new evidence appears: a decision, example, failure, source note, or field observation.

Query means use the wiki while working. Read pages, follow links, check backlinks, and search before inventing an answer.

Lint checks whether the knowledge structure is still healthy. It should find missing metadata, broken links, orphan pages, and unsupported structure.

The loop:

- ingest the source
- write or update the OKF page
- link it to related pages
- query it during real work
- lint the wiki
- repair warnings while they are small

This is not an agent runtime. It is the knowledge substrate an agent runtime can later use.
""",
    },
    {
        "slug": "guides/wiki-workflow",
        "title": "Wiki Workflow",
        "page_type": "guide",
        "description": "How humans should maintain Agent Rebel pages.",
        "tags": ["guide", "editing", "workflow"],
        "body_markdown": """# Wiki Workflow

Write pages like field notes that survived review.

Good pages are short, linked, and opinionated. They explain when an idea applies and when it fails.

When editing:

- use the OKF editor
- keep the frontmatter accurate
- link related concepts with wiki links
- prefer a specific warning over a broad principle
- record recurring problems in [[meta/error-book]]
- run lint after structural changes

Do not turn the wiki into a blog. A page exists because it helps someone make or evaluate an agent design decision.

Future LLM tools may maintain drafts and links. Humans still decide what belongs.
""",
    },
    {
        "slug": "concepts/what-is-an-agent",
        "title": "What Is an Agent",
        "page_type": "concept",
        "description": "A practical distinction between an LLM call, a workflow, an assistant, and an agent.",
        "tags": ["concept", "agent-design"],
        "body_markdown": """# What Is an Agent

An AI agent is a software system that uses artificial intelligence to pursue a goal on behalf of a user.

An LLM call answers one prompt.

A workflow follows known steps.

An assistant responds to user prompts and helps the user do work.

An agent chooses the next step dynamically. It may reason, plan, observe, use tools, collaborate with humans or other agents, revise its approach, and stop when the goal is satisfied.

Useful agent capabilities include:

- reasoning: drawing conclusions from available information
- acting: taking actions through tools, files, APIs, or other systems
- observing: inspecting environment state, user context, logs, sensors, media, or code
- planning: decomposing goals into steps and updating the plan as conditions change
- collaborating: working with humans or other agents
- self-refining: learning from experience without silently corrupting the system

Use an agent when the next useful action depends on information discovered during the task.

Do not call something an agent just because it calls a model. A predictable chain is usually a [[concepts/agent-vs-workflow|workflow]].

Agents are often built on large language models. The model supplies flexible language and reasoning behavior; memory, retrieval, tools, and protocols give the system persistence and the ability to act. See [[capabilities/core-agent-capabilities]].
""",
    },
    {
        "slug": "concepts/agent-vs-workflow",
        "title": "Agent vs Workflow",
        "page_type": "concept",
        "description": "When deterministic workflows are better than agentic control.",
        "tags": ["concept", "workflow", "agent-design"],
        "body_markdown": """# Agent vs Workflow

A workflow is predictable; an agent decides the next step dynamically.

Prefer a workflow when:

- the steps are known
- the inputs are structured
- the acceptable outputs are narrow
- failure handling can be written down

Prefer an agent when:

- the task requires investigation
- the state is partly unknown
- the useful next action depends on what was found
- stopping conditions can be checked

Most production systems should mix both: deterministic workflow outside, narrow agent loop inside. See [[strategies/narrow-agent-scope]].
""",
    },
    {
        "slug": "concepts/agent-categories",
        "title": "Agent Categories",
        "page_type": "concept",
        "description": "Common ways to classify agents by interaction style, number of agents, and role.",
        "tags": ["concept", "taxonomy", "agent-design"],
        "body_markdown": """# Agent Categories

Agent categories are useful when they make design constraints visible. They are not permanent identities.

By interaction style:

- interactive agents talk directly with users and handle requests on demand
- background agents run without much direct user interaction and monitor, automate, or analyze systems

By number of agents:

- single-agent systems use one agent to pursue a defined goal
- multi-agent systems use multiple agents that collaborate, delegate, or compete

By organizational role:

- customer agents answer questions, resolve issues, and personalize service
- employee agents streamline internal work and repetitive tasks
- creative agents support ideation, drafts, campaigns, and content production
- data agents analyze structured or unstructured data while preserving factual integrity
- code agents generate, review, debug, and modify software
- security agents monitor, investigate, and respond across security workflows

Other practical roles include research agents, browser agents, support agents, and personal assistant agents.

Do not choose an agent category because it sounds advanced. Choose it because the role makes tool permissions, evaluation, and failure handling clearer. See [[strategies/narrow-agent-scope]].
""",
    },
    {
        "slug": "concepts/illusion-of-agents",
        "title": "The Illusion of Agents",
        "page_type": "concept",
        "description": "Agents are next-token generators, not minds, but streaming and visible reasoning make them feel human.",
        "tags": ["concept", "agent-design", "trust"],
        "body_markdown": """# The Illusion of Agents

An agent is not a thinking being. It is a next-token generator wrapped in a loop with tools. Its "thinking" is generated text, not introspection. It does not know what it knows.

We know the agent is not real. Yet the experience reads as human. Output streams in like someone typing. Reasoning appears step by step. The system pauses, hedges, and corrects itself the way a person might. This is enjoyable, and it makes the tool easier to work with.

The illusion is useful as long as you remember it is an illusion.

The risk is over-trust. If you treat generated confidence as genuine understanding, you inherit every failure mode worse: invented facts read as careful analysis, and a wrong plan reads as a considered one.

Honest framing is a feature. Call it generation, not cognition. Enjoy the human feel, but ground answers in evidence and verify them. The agent performs thought; it does not have it.

See [[patterns/streaming-and-thinking]] for why the performance feels human, [[concepts/what-is-an-agent]] for what an agent actually is, and [[capabilities/core-agent-capabilities]] for the mechanisms behind the appearance.

Related: [[concepts/what-is-an-agent]], [[capabilities/core-agent-capabilities]], [[patterns/streaming-and-thinking]].
""",
    },
    {
        "slug": "patterns/streaming-and-thinking",
        "title": "Streaming and Thinking",
        "page_type": "pattern",
        "description": "Token streaming, the typing effect, and visible reasoning make agents feel human, but fluency is not correctness.",
        "tags": ["pattern", "ux", "streaming", "reasoning"],
        "body_markdown": """# Streaming and Thinking

Modern agent interfaces share three UX patterns.

- token streaming: output appears progressively as it is generated, not all at once
- the typing effect: text arrives word by word, like a person typing
- visible reasoning: the model shows intermediate "thinking" before the final answer

These patterns improve perceived responsiveness. The user sees progress immediately, the wait feels shorter, and the step-by-step reasoning reads as careful work. Together they make the system feel human and build trust.

That trust is the trap. Fluency is not correctness. A smooth, confident stream of wrong tokens still reads convincing. Visible reasoning can be a plausible story told after the fact, not a faithful trace of how the answer was reached.

Practical stance:

- stream for user experience, because progressive output genuinely helps
- do not trust the vibe; a confident stream is not evidence
- ground answers in retrieved knowledge with [[strategies/retrieval-first]]
- evaluate output against sources and tests, not against how good it sounds

The performance is real and useful. Correctness is a separate question. See [[concepts/illusion-of-agents]].

Related: [[concepts/illusion-of-agents]], [[concepts/what-is-an-agent]], [[strategies/retrieval-first]].
""",
    },
    {
        "slug": "protocols/agent-protocols",
        "title": "Agent Protocols",
        "page_type": "protocol",
        "description": "How modern agents connect to tools, services, and other agents.",
        "tags": ["protocol", "tools", "interoperability"],
        "body_markdown": """# Agent Protocols

Protocols keep agent systems from becoming custom glue code around every tool and service.

Useful protocol map:

- MCP standardizes model-to-tool and model-to-data access
- ACP supports asynchronous multimodal messaging between agents and services
- A2A supports agent-to-agent discovery, delegation, tasks, messages, and artifacts
- ANP explores decentralized agent discovery and collaboration using distributed identity ideas

MCP is usually the first protocol to adopt because tool access is the first practical bottleneck. It defines resources, tools, prompts, and a client-server shape, often over JSON-RPC style transports.

A2A solves a different problem. It connects whole agents, not just models to tools. Agent cards describe capabilities and endpoints so one agent can discover and delegate to another.

Adoption roadmap:

- start with MCP for controlled tool access
- add asynchronous messaging when work outlives one request
- add agent-to-agent protocols only when real delegation is needed
- treat decentralized networks as a later concern unless discovery and distributed trust are core requirements

Protocol choice is an architecture decision. Record why the choice was made in a [[decisions/use-okf|decision record]].
""",
    },
    {
        "slug": "capabilities/core-agent-capabilities",
        "title": "Core Agent Capabilities",
        "page_type": "capability",
        "description": "The core capabilities an agent needs: reasoning, planning, memory, and tool use.",
        "tags": ["capability", "planning", "tools", "memory"],
        "body_markdown": """# Core Agent Capabilities

An agent needs capabilities beyond text generation.

Reasoning lets the system analyze situations, compare alternatives, and make context-dependent decisions.

Planning decomposes a goal into executable steps and updates the plan when conditions change. Two common loop shapes are:

- ReAct: interleave reasoning and acting
- Plan-and-Execute: create a plan first, then execute subtasks

Memory keeps useful information available beyond the current turn. Memory is only useful if it can be inspected, corrected, and forgotten. See [[memory/context-and-memory]].

Tool use lets the agent act through external functions, APIs, files, browsers, or services. Tool access needs explicit purpose, permission, validation, and stop conditions. See [[tools/safe-tool-use]].

Additional capabilities include retrieval, observation, delegation, and evaluation hooks.

The capability test is simple: if the capability cannot be observed, constrained, and evaluated, it is not ready for production use.
""",
    },
    {
        "slug": "memory/context-and-memory",
        "title": "Context and Memory",
        "page_type": "memory",
        "description": "How temporary context differs from persistent memory, and how both can fail.",
        "tags": ["memory", "context", "retrieval"],
        "body_markdown": """# Context and Memory

Context is temporary working memory. It lives in the model context window and usually disappears when the session ends.

Memory is persistent storage. It spans sessions and can be recalled, updated, corrected, or deleted.

Useful distinction:

- context holds recent instructions, conversation, source excerpts, and task state
- memory holds durable facts, decisions, examples, preferences, and learned procedures

Long context windows do not remove the need for retrieval. They still fill up, they still cost money, and important material can be lost in the middle.

Common memory types:

- short-term memory: current context window
- episodic memory: past interactions and experiences
- semantic memory: facts and structured knowledge
- procedural memory: skills, workflows, and action patterns

Memory risks:

- stale memory can poison future answers
- memory bloat retrieves irrelevant facts
- private data can leak into outputs
- uninspectable memory cannot be trusted

Use retrieval to put only relevant material into context. Use [[knowledge/stale-knowledge]] to track freshness risks.
""",
    },
    {
        "slug": "strategies/retrieval-first",
        "title": "Retrieval First",
        "page_type": "strategy",
        "description": "Retrieve relevant knowledge before answering or planning when local context matters.",
        "tags": ["strategy", "retrieval", "context"],
        "body_markdown": """# Retrieval First

Use retrieval before planning when the answer depends on project-specific knowledge.

Planning from memory is cheap and often wrong. The agent should first inspect the relevant source, page, file, ticket, or decision record.

Good retrieval asks:

- What source would settle this?
- Which prior decision constrains the answer?
- Is the current context enough?
- What related page should be read next?

Retrieval is not a license to keep searching. Stop when the evidence is enough to act. See [[failures/tool-overuse]] and [[evaluation/source-grounding]].
""",
    },
    {
        "slug": "strategies/human-in-the-loop",
        "title": "Human in the Loop",
        "page_type": "strategy",
        "description": "When the system should ask for confirmation instead of acting alone.",
        "tags": ["strategy", "safety", "confirmation"],
        "body_markdown": """# Human in the Loop

Ask for confirmation when an action is destructive, expensive, externally visible, legally sensitive, or hard to reverse.

Do not ask for confirmation just because the system is uncertain. First inspect the relevant context. Ask only when the decision belongs to the user.

Required confirmation examples:

- deleting data
- pushing to production
- sending messages as the user
- changing billing or permissions
- replacing trusted source material

Tool rules belong in [[tools/safe-tool-use]].
""",
    },
    {
        "slug": "strategies/narrow-agent-scope",
        "title": "Narrow Agent Scope",
        "page_type": "strategy",
        "description": "Small agents are easier to trust, evaluate, and stop.",
        "tags": ["strategy", "scope", "evaluation"],
        "body_markdown": """# Narrow Agent Scope

Small agents are easier to trust and evaluate.

Give an agent one job, a clear input, allowed tools, forbidden actions, and a stop condition.

Avoid agents with broad authority like "fix the project" or "manage all knowledge." Prefer scoped jobs:

- lint the wiki
- summarize one source
- propose links for one page
- inspect a failing test
- draft a decision record

The wider the scope, the more important [[strategies/human-in-the-loop]] becomes.
""",
    },
    {
        "slug": "strategies/agent-design-patterns",
        "title": "Agent Design Patterns",
        "page_type": "pattern",
        "description": "Practical patterns for safer, more predictable agent behavior.",
        "tags": ["pattern", "strategy", "agent-design"],
        "body_markdown": """# Agent Design Patterns

Patterns are useful only when they reduce failure.

Retrieval-first means fetch relevant knowledge before answering or planning. Use it when the answer depends on project-specific or changing information. See [[strategies/retrieval-first]].

Plan-and-Execute means draft a plan before taking action. Use it when the task is long, costly, or easy to interrupt badly.

ReAct means alternate reasoning and acting. Use it when each observation changes the next useful step.

Human-in-the-loop means ask the user to decide before high-impact actions. Use it for destructive, expensive, external, legal, or hard-to-reverse actions. See [[strategies/human-in-the-loop]].

Narrow scope means give the agent a small job, limited tools, and clear stop conditions. See [[strategies/narrow-agent-scope]].

Fail-safe action means define what the agent should do when a tool fails, evidence is missing, or output validation fails.

Keep pages small means split knowledge into linked OKF pages. Large pages harm retrieval and make stale claims harder to find.
""",
    },
    {
        "slug": "tools/safe-tool-use",
        "title": "Safe Tool Use",
        "page_type": "tool",
        "description": "Rules for using tools without drifting, looping, or causing avoidable harm.",
        "tags": ["tools", "safety", "operations"],
        "body_markdown": """# Safe Tool Use

Inspect before changing.

Ask or stop before destructive actions.

Do not call tools without purpose.

Summarize what changed.

A tool call should have a reason tied to the user goal. Repeated tool use without a new question is often [[failures/tool-overuse]].

Before using a write tool, know:

- what will change
- how to verify it
- how to recover if it fails
- whether user confirmation is required
""",
    },
    {
        "slug": "tools/qdrant",
        "title": "Qdrant",
        "page_type": "tool",
        "description": "An open-source vector similarity database for retrieval, and when a small wiki does not need it yet.",
        "tags": ["tool", "vector-db", "rag", "retrieval"],
        "body_markdown": """# Qdrant

Qdrant is an open-source vector similarity database.

It stores embeddings: numeric vectors that represent the meaning of text, images, or other data. A model turns content into a vector, and similar content lands near other similar content in vector space.

Vector search works by nearest-neighbor lookup. You embed the query, then ask the database for the stored vectors closest to it. This finds records by meaning, not by exact keywords.

In a RAG pipeline, a vector database is the retrieval layer. It returns the most relevant chunks so the model can generate an answer grounded in evidence. See [[knowledge/okf-and-rag]].

When a small curated wiki does not need it yet:

- few pages mean keyword and SQL search already find the right records
- a vector database adds operational weight: indexing, embeddings, and a service to run
- curated OKF pages are short and well-tagged, which suits simple search

Treat Qdrant as a later-stage tool. Adopt it when curated knowledge outgrows keyword and SQL search, and retrieval quality clearly suffers without semantic matching. Agent Rebel deliberately does not start here.

Related: [[knowledge/okf-and-rag]], [[strategies/retrieval-first]], [[decisions/use-okf]].
""",
    },
    {
        "slug": "tools/cognee",
        "title": "Cognee",
        "page_type": "tool",
        "description": "A framework that gives agents persistent memory by building a knowledge graph and vector layer from their data.",
        "tags": ["tool", "memory", "knowledge-graph", "agent-memory"],
        "body_markdown": """# Cognee

Cognee is a framework that gives agents persistent memory.

It turns raw data into a knowledge graph plus a vector layer, so an agent can recall facts and relationships across sessions rather than starting empty each time.

Cognee describes this as an ECL pipeline:

- extract: pull data from documents, conversations, and other sources
- cognify: build a knowledge graph and embeddings that link entities and meaning
- load: store the result so the agent can query it later

The graph captures how things relate; the vector layer supports retrieval by meaning. Together they let an agent answer questions using memory it built earlier.

This connects to [[memory/context-and-memory]]: temporary context lives only within a session, while persistent memory survives across sessions. Cognee is one way to provide that persistent layer.

The same caution as with a vector database applies. Persistent memory adds storage, indexing, and maintenance. Adopt it when memory needs outgrow simple stores, not before. A small curated wiki may not need a knowledge-graph memory system yet.

Related: [[memory/context-and-memory]], [[knowledge/okf-and-rag]], [[tools/qdrant]].
""",
    },
    {
        "slug": "knowledge/stale-knowledge",
        "title": "Stale Knowledge",
        "page_type": "failure-mode",
        "description": "Old or wrong knowledge can make agents confidently wrong.",
        "tags": ["knowledge", "freshness", "failure-mode"],
        "body_markdown": """# Stale Knowledge

Old knowledge can be worse than missing knowledge because it feels authoritative.

Memory is only useful if it can be inspected, corrected, and forgotten.

Watch for:

- decisions that no longer match the system
- source pages without dates
- examples copied from obsolete code
- rules that conflict with newer rules

When freshness matters, retrieve current sources before answering. See [[strategies/retrieval-first]].
""",
    },
    {
        "slug": "knowledge/okf-and-rag",
        "title": "OKF and RAG",
        "page_type": "concept",
        "description": "How OKF pages support retrieval-augmented generation and cited answers.",
        "tags": ["knowledge", "okf", "rag", "retrieval"],
        "body_markdown": """# OKF and RAG

OKF is a practical format for knowledge that humans and agents can both read.

An OKF page has frontmatter, Markdown body content, and links to related pages. The frontmatter makes the page easy to validate, index, filter, and cite.

RAG means retrieval-augmented generation. The system retrieves relevant records before producing an answer.

Good RAG over OKF should:

- search title, description, tags, and body text
- prefer small focused pages over giant documents
- include source pages or wiki pages as citations
- separate retrieved evidence from model inference
- warn when retrieved evidence is weak

Decision records are especially useful in RAG because they explain why a design choice was made. Agents should not undo past decisions just because a generic pattern sounds better.

Agent Rebel should add `/ask` only as a read-only query over current OKF knowledge first. Generation can come later after retrieval, citations, and evaluation are reliable.
""",
    },
    {
        "slug": "decisions/use-okf",
        "title": "Use OKF",
        "page_type": "decision",
        "description": "Why Agent Rebel stores knowledge as structured OKF pages.",
        "tags": ["decision", "okf", "architecture"],
        "body_markdown": """# Use OKF

Decision: Agent Rebel stores working knowledge as OKF pages.

Reasons:

- plain text is readable by humans
- frontmatter is readable by software and future agents
- Markdown keeps examples and explanations easy to edit
- stable slugs make links, backlinks, and citations reliable
- small pages work well with search and RAG
- the format can be rendered, linted, exported, and versioned

SQLite is the MVP storage layer. OKF is still the knowledge format: pages are edited and validated as OKF documents even when stored in the database.

Rejected alternative: store only free-form Markdown. It is simpler at first, but weak metadata makes search, graph views, citations, and validation worse.

Rejected alternative: start with a vector database. It adds operational weight before the wiki has enough curated knowledge to justify it.

Related: [[knowledge/okf-and-rag]] and [[concepts/sources-wiki-schema]].
""",
    },
    {
        "slug": "evaluation/agent-evaluation",
        "title": "Agent Evaluation",
        "page_type": "evaluation",
        "description": "Metrics and methods for evaluating agent behavior beyond simple answer accuracy.",
        "tags": ["evaluation", "metrics", "testing"],
        "body_markdown": """# Agent Evaluation

Agent evaluation needs more than answer accuracy.

Measure task performance:

- task completion rate
- answer accuracy
- success rate under realistic constraints

Measure trajectory quality:

- whether the agent followed required steps
- whether actions were efficient
- whether tool calls were necessary
- whether the agent stopped at the right time

Measure tool calling:

- correct tool selection
- valid parameters
- successful execution
- avoidance of redundant calls

Measure safety and compliance:

- harmful output avoidance
- instruction adherence
- private data protection
- regulatory or policy constraints

Measure efficiency:

- latency
- cost
- token usage
- number of iterations

Evaluation methods include human review, benchmark tasks, regression tests, LLM-as-judge scoring, A/B tests, and telemetry review.

Observability matters because failures often appear as traces: hallucination cascades, tool misfires, infinite loops, latency spikes, and context drift. See [[failures/agent-failure-modes]].
""",
    },
    {
        "slug": "evaluation/source-grounding",
        "title": "Source Grounding",
        "page_type": "evaluation",
        "description": "Answers should be grounded in visible source pages where possible.",
        "tags": ["evaluation", "grounding", "sources"],
        "body_markdown": """# Source Grounding

Answers should be grounded in visible source pages where possible.

A grounded answer says where its important claims came from. It does not hide behind vague phrases like "best practices say."

Good grounding:

- points to the page or source used
- separates evidence from inference
- warns when evidence is missing
- avoids citing pages that do not support the claim

Broken grounding is a knowledge failure. Record repeated cases in [[meta/error-book]].
""",
    },
    {
        "slug": "failures/agent-failure-modes",
        "title": "Agent Failure Modes",
        "page_type": "failure-mode",
        "description": "Common ways agentic systems fail and how to debug them.",
        "tags": ["failure-mode", "debugging", "safety"],
        "body_markdown": """# Agent Failure Modes

Failure modes should be named so they can be detected, tested, and repaired.

Hallucination cascade happens when the model invents facts and later steps amplify the error. Missing retrieval and unsupported assumptions are common triggers.

Tool invocation misfires happen when an agent chooses the wrong tool or sends ambiguous parameters.

Context window truncation happens when long histories or verbose prompts push critical instructions out of context.

Planner infinite loops happen when success criteria are missing or ambiguous.

Data leakage and PII exposure happen when retrieval, prompts, or outputs expose sensitive information.

Non-deterministic output drift happens when the same input produces inconsistent output because of sampling, prompt changes, or model updates.

Memory bloat and state drift happen when long-term memory grows without inspection, correction, or deletion.

Latency spikes and resource starvation happen when planning, tool chains, or retrieval become too expensive.

Context drift happens when the agent optimizes for recent intermediate work instead of the original user goal. See [[failures/context-drift]].

Debugging requires traces, schema checks, cost and latency limits, explicit end conditions, and grounded source review. See [[evaluation/agent-evaluation]].
""",
    },
    {
        "slug": "failures/tool-overuse",
        "title": "Tool Overuse",
        "page_type": "failure-mode",
        "description": "The agent keeps using tools instead of answering or stopping.",
        "tags": ["failure-mode", "tools", "stop-condition"],
        "body_markdown": """# Tool Overuse

Tool overuse happens when an agent keeps inspecting, searching, or editing without a clear stop condition.

Symptoms:

- the same source is inspected repeatedly
- new tool calls do not answer a new question
- the agent delays a straightforward answer
- the user goal disappears behind process

Prevention:

- state the purpose before using a tool
- stop when enough evidence exists
- answer with known uncertainty
- ask the user only when the decision is actually theirs

Related: [[tools/safe-tool-use]] and [[failures/context-drift]].
""",
    },
    {
        "slug": "failures/context-drift",
        "title": "Context Drift",
        "page_type": "failure-mode",
        "description": "How agents lose the original user goal during long tasks.",
        "tags": ["failure-mode", "context", "goals"],
        "body_markdown": """# Context Drift

Context drift happens when the agent optimizes for the recent conversation instead of the original goal.

Common causes:

- long tool sessions
- too many intermediate findings
- unclear success criteria
- untracked user corrections

Countermeasures:

- restate the active goal before major work
- keep operation logs short and factual
- use [[strategies/narrow-agent-scope]]
- stop and answer when the task is handled
""",
    },
    {
        "slug": "examples/coding-agent",
        "title": "Coding Agent Example",
        "page_type": "example",
        "description": "How a coding agent should use the wiki before modifying code.",
        "tags": ["example", "coding-agent", "tools"],
        "body_markdown": """# Coding Agent Example

A coding agent should use the wiki before modifying code when the change touches agent behavior, tool use, memory, retrieval, or evaluation.

Useful sequence:

- read the relevant strategy page
- inspect the actual code
- state the smallest safe change
- edit only what is needed
- verify with tests
- summarize what changed

If the task depends on project-specific facts, use [[strategies/retrieval-first]].

If the task may delete, publish, migrate, or overwrite data, use [[strategies/human-in-the-loop]].
""",
    },
    {
        "slug": "meta/self-describing-wiki",
        "title": "Self-Describing Wiki",
        "page_type": "meta",
        "description": "Agent Rebel is both a knowledge base and a description of the LLM-as-wiki idea it is built on.",
        "tags": ["meta", "okf", "knowledge", "architecture"],
        "body_markdown": """# Self-Describing Wiki

This wiki describes its own idea. It is a knowledge base about agents, and at the same time documentation of what an LLM-wiki is and why it should exist.

The parts connect in one chain:

- raw sources hold evidence and notes
- OKF pages turn that material into structured, reusable knowledge
- schema and lint rules keep the knowledge inspectable
- humans curate, so humans own the truth
- wikilinks join pages into a navigable graph
- LLM tools can maintain pages, but they do not own the truth

The OKF page is a plain YAML front matter block followed by Markdown, the same lineage as static-site front matter that Google and other publishers describe for structured content. That choice is deliberate: front matter is typed and machine-readable, while the body stays easy for a person to write and edit.

Andrej Karpathy framed the underlying intuition: a large language model is a lossy, compressed store of the internet, useful but frozen and hard to inspect. A wiki is the complement. Its knowledge is up to date, curated, inspectable, and editable, and it does not silently go stale the way model weights do. See [[knowledge/stale-knowledge]].

So the advantage is structural. Knowledge here is readable, browsable, editable, linkable, versioned, and lintable. None of those hold for free-form notes with weak metadata, and none hold for what a model happens to have memorized.

Related: [[concepts/okf-wiki]], [[concepts/sources-wiki-schema]], [[knowledge/stale-knowledge]], [[knowledge/okf-and-rag]], [[decisions/use-okf]].
""",
    },
    {
        "slug": "meta/error-book",
        "title": "Error Book",
        "page_type": "meta",
        "description": "A place to record repeated knowledge and agent behavior errors.",
        "tags": ["meta", "lint", "quality"],
        "body_markdown": """# Error Book

Record repeated knowledge problems here.

Examples:

- stale claims
- missing source pages
- unsupported recommendations
- broken concepts
- contradictory strategy pages
- agent behavior that keeps failing

The error book is not blame. It is a repair queue for the knowledge system.
""",
    },
    {
        "slug": "log",
        "title": "Operation Log",
        "page_type": "log",
        "description": "Human-readable mirror of structured wiki operations.",
        "tags": ["log", "operations"],
        "body_markdown": """# Operation Log

The database stores the parseable operation log.

Use the Log view to inspect edits, ingests, and lint runs.
""",
    },
]


def seed_if_empty(conn) -> None:
    existing = conn.execute("SELECT COUNT(*) AS count FROM pages").fetchone()["count"]
    if existing:
        return
    for page in SEED_PAGES:
        save_page(conn, change_summary="Seeded Agent Rebel sample page.", actor="system", **page)
    rebuild_all_links(conn)
    lint_all(conn)
    conn.commit()
