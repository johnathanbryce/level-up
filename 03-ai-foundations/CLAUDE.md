# AI Foundations (Light) — Progression Tracker

## Overview

Light pass on AI/LLM concepts. Goal is conceptual understanding and a basic working POC, NOT production-grade implementation. The deep dive happens in Section 5 after system design and backend knowledge are solid.

**Prior Knowledge:** Johnathan has already completed LLM integration patterns (streaming, cost control, prompt lifecycle, full request lifecycle). This section picks up from there.

## Definition of Done

Can explain RAG architecture end-to-end, describe chunking trade-offs with specific examples, articulate when vector search fails and what alternatives exist. Has a working basic RAG proof-of-concept.

---

## Section Operating Model

Locked in 2026-05-17 before the first chunk of real material. Future-Claude in a fresh window should read this section first to understand how this section is taught and where artifacts live.

### Folder map

```
03-ai-foundations/
├── CLAUDE.md
├── notes/          numbered .md files per sub-topic group (one file per group)
│                   01-embeddings-and-vector-concepts.md, 02-rag-architecture.md, 03-search-and-retrieval-concepts.md
│                   (files created lazily — only when John starts taking notes on that group)
├── experiments/    micro-scripts (~10-15 min each) that ride inside conceptual chunks to make abstract ideas concrete
│                   examples: embeddings_demo.py, cosine_similarity.py, chunking_demo.py
└── rag-poc/        capstone hands-on project (FastAPI + embeddings + vector store + LLM call)
                    populated only when sub-topic group 4 starts
```

### Notes-file pattern

Identical to System Design. Within each `notes/NN-*.md` file:
- `#` file title only
- `##` major sections (one per CLAUDE.md sub-bullet group)
- `###` sub-sections
- `**bold**` reserved for vocabulary/emphasis only — NEVER as a section marker

End-of-session heading audit (per project CLAUDE.md) applies.

### Teaching cadence

| Granularity | What happens |
|---|---|
| **Chunk** (5-10 min) | Teach one concept → one quick applied check question → confirm landed → next chunk. No formal quiz at this granularity. |
| **Sub-topic group** | "Now apply it" beat — applied scenario, diagram, or 2-3 question check before marking the group done. Per Daily Session Structure rule. |
| **Pre-POC gate** (after groups 1-3) | End-of-section warm-down quiz, 5-7 mixed-format questions across embeddings + RAG + search/retrieval. Mandatory gate before starting the POC build. |
| **Capstone** | POC Demo + Verbal Walkthrough — already defined further down this file. Section close gate. |

### Hands-on mix per sub-topic group

| Group | Mix | Specific hands-on |
|---|---|---|
| 1. Embeddings & Vector Concepts | Concept-heavy + 2 micro scripts | `embeddings_demo.py`, `cosine_similarity.py` |
| 2. RAG Architecture | Concept-heavy + diagram + 1 micro script | Pipeline flow diagram (ingest → chunk → embed → store → retrieve → generate); `chunking_demo.py` |
| 3. Search & Retrieval Concepts | Concept-only by default | Optional `bm25_vs_vector.py` if BM25 vs embeddings confusion lingers (flagged 2026-04-21, 2026-05-14) |
| 4. Hands-On: Basic RAG POC | Pure hands-on build under `rag-poc/` | Full pipeline — see Sub-Topics below |

Micro-scripts: Claude scaffolds the boilerplate, John writes the meaningful lines. Same rule as algos.

### Granularity guide — how deep to go on AI topics

Locked in 2026-05-17 in response to John's "how granular do I need to go?" question during chunk 2. Use as the rubric for any sub-topic in this section.

| Tier | Meaning | Examples |
|---|---|---|
| **1 — Must know cold** | Interview-death-blow level. Cannot fumble. | What an embedding IS; why semantic search beats keyword for freeform queries; general RAG pipeline shape (ingest → chunk → embed → store → retrieve → generate); that chunking is necessary |
| **2 — Should reason about it** | Mid-level differentiator. Explain + justify trade-offs, don't memorize. | Cosine similarity (roughly why); chunking trade-offs (small vs large); API mechanics (tokens, batching, rate limits); different models → incompatible vectors |
| **3 — Senior / nice-to-have** | Look up when needed; do NOT memorize. | Specific dimensions per model (1536, 1024); specific token limits (8191); cost per 1M tokens; vector DB choice rationale; HNSW / ANN index internals; re-ranking strategies |
| **4 — Specialized only** | Not required for general AI engineering. | Transformer internals (attention math, layer norm); training your own embedding model; embedding fine-tuning |

**Rule of thumb:** if John can articulate Tier 1 + reason about Tier 2 trade-offs, that's mid-level competency for this section. Tier 3 specifics can be Googled when actually needed — don't burn cycles memorizing tier-3 numbers, burn them on locking Tier 1-2 mental models.

**When teaching:** flag concepts by tier as they come up ("this is a Tier 3 detail — know it exists, look it up"). When John pushes back on density, default to: keep Tier 1-2 in notes, mention Tier 3 in passing, skip Tier 4 entirely.

---

## Sub-Topics

### Embeddings & Vector Concepts

- [ ] What embeddings are — text as numerical vectors, semantic similarity
- [ ] How embedding models work (high level — not transformer internals)
- [ ] Cosine similarity and distance metrics
- [ ] Dimensionality and its impact on performance/quality
- [ ] Common embedding models and their trade-offs (OpenAI, Cohere, open-source)

### RAG Architecture

- [ ] End-to-end RAG pipeline: ingest → chunk → embed → store → retrieve → generate
- [ ] Chunking strategies: fixed-size, semantic, recursive, overlap
- [ ] Chunking trade-offs: small chunks (precise, less context) vs large (more context, noisier)
- [ ] Retrieval: top-K selection, similarity thresholds, re-ranking
- [ ] Citation and grounding — how to attribute answers to source documents
- [ ] Hallucination risks and mitigation strategies

### Search & Retrieval Concepts

- [ ] Vector search: approximate nearest neighbors (ANN), HNSW index
- [ ] Keyword search: BM25, TF-IDF (conceptual understanding)
- [ ] Hybrid search: combining vector + keyword, why it outperforms either alone
- [ ] When vector search fails (out-of-domain queries, exact match needs, sparse data)
- [ ] Retrieval evaluation: precision, recall, relevance scoring

### Hands-On: Basic RAG POC

- [ ] Set up a simple Python project with FastAPI
- [ ] Implement document ingestion and chunking
- [ ] Generate and store embeddings (pgvector or in-memory for POC)
- [ ] Implement basic retrieval (vector similarity search)
- [ ] Connect to an LLM for answer generation
- [ ] Test with sample documents and queries

---

## End-of-Section Capstone

This section is lighter than System Design — the RAG POC is the primary proof of understanding. The capstone adds one verbal layer to confirm the concepts are internalized, not just implemented by following a tutorial.

### POC Demo + Verbal Walkthrough (20-30 min)
John runs the working RAG POC and explains the full pipeline end-to-end (ingest → chunk → embed → store → retrieve → generate) as if onboarding a junior engineer — no notes. Claude then asks 4-5 targeted follow-up questions, for example:
- "Why this chunk size? What would break if you doubled it?"
- "Your vector search returned a bad answer for an exact-match query. Walk me through how you'd debug it."
- "When would this POC fail at scale? What's the first thing you'd change?"
- "What's the difference between your vector search and what Elasticsearch does?"
- "How would you evaluate whether this RAG system is actually giving good answers?"

**Pass criteria:** POC works end-to-end, pipeline explained clearly without notes, 3/5 follow-up questions answered with specific reasoning (not vague gestures). Section closes when this passes. Log result in Session Log below.

**Capstone result:** NOT YET RUN

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)

---

## Bridge to Section 5

When this section is complete, Johnathan will have conceptual understanding and a basic POC. Section 5 (AI Production) revisits all of this with system design knowledge: caching embeddings, scaling retrieval, hybrid search implementation, evaluation pipelines, cost optimization, and production failure handling.
