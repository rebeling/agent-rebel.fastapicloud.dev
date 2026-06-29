from app.lint import lint_all
from app.repository import rebuild_all_links, save_page


SEED_PAGES = [
    {
        "slug": "index",
        "title": "Agent Rebel",
        "page_type": "catalog",
        "description": "Strategy, knowledge, and failure modes for AI agents.",
        "tags": ["catalog", "agent-strategy"],
        "body_markdown": """# Agent Rebel

Agent Rebel is a writable OKF wiki for agent strategy and agent knowledge.

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
- [[strategies/retrieval-first|Retrieval first]]
- [[strategies/human-in-the-loop|Human in the loop]]
- [[strategies/narrow-agent-scope|Narrow agent scope]]
- [[tools/safe-tool-use|Safe tool use]]
- [[evaluation/source-grounding|Source grounding]]
- [[failures/tool-overuse|Tool overuse]]
- [[failures/context-drift|Context drift]]
- [[examples/coding-agent|Coding agent example]]
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
        "description": "A practical distinction between an LLM call, a workflow, and an agent.",
        "tags": ["concept", "agent-design"],
        "body_markdown": """# What Is an Agent

An LLM call answers one prompt.

A workflow follows known steps.

An agent chooses the next step dynamically. It may inspect state, use tools, revise a plan, or stop when the goal is satisfied.

Use an agent when the next useful action depends on information discovered during the task.

Do not call something an agent just because it calls a model. A predictable chain is usually a [[concepts/agent-vs-workflow|workflow]].
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
