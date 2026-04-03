# AI Production (Deep Dive) — Progression Tracker

## Overview

The second pass on AI systems, now with system design and backend knowledge. Rebuild the RAG pipeline from Section 3 into a production-grade system. This is where AI knowledge meets engineering judgment.

**Prerequisites:** Sections 2 (System Design), 3 (AI Foundations), and 4 (Backend) should be complete before starting this section.

## Definition of Done

Can design a cost-aware, production-ready RAG system from scratch with caching, monitoring, failure handling, and evaluation. Can explain trade-offs between pgvector and dedicated vector databases. Can articulate cost optimization strategies and quality evaluation approaches.

---

## Sub-Topics

### Production RAG Pipeline

- [ ] Rebuild ingestion pipeline with proper error handling and retry logic
- [ ] Implement chunking with multiple strategies, benchmark quality differences
- [ ] Embedding generation with batching and error handling
- [ ] pgvector setup, indexing (HNSW), and query optimization
- [ ] Implement caching layer: cache frequent queries, cache embeddings
- [ ] Retrieval with re-ranking (cross-encoder or LLM-based)

### Hybrid Search Implementation

- [ ] Implement BM25 keyword search alongside vector search
- [ ] Score fusion strategies (Reciprocal Rank Fusion, weighted combination)
- [ ] Compare: vector-only vs keyword-only vs hybrid — measure quality differences
- [ ] Handle edge cases: exact match queries, out-of-domain queries

### Vector Database Trade-offs

- [ ] pgvector: capabilities, limitations, indexing options (IVFFlat vs HNSW)
- [ ] When pgvector is enough (most startup use cases)
- [ ] When dedicated vector DBs make sense (Pinecone, Weaviate, Qdrant)
- [ ] Scaling considerations: millions of vectors, dimensionality impact
- [ ] Cost comparison: managed vector DB vs pgvector on existing Postgres

### Quality & Evaluation

- [ ] Retrieval evaluation: precision@K, recall@K, MRR
- [ ] Answer quality evaluation: faithfulness, relevance, completeness
- [ ] Build a simple evaluation pipeline (test queries → expected results → measure)
- [ ] Hallucination detection strategies
- [ ] Human-in-the-loop feedback patterns

### Cost Optimization

- [ ] Token usage tracking and optimization
- [ ] Embedding caching (avoid re-embedding identical content)
- [ ] Query caching (identical/similar queries return cached results)
- [ ] Model routing: cheaper models for simple queries, expensive for complex
- [ ] Chunking impact on cost (fewer chunks = fewer embedding calls)

### Production Concerns

- [ ] Monitoring: track retrieval quality, latency, cost per query
- [ ] Failure modes: what happens when embedding service is down, DB is slow, LLM times out
- [ ] Graceful degradation: fallback to keyword search if vector search fails
- [ ] Document freshness: handling updates and deletions in the index
- [ ] Multi-tenancy considerations (if relevant)

### Prompt Engineering for RAG

- [ ] System prompts for RAG: grounding instructions, citation requirements
- [ ] Few-shot examples for consistent output formatting
- [ ] Handling "I don't know" — when the context doesn't contain the answer
- [ ] Temperature and parameter tuning for different use cases

---

## Project: Production RAG System

**Description:** Full rebuild of Section 3's POC as a production-grade system. FastAPI backend, pgvector, Redis caching, hybrid search, evaluation pipeline.
**Status:** NOT STARTED
**Notes:**

---

## Session Log

| Date | Topics Covered | Assessment | Next Focus |
|------|---------------|------------|------------|
| — | — | — | — |

---

## Notes & Weak Spots

- (none yet)
