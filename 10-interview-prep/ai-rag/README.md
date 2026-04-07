# AI / RAG Interview Questions

Curated questions specifically for the AI engineer angle. Mix of conceptual ("explain X"), design ("how would you build Y"), and trade-off ("when do you choose A over B"). These are pulled from the kinds of questions asked at startups hiring AI engineers in 2025-2026.

**Use these AFTER Section 3 (AI Foundations) is mostly complete.** Section 5 (AI Production) is where most of these become genuinely answerable.

---

## Tier 1 — Conceptual fluency

### 1. Explain RAG end-to-end
Walk through ingest → chunk → embed → store → retrieve → rerank → generate. For each step, name one common failure mode.
- **Discuss:** Where most RAG systems actually fail (hint: retrieval quality, not the LLM).

### 2. Chunking strategy trade-offs
You're chunking technical documentation. Compare fixed-size, semantic, and recursive chunking. Which would you pick and why?
- **Discuss:** Chunk size vs context window vs retrieval precision. Why overlap matters. When to enrich chunks with metadata.

### 3. When does vector search fail?
Give three concrete scenarios where pure vector search produces bad results, and what you'd do about each.
- **Discuss:** Out-of-domain queries, exact match needs (product SKUs, names), sparse data, ambiguous queries. How hybrid search helps.

### 4. Hybrid search: vector + BM25
Why does hybrid search outperform either alone? Walk through Reciprocal Rank Fusion conceptually.
- **Discuss:** When BM25 wins. When vector wins. How to weight them.

---

## Tier 2 — Architecture & design

### 5. Design a RAG pipeline for 1M documents
Cover ingest, embed, store, query. Specifically address: how often you re-embed, how you handle updates/deletes, what happens when an embedding model is upgraded.
- **Discuss:** pgvector vs dedicated vector DB at this scale. HNSW vs IVFFlat. Cost.

### 6. Build a cost-aware LLM routing layer
Cheap model for simple queries, expensive model for complex. How do you decide which model gets a query?
- **Discuss:** Classifier vs heuristics. When the routing decision itself becomes expensive. Fallback patterns.

### 7. Prevent hallucinations in a customer support bot
Specifically: when the retrieved context doesn't contain the answer, the bot should say "I don't know" rather than guess.
- **Discuss:** Prompt engineering for grounding, citation requirements, similarity thresholds, evaluation metrics (faithfulness).

### 8. Design an evaluation pipeline for a RAG system
You've shipped a RAG bot. How do you know if it's getting better or worse over time?
- **Discuss:** Golden test set, retrieval metrics (precision@K, recall@K, MRR), generation metrics (faithfulness, relevance), human-in-the-loop feedback loops.

---

## Tier 3 — Trade-off questions

### 9. pgvector vs Pinecone vs Weaviate
When does each make sense? What does the dedicated vector DB give you that pgvector doesn't (and vice versa)?
- **Discuss:** Operational simplicity, scale ceiling, cost, query latency, hybrid search support.

### 10. Embedding model selection
You're choosing between OpenAI's `text-embedding-3-small`, an open-source model (e.g., BGE), and Cohere. Walk through the decision.
- **Discuss:** Quality vs cost vs latency vs vendor lock-in. When self-hosting matters. Dimensionality trade-offs.

### 11. Cache strategy for an LLM-powered API
What can you cache? What can't you? What are the gotchas?
- **Discuss:** Identical-query cache (easy), semantic cache (harder, embedding lookup before LLM call), embedding cache (avoid re-embedding identical content).

### 12. RAG vs fine-tuning
A user asks "should we fine-tune a model on our docs instead of doing RAG?" How do you answer?
- **Discuss:** When RAG wins (changing data, citations needed, lower cost). When fine-tuning wins (consistent style, narrow task). When both.

---

## Notes on usage

- These questions assume comfortable familiarity with embeddings and vector search. Start them after the conceptual sub-topics in Section 3 are mostly checked off.
- For Block 3 use, pull the question that maps to the sub-topic just covered.
- For interview prep proper, treat these as discussion questions — practice articulating answers verbally, not just writing them down.
