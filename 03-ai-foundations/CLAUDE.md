# AI Foundations (Light) — Progression Tracker

## Overview

Light pass on AI/LLM concepts. Goal is conceptual understanding and a basic working POC, NOT production-grade implementation. The deep dive happens in Section 5 after system design and backend knowledge are solid.

**Prior Knowledge:** Johnathan has already completed LLM integration patterns (streaming, cost control, prompt lifecycle, full request lifecycle). This section picks up from there.

## Definition of Done

Can explain RAG architecture end-to-end, describe chunking trade-offs with specific examples, articulate when vector search fails and what alternatives exist. Has a working basic RAG proof-of-concept.

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
