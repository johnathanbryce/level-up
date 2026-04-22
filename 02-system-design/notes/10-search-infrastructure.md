# Search Infrastructure as a System Component

## 4 Search Topics

1. What Elasticsearch is (and what it isn't)
2. When to reach for a search layer
3. How search fits into a system
4. Keyword vs. Semantic Search (BM25 vs. Embeddings)

---

## What Elasticsearch is (and what it isn't)
- ES is a **search engine** -- purpose-built for text search, log aggregation, and analytics
- When a user types a freeform query like "wireless headphones under 100" into a product search box, that's the kind of problem ES solves
- 3 things it's commonly used for:
        1. Product/content search -- ranked, relevant results from natural language queries
        2. Log aggregation
        3. Analytics dashboards -- querying large volumes of event data fast
- ES can function as a vector database, but important to note some distinctions:
    - **Elasticsearch** -- search engine first. Text search, log aggregation, analytics. Vector search was added on top. General purpose
    - **Native vector DBs** (Pinecone, Weviate) -- built from day one for high-dimension vector operations. Tends to outperform ES for pure vector search at scale
    - **pgvector** -- postgres extension for storing/querying embeddings. Not a standalone DB

- ES is not exclusively a vector DB, and calling it one by default is imprecise

## When to reach for a search layer
- Your primary DB (postgres) is fine when you're filtering on exact matches 
- You add a search engine when users are typing **freeform queries** and expect ranked, relevant results 
    - SQL can't rank
    - Elasticsearch scores results by relevance and handles partial matches, typos, etc.
- Signal for sys design interview: the moment a requirement says "users can search for X by keyword" -- thats the cue to mention a search layer
    - Another signal is **log volume** -- if you're ingesting millions of log events per minute and need to query them fast, ES is the standard answer

- [SCENARIO] - your startup has a Postgres database with 5 million job listings. Users type things like "senior react engineer remote NYC." Do you query Postgres or add Elasticsearch? Why
    - [ANSWER] 
        - Elasticsearch for keyword relevance + vector search for semantic similarity, results merged. 
        - Data stays in sync between ES and Postgres database so results provided by ES align with the reality of the database

## How search fits into a system
- Elasticsearch is a **read-optimized view** of your primary data - never the source of truth 
- The pattern:
        1. Write goes to Postgres (source of truth)
        2. A sync process (queue consumer or event stream) copies that data to Elasticsearch
        3. Search queries hit Elasticsearch, not Postgres

- The trade-off: **eventual consistency**. A new job posting might not appear in search results for a second or two. That's acceptable for almost every search use case

## Keyword Search vs. Semantic Search (BM25 vs. Embeddings)
- **BM25** = keyword relevance scoring
    - Looks how often the search term appears in a document and how rare it is across all documents
    - Pure text matching, no embeddings involved (this is what ES does natively)
- **Semantic similarity (embeddings)** = vector math
    - Convert query and documents to vectors, find the closest ones
    - This is what pgvector / Pinecone do

- **Hybrid search** = combining both
    - ES/BM25 for keyword matches + vector DB for semantic matches, results merged

### Revised Mental Model

- Keyword query with relevance ranking -> Elasticsearch (BM25)
- Semantic / conceptual query -> pgvector / vector DB (embeddings)
- Both at once -> hybrid search 