# RAG Deep — My Notes

> **Status:** Not yet taught.
> **Lesson plan:** [../lesson-tracker.md](../lesson-tracker.md) → RAG Deep section.
> Take notes below as Claude teaches. You ship RAG production code at Caseway already — this lesson formalizes and deepens what you do.

---

## Chunk 1 — Full RAG pipeline (offline indexing + online querying)

**RAG = two parallel pipelines, sharing the vector store as handoff.**

- **Indexing (offline):** `Documents → Chunk → Embed → Store`. Batch/async, latency irrelevant, cost = embedding calls.
- **Querying (online):** `Query → Embed → Retrieve top-K → Rerank → Assemble → Generate → Cite`. User-facing, sub-second target, cost = LLM + reranker.

**Why "two pipelines" matters as framing:** can't reason about chunking, embedding model, or vector store choice without knowing whether you're optimizing ingestion throughput (offline) or query latency (online). They pull opposite ways.

**Killer stat (memorize):** ~73% of RAG failures are RETRIEVAL, not generation.

**Interview line:** _"Bigger LLMs are the wrong lever. ~73% of RAG failures are retrieval, so I'd invest in chunking, hybrid search, and reranking before reaching for a more expensive generator."_

---

## Chunk 2 — Chunking strategies (recursive 512-token default; fixed / semantic / document-aware)

- The default -> **recursive character splitter** - 512 tokens, 10-20% overlap.
  - **What "recursive" actually means:** the splitter tries to break on natural boundaries **in order** - _paragraph -> sentence -> word -> char_
  - This is what keeps chunks coherent: sentences stay intact, paragraphs stay grouped where they fit

- **When to upgrade to document-aware splitters** (format has structure worth preserving):
  - **Code** - split on functions/classes, not mid-function
  - **Markdown** - split on headers
  - **PDFs with tables** - preserve table boundaries

- **Long-doc trick**: parent-document retrieval - index _small_ chunks for retrieval position, return the parent doc for generation context

- **Interview line:** _"Recursive 512-token splitter with 10-20% overlap is the prod default. Splits on natural boundaries so chunks stay coherent. Upgrade to document-aware splitters when the format has structure worth preserving, like code or tables in PDFs_

---

## Chunk 3 — Embedding model choice (text-embedding-3-small default; when to self-host)
- **Default** OpenAi *text-embedding-3-small*
    - **Why this model?**
        - Cheap enough that re-embedding a corpus is affordable
        - 1536 dimensions = fits comfortable in any vector store
        - Multilingual
        - OpenAI's batch API gets you 50% off for offline indexing

- **When to upgrade to text-embedding-3-large:** if benchmarks show recall @k is your bottleneck 
- **The migration trap:**
    - **Different embedding models produce incompatible vectors. You CANNOT mix them in the same index. Switching models means re-embedding your ENTIRE corpus**

---

## Chunk 4 — Vector store choice (pgvector / Pinecone)

- **pgvector (Postgres extension)**
    - **When:** already on Postgres + corpus <10M vectors + want one DB to back up
    - **Why it wins:** transactional consistency with your app data, no cross-system sync, free
    - **Why it loses:** doesn't scale past ~10M vectors well, no managed tier (you run it)

- **Pinecone (managed SaaS)**
    - **When:** want zero ops + can pay for it + scale matters
    - **Why it wins:** fully managed, scales to billions, predictable latency
    - **Why it loses:** $, vendor lock-in, vectors live outside infra

- **Bonus name-drops (if asked):**
    - **Elasticsearch** — search engine that added vector capabilities (valid choice when keyword + vector are both first-class — what Caseway uses)
    - **Weaviate** — native hybrid search built in
    - **Qdrant** — the open-source on-prem option if vendor-lock-in is a hard no

### Decision table

| Situation | Pick |
|---|---|
| Already on Postgres, <10M vectors | **pgvector** |
| Zero-ops, willing to pay | **Pinecone** |
| Keyword + vector both first-class (security logs, docs) | **Elasticsearch** |
| Billions of vectors | **Milvus** |
---

## Chunk 5 — Retrieval techniques (vector vs BM25 vs hybrid + RRF)
- **Why pure vector only search misses things** - vector search finds **semantic** matches ("car" matches "automobile") but it **misses exact-token matches** that matter (model numbers, error codes, names, IDs, acronyms).
    - A query for *CVE-2024-1234* against pure vector retrieval might return semantically-similar vulnerability descriptions but miss the doc that literally contains that CVE ID

- **Why pure BM25 misses things** - BM25 = keyword relevance, based on the term frequency and rarity. Finds **exact-token matches** beautifully, but conceptual matches. 
    - A query for *car safety* won't match a doc that says "vehicle crash protection"

- **They fail in opposite directions**. That's why hybrid wins - they cover each other's blind spots

- **The merge problem:** can't average BM25 scores and vector scores - different scales, not comparable.
- **Reciprocal Rank Fusion (RRF)** is the standard solution - merges by **rank position**, not score. Docs that rank high in BOTH lists score highest.
- **Most modern vector stores handle RRF natively** (ES, OpenSearch, Qdrant, Weaviate) - it's a config flag, not something you implement.

- **Interview line:** *"Hybrid retrieval is the biggest single lever in RAG. Vector finds semantic matches; BM25 finds exact tokens like CVE IDs or model numbers. They fail in opposite directions, so combining them covers both blind spots. The merge problem is that the two have incompatible score scales — RRF solves it by merging on rank instead of score. Most modern vector stores ship RRF natively, so it's a config-level decision."*

---

## Chunk 6 — Reranking 
- 2-stage retrieval pattern: *Hybrid retrieve (top 50-100) -> Rerank (top 5-10) -> LLM*

---

## Chunk 7 — Context assembly + citations (dedupe, order, "lost in the middle")
- Once you have your top 5-10 re-ranked chunks, you don't just dump them into the prompt. 3 things to handle before LLM call:
    1. **Dedup near-duplicates** - if two chunks say nearly the same thing, drop one 
    2. **Ordering matters ("lost in the middle")** - LLMs attend more to the **start and the end** of the context window. Put the **most-relevant chunk at the start and the second most relevant chunk at the end**
    3. **Mandatory "I don't know" fallback** - if retrieval returns nothing relevant (low confidence scores) the system must return "I don't have enough info to answer that"

- **Citations:** each retrieved chunk should carry metadata (doc ID, section, line range). When you generate the answer, embed those as inline citations. 

---

## Chunk 8 — RAG evaluation (faithfulness, answer relevancy, context precision; RAGAS)
- How do you evaluate a RAG system? --> a framework (**RAGAS** is the prod standard)
- How does it work mechanically? --> **LLM-as-judge**. A second LLM scores the first LLMs output and allows you to eval on **live production traffic** without human labels 
- Why does it matter? --> **No human-labeled ground-truth data needed**. 

---

## Chunk 9 — Advanced patterns (HyDE, parent-document retrieval, multi-query)
1. **HyDE (Hypothetical Document Embeddings)**
    - **The trick:** generate a hypothetical answer to the user's query, then embed THAT and search with it (instead of embedding the question itself)
    - **Why it works:** answer-text matches answer-text in vector space better than question-text matches answer-text. Questions and answers don't look semantically identical even when they should

2. **Query Rewriting**
    - **The trick:** before retrieval, rewrite the user's query (fix spelling, expand acronyms, generate multiple paraphrases and retrieve against all of them)
    - **Why it works:** users write messy queries. Cleaning + expanding before retrieval catches docs the original phrasing would miss




---

## End-of-Lesson Self-Quiz Answers

_Filled in after Claude runs the quiz._
