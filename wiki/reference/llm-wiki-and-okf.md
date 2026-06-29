---
title: LLM Wiki and OKF
type: concept
section: Reference
section_title: Reference
section_order: 4
nav_order: 1
description: How Karpathy's LLM Wiki pattern and the Open Knowledge Format fit The Agent Wiki.
tags: [llm-wiki, okf, karpathy, markdown, human-agent-loop, knowledge-format]
status: starter
---

# LLM Wiki and OKF

The Agent Wiki is not only a wiki about agents. It is also a small experiment in the **LLM Wiki** pattern.

The idea is simple:

```text
raw sources -> structured wiki pages -> retrieval, answers, and updates
```

Normal RAG retrieves raw chunks at question time. That can work, but the system often has to rediscover and reassemble the same knowledge again and again.

An LLM Wiki adds a maintained wiki layer between raw sources and answers. The LLM does not only answer questions. It helps update the knowledge base: it improves pages, adds links, notes contradictions, and proposes new pages when something important is missing.

## The three parts

### 1. Raw sources

Raw sources are the original material.

Examples:

- articles
- papers
- docs
- transcripts
- notes
- exported chats
- screenshots
- source code

Raw sources should be preserved as evidence. They can be summarized, cited, and linked, but they should not be silently rewritten.

### 2. Wiki layer

The wiki is the maintained synthesis layer.

It contains:

- concepts
- comparisons
- summaries
- strategies
- decisions
- examples
- failure modes
- source notes

This is where knowledge becomes easier to reuse. A good wiki page is smaller and more deliberate than raw source material. It has a title, metadata, links, and references.

### 3. Schema and rules

The schema tells humans and agents how the wiki should be maintained.

It can define:

- folder structure
- page types
- frontmatter fields
- link rules
- citation rules
- ingest workflow
- query workflow
- lint workflow
- review rules

For this project, these rules can later live in a file like:

```text
AGENTS.md
```

or:

```text
wiki-schema.md
```

The schema is what turns a generic chatbot into a disciplined wiki maintainer.

## What OKF adds

**OKF**, the Open Knowledge Format, gives the LLM Wiki idea a simple file format.

For this starter, OKF means:

```text
Markdown files + YAML frontmatter + links + references
```

That is enough to make the same knowledge usable by both humans and agents.

Humans can:

- read pages in a browser
- edit Markdown
- review changes in Git
- follow links
- check references

Agents can:

- parse metadata
- retrieve relevant pages
- follow links
- cite sources
- propose edits
- validate page structure

The important part is not the format itself. The important part is that the knowledge stays **visible, versionable, and editable**.

## Why this is different from chat

A chat answer is useful once.

A wiki page can be improved and reused.

```text
chat answer -> disappears into history
wiki page   -> becomes durable knowledge
```

The goal is not to replace the wiki with chat. The goal is to make chat improve the wiki.

When a user asks a good question, the answer should not only solve the moment. It should reveal whether the wiki is missing something.

## The loop

The future loop should look like this:

```text
ask -> retrieve pages -> answer with sources -> propose update -> improve wiki
```

A useful question can create one of three outcomes:

1. The wiki already has enough knowledge, so the agent answers with references.
2. The wiki is missing knowledge, so the agent proposes a new page.
3. The wiki has weak or stale knowledge, so the agent proposes a page update.

That is how the wiki compounds.

## How to iterate

Start manually.

Do not begin with a vector database, graph database, or autonomous editor.

### Stage 1: Human-readable wiki

The app renders a small Markdown wiki.

Success means a human can browse it and understand the topic without any LLM feature.

### Stage 2: Structured pages

Add consistent frontmatter and page types.

The wiki should know what each page is:

- concept
- strategy
- protocol
- memory
- evaluation
- failure-mode
- example
- source

### Stage 3: Source catalog

Keep a short source catalog.

Each source should explain:

- what it is
- why it matters
- which pages use it

### Stage 4: Assisted ingest

The agent reads one new source and proposes a diff.

It should not silently rewrite the wiki.

Good ingest should update existing pages, not only create summaries.

### Stage 5: Ask the wiki

Add a query endpoint.

The agent should:

1. select relevant pages
2. answer from those pages
3. show the pages used
4. suggest missing or outdated pages

### Stage 6: Save useful answers

Add a workflow like:

```text
Save this as a page
```

or:

```text
Propose update to existing page
```

This is where chat becomes durable knowledge.

## Human and agent roles

The human should decide what matters.

Humans are good at:

- choosing sources
- judging importance
- correcting weak synthesis
- deciding what should be trusted
- approving larger changes

The agent should reduce maintenance work.

Agents are good at:

- drafting summaries
- finding related pages
- detecting broken links
- proposing page updates
- comparing sources
- keeping references current
- finding missing concepts

The best version is not human-only and not agent-only.

The best version is shared work on the same visible knowledge.

## What to avoid

Avoid building a large low-quality wiki.

Do not start with:

- 100 weak generated pages
- hidden agent memory humans cannot inspect
- a graph database before links matter
- a vector database before the pages are useful
- silent autonomous edits
- source summaries without synthesis

A small wiki with strong pages is better than a large wiki full of filler.

## For The Agent Wiki

The Agent Wiki starts as a compact manual about agents.

Later, it can become an LLM-maintained wiki about agents.

That means:

- raw sources stay separate
- wiki pages become the maintained synthesis
- humans can edit the same knowledge the agent uses
- agents can propose improvements instead of hiding memory
- answers can become page updates

## Related pages

- [[design/agent-memory]]
- [[design/retrieval-and-grounding]]
- [[design/protocols-and-tool-access]]
- [[operate/evaluation]]
- [[reference/sources]]

## References

- Andrej Karpathy, “LLM Wiki”: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Google Cloud, “Introducing the Open Knowledge Format”: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
- Weaviate, “Context Engineering”: https://weaviate.io/blog/context-engineering
