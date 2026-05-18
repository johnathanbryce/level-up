# Embeddings and Vector Concepts

## Section Legend

- [x] Chunk 1: What an embedding is
- [ ] Chunk 2: How embedding models work (high level)
- [ ] Chunk 3: Cosine similarity and distance metrics
- [ ] Chunk 4: Dimensionality and its impact on performance/quality
- [ ] Chunk 5: Common embedding models and trade-offs

---

## What an Embedding Is

- An **embedding** is a list of floating-point numbers - a **vector** - that represents the _meaning_ of a piece of text (or an image, or audio - but text is our focus)
- EXAMPLE: if you embed the string _"the cat say on the mat"_ with OpenAI's small model, you get back something like:
  - [0.012, -0.084, 0.231, 0.005, -0.117, ..., 0.043] # 1536 numbers

- The list of numbers is the embedding. Nothing magical happens to the string after - that vector IS the model's numerical representation of the meaning.

### The core property - why embeddings matter

- **Similar meaning → similar direction.**
- _Meaning becomes geometry. Two texts that mean similar things produce two vectors that point in similar directions._
- Without this property, a vector is just a meaningless list of numbers
  - _"dog"_ and _"puppy"_ -> vectors pointing **roughly the same direction**
  - _"dog"_ and _"golden retriever"_ -> also close
  - _"dog"_ and _"calculator"_ -> vectors pointing in **very different directions**

### The killer use case - semantic search

- Consider two phrases:
  - Phrase A: _"the bank approved my loan"_
  - Phrase B: _"the financial institution accepted my application"_
- These share **zero exact keywords**. A keyword search system (BM25, classic ES term matching) would treat them as completely unrelated documents
- Embedding-based search treats them as **high similar** because the underlying vectors point in nearly the same direction
- The model has learned, from training on huge text corpora, that "bank" and "financial institution" cluster together in meaning-space
- This is what makes "semantic search" a different category of tool from keyword search - and it is the foundation of RAG, recommendation systems, and most modern AI retrieval

### How semantic search actually works (mechanism)

1. **Index time:** every doc gets embedded → vector stored in a vector store (e.g., pgvector, Pinecone)
2. **Query time:** the query gets embedded with the **same model** → `V_query`
3. **Match step:** compute cosine similarity between `V_query` and every stored `V_doc` (or use an ANN index for speed — see chunk 3)
4. **Return:** the top-K docs by similarity score

- **GOTCHA — embeddings are passage-level, NOT word-level.** The query _"how do I reset my password"_ produces ONE 1536-dim vector for the whole sentence — NOT seven word vectors. This is the modern transformer-based approach. (Older techniques like word2vec DO operate per-word, but that's not what modern embedding models do.)

### Two properties worth remembering

1. **Deterministic** - same input text -> same vector (every time, from the same model version)
2. **Model-incompatible** - an embedding from OpenAI's model and an embedding from Cohere's model for the same string live in **different vector spaces**. You cannot compare them. Switching models = re-embedding everything from your store

## How Embedding Models Work (High Level)

### What an embedding model actually is

- An embedding model is a **neural network** — specifically a **transformer-based model**. Same family of architecture as GPT, Claude, BERT.
- **Input:** text (a string, up to the model's token limit)
- **Output:** a vector of floats (same dimensions every time for that model)
- **Text in, vector out.**

### What's a "neural network" (one sentence)

- A neural network is a **function** that maps inputs to outputs by passing them through layers of weighted math operations, where the **weights are learned from data during training** rather than hand-coded by a programmer.
- The weights ARE the model's knowledge. **Training** = adjusting weights until the function produces useful outputs. **Inference** = feeding inputs through the now-fixed weights to get outputs.

### What's a "transformer" (one sentence)

- A transformer is a specific neural network **architecture** (introduced in the 2017 paper *"Attention Is All You Need"*) that processes entire sequences at once using a mechanism called **self-attention** — each position in the input "looks at" every other position and figures out how relevant they are to each other.
- **Why this matters for embeddings:** self-attention is exactly what lets the model understand WHOLE-SEQUENCE meaning (the passage-level-not-word-level gotcha from chunk 1). Older architectures (RNNs, LSTMs) processed sequences one token at a time and lost information across long inputs. Transformers see the whole thing at once — which is why modern embedding models capture nuanced meaning that pre-2018 models couldn't.

### How the model learned to do this

- Trained on **billions of words**. The training objective rewards the model for producing vectors where **semantically similar text -> similar vectors** and dissimilar text -> distinct vectors. Different models use different training approaches but the *result* is always the same: a function that maps text -> meaningful geometry
- **Interview-level summary:** *trained on a huge text corpus with a similarity preserving objective*

### In practice - what API calls look like

- You make a request (or run a local model) and get back a vector:

    # Pseudo-code shape — actual script comes after chunk 3
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input="how do I reset my password"
    )

    vector = response.data[0].embedding   # [0.012, -0.084, ..., 0.043]  (1536 floats)

- 3 practical things to know:
    - **You pay per token**
    - **Latency**: typically 50-300ms per call. **Batching** multiple inputs in one API call is the big speedup
    - **Token limit:** every model has a max input length. 
        - text-embedding-3-small caps at 8191 tokens (~6000 words)
        - Anything longer must be chunked first (which is why "chunking strategies" is a whole sub-topic in RAG architecture) 
