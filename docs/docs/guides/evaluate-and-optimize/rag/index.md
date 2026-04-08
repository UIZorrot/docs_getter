---
source_url: "https://openrouter.ai/docs/guides/evaluate-and-optimize/rag"
title: "RAG with Embeddings & Rerank | Retrieval-Augmented Generation on OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:36.822124+00:00"
---
[Guides](../../administration/activity-export/index.md)[Evaluate & Optimize](../distillation/index.md)

# 

RAG with Embeddings & Rerank

Build retrieval-augmented generation pipelines using OpenRouter’s embeddings and rerank APIs

Retrieval-Augmented Generation (RAG) grounds LLM responses in your own data by retrieving relevant documents before generating an answer. This prevents hallucinations and keeps responses up to date without fine-tuning.

OpenRouter provides all three building blocks for a RAG pipeline through a single API:

1. **Embeddings** — convert documents and queries into vectors for semantic search
2. **Rerank** — re-score retrieved candidates for higher precision
3. **Chat Completions** — generate a final answer using the retrieved context

## How RAG Works

A typical RAG pipeline follows these steps:

1. **Index** — chunk your documents and generate embeddings for each chunk
2. **Retrieve** — embed the user’s query and find the most similar document chunks
3. **Rerank** (optional) — re-score the top candidates with a cross-encoder rerank model for better precision
4. **Generate** — pass the top documents as context to an LLM to produce a grounded answer

```
|  |
| --- |
| User Query |
| │ |
| ▼ |
| ┌──────────┐     ┌──────────────┐     ┌──────────┐     ┌──────────────┐ |
| │ Embed    │────▶│ Vector Search│────▶│ Rerank   │────▶│ LLM Generate │ |
| │ Query    │     │ (Top N docs) │     │ (Top K)  │     │ with Context │ |
| └──────────┘     └──────────────┘     └──────────┘     └──────────────┘ |
```

## Step 1: Index Your Documents

Split your documents into chunks and generate embeddings for each chunk. Store the embeddings in a vector database (or in-memory for prototyping).

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 |  |
| 4 | OPENROUTER_API_KEY = "{{API_KEY_REF}}" |
| 5 |  |
| 6 | # Your documents, split into chunks |
| 7 | chunks = [ |
| 8 | "OpenRouter is a unified API gateway for LLMs. It aggregates models from multiple providers.", |
| 9 | "RAG stands for Retrieval-Augmented Generation. It grounds LLM answers in external data.", |
| 10 | "Embeddings convert text into numerical vectors that capture semantic meaning.", |
| 11 | "Reranking uses a cross-encoder to re-score documents for a given query, improving precision.", |
| 12 | "Vector databases like Pinecone, Weaviate, and Qdrant store embeddings for fast similarity search.", |
| 13 | "Prompt caching can reduce costs by reusing previous computations for repeated prefixes.", |
| 14 | "OpenRouter supports provider routing to control which providers serve your requests.", |
| 15 | ] |
| 16 |  |
| 17 | # Generate embeddings for all chunks in one batch request |
| 18 | response = requests.post( |
| 19 | "https://openrouter.ai/api/v1/embeddings", |
| 20 | headers={ |
| 21 | "Authorization": f"Bearer {OPENROUTER_API_KEY}", |
| 22 | "Content-Type": "application/json", |
| 23 | }, |
| 24 | json={ |
| 25 | "model": "{{MODEL}}", |
| 26 | "input": chunks, |
| 27 | }, |
| 28 | ) |
| 29 |  |
| 30 | data = response.json() |
| 31 | # Each item in data["data"] contains an "embedding" vector |
| 32 | # Store these alongside your chunks in a vector database |
| 33 | document_embeddings = [ |
| 34 | {"text": chunks[item["index"]], "embedding": item["embedding"]} |
| 35 | for item in data["data"] |
| 36 | ] |
| 37 |  |
| 38 | print(f"Indexed {len(document_embeddings)} chunks with {len(document_embeddings[0]['embedding'])}-dim embeddings") |
```

##### 

In production, use a vector database (Pinecone, Weaviate, Qdrant, pgvector, etc.) to store and query embeddings efficiently. The in-memory approach shown here is for illustration only.

## Step 2: Retrieve Relevant Documents

When a user asks a question, embed the query and find the most similar document chunks using cosine similarity.

```
|  |  |
| --- | --- |
| 1 | import numpy as np |
| 2 |  |
| 3 | def cosine_similarity(a, b): |
| 4 | return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) |
| 5 |  |
| 6 | def retrieve(query, document_embeddings, top_n=5): |
| 7 | # Embed the query |
| 8 | response = requests.post( |
| 9 | "https://openrouter.ai/api/v1/embeddings", |
| 10 | headers={ |
| 11 | "Authorization": f"Bearer {OPENROUTER_API_KEY}", |
| 12 | "Content-Type": "application/json", |
| 13 | }, |
| 14 | json={ |
| 15 | "model": "{{MODEL}}", |
| 16 | "input": query, |
| 17 | }, |
| 18 | ) |
| 19 |  |
| 20 | query_embedding = np.array(response.json()["data"][0]["embedding"]) |
| 21 |  |
| 22 | # Score each document by cosine similarity |
| 23 | scored = [] |
| 24 | for doc in document_embeddings: |
| 25 | score = cosine_similarity(query_embedding, np.array(doc["embedding"])) |
| 26 | scored.append({"text": doc["text"], "score": float(score)}) |
| 27 |  |
| 28 | # Return the top N most similar chunks |
| 29 | scored.sort(key=lambda x: x["score"], reverse=True) |
| 30 | return scored[:top_n] |
| 31 |  |
| 32 | query = "What is RAG and how does it work?" |
| 33 | results = retrieve(query, document_embeddings, top_n=5) |
| 34 |  |
| 35 | print("Retrieved documents:") |
| 36 | for i, r in enumerate(results): |
| 37 | print(f"  {i+1}. (score: {r['score']:.4f}) {r['text']}") |
```

## Step 3: Rerank for Better Precision

Embedding-based retrieval is fast but approximate. A rerank model uses a cross-encoder to compare each document directly against the query, producing more accurate relevance scores. This is especially valuable when you retrieve many candidates (e.g., 20) and want to narrow down to the best few (e.g., 3).

```
|  |  |
| --- | --- |
| 1 | def rerank(query, documents, top_n=3): |
| 2 | response = requests.post( |
| 3 | "https://openrouter.ai/api/v1/rerank", |
| 4 | headers={ |
| 5 | "Authorization": f"Bearer {OPENROUTER_API_KEY}", |
| 6 | "Content-Type": "application/json", |
| 7 | }, |
| 8 | json={ |
| 9 | "model": "{{RERANK_MODEL}}", |
| 10 | "query": query, |
| 11 | "documents": documents, |
| 12 | "top_n": top_n, |
| 13 | }, |
| 14 | ) |
| 15 |  |
| 16 | data = response.json() |
| 17 | return data["results"] |
| 18 |  |
| 19 | # Use the texts from the retrieval step |
| 20 | retrieved_texts = [r["text"] for r in results] |
| 21 |  |
| 22 | reranked = rerank(query, retrieved_texts, top_n=3) |
| 23 |  |
| 24 | print("Reranked documents:") |
| 25 | for r in reranked: |
| 26 | print(f"  Score: {r['relevance_score']:.4f} | {r['document']['text']}") |
```

## Step 4: Generate an Answer with Context

Pass the top-ranked documents as context to a chat model. The LLM generates a grounded answer based on the retrieved information.

```
|  |  |
| --- | --- |
| 1 | def generate_answer(query, context_docs): |
| 2 | # Build a context string from the reranked documents |
| 3 | context = "\n\n".join( |
| 4 | f"[{i+1}] {doc['document']['text']}" |
| 5 | for i, doc in enumerate(context_docs) |
| 6 | ) |
| 7 |  |
| 8 | response = requests.post( |
| 9 | "https://openrouter.ai/api/v1/chat/completions", |
| 10 | headers={ |
| 11 | "Authorization": f"Bearer {OPENROUTER_API_KEY}", |
| 12 | "Content-Type": "application/json", |
| 13 | }, |
| 14 | json={ |
| 15 | "model": "{{CHAT_MODEL}}", |
| 16 | "messages": [ |
| 17 | { |
| 18 | "role": "system", |
| 19 | "content": "Answer the user's question based on the provided context. " |
| 20 | "Cite the relevant source numbers in brackets. " |
| 21 | "If the context doesn't contain enough information, say so.", |
| 22 | }, |
| 23 | { |
| 24 | "role": "user", |
| 25 | "content": f"Context:\n{context}\n\nQuestion: {query}", |
| 26 | }, |
| 27 | ], |
| 28 | }, |
| 29 | ) |
| 30 |  |
| 31 | return response.json()["choices"][0]["message"]["content"] |
| 32 |  |
| 33 | answer = generate_answer(query, reranked) |
| 34 | print(f"Question: {query}") |
| 35 | print(f"Answer: {answer}") |
```

## Complete Example

Here is a full end-to-end RAG pipeline combining all four steps:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import numpy as np |
| 3 |  |
| 4 | OPENROUTER_API_KEY = "{{API_KEY_REF}}" |
| 5 | EMBEDDING_MODEL = "{{EMBEDDING_MODEL}}" |
| 6 | RERANK_MODEL = "{{RERANK_MODEL}}" |
| 7 | CHAT_MODEL = "{{CHAT_MODEL}}" |
| 8 | BASE_URL = "https://openrouter.ai/api/v1" |
| 9 |  |
| 10 | def get_headers(): |
| 11 | return { |
| 12 | "Authorization": f"Bearer {OPENROUTER_API_KEY}", |
| 13 | "Content-Type": "application/json", |
| 14 | } |
| 15 |  |
| 16 | def embed(texts): |
| 17 | """Generate embeddings for a list of texts.""" |
| 18 | response = requests.post( |
| 19 | f"{BASE_URL}/embeddings", |
| 20 | headers=get_headers(), |
| 21 | json={"model": EMBEDDING_MODEL, "input": texts}, |
| 22 | ) |
| 23 | return [item["embedding"] for item in response.json()["data"]] |
| 24 |  |
| 25 | def cosine_similarity(a, b): |
| 26 | return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) |
| 27 |  |
| 28 | def retrieve(query_embedding, doc_embeddings, top_n=10): |
| 29 | """Find the top N most similar documents by cosine similarity.""" |
| 30 | scored = [ |
| 31 | (i, cosine_similarity(query_embedding, emb)) |
| 32 | for i, emb in enumerate(doc_embeddings) |
| 33 | ] |
| 34 | scored.sort(key=lambda x: x[1], reverse=True) |
| 35 | return scored[:top_n] |
| 36 |  |
| 37 | def rerank(query, documents, top_n=3): |
| 38 | """Rerank documents using a cross-encoder model.""" |
| 39 | response = requests.post( |
| 40 | f"{BASE_URL}/rerank", |
| 41 | headers=get_headers(), |
| 42 | json={ |
| 43 | "model": RERANK_MODEL, |
| 44 | "query": query, |
| 45 | "documents": documents, |
| 46 | "top_n": top_n, |
| 47 | }, |
| 48 | ) |
| 49 | return response.json()["results"] |
| 50 |  |
| 51 | def generate(query, context_docs): |
| 52 | """Generate an answer grounded in the provided context.""" |
| 53 | context = "\n\n".join( |
| 54 | f"[{i+1}] {doc}" |
| 55 | for i, doc in enumerate(context_docs) |
| 56 | ) |
| 57 | response = requests.post( |
| 58 | f"{BASE_URL}/chat/completions", |
| 59 | headers=get_headers(), |
| 60 | json={ |
| 61 | "model": CHAT_MODEL, |
| 62 | "messages": [ |
| 63 | { |
| 64 | "role": "system", |
| 65 | "content": ( |
| 66 | "Answer the user's question using only the provided context. " |
| 67 | "Cite sources with [n]. If the context is insufficient, say so." |
| 68 | ), |
| 69 | }, |
| 70 | { |
| 71 | "role": "user", |
| 72 | "content": f"Context:\n{context}\n\nQuestion: {query}", |
| 73 | }, |
| 74 | ], |
| 75 | }, |
| 76 | ) |
| 77 | return response.json()["choices"][0]["message"]["content"] |
| 78 |  |
| 79 | # --- Pipeline --- |
| 80 |  |
| 81 | # 1. Index: chunk your knowledge base and embed |
| 82 | chunks = [ |
| 83 | "OpenRouter is a unified API gateway for LLMs. It aggregates models from multiple providers into a single OpenAI-compatible interface.", |
| 84 | "RAG stands for Retrieval-Augmented Generation. It retrieves relevant documents and uses them as context for LLM generation.", |
| 85 | "Embeddings convert text into high-dimensional vectors where semantically similar texts are closer together.", |
| 86 | "Reranking uses a cross-encoder to compare each document directly against the query, producing more accurate relevance scores than embedding similarity alone.", |
| 87 | "Vector databases like Pinecone, Weaviate, and Qdrant are optimized for storing and querying embedding vectors at scale.", |
| 88 | "Prompt caching reduces costs by reusing computations for repeated prompt prefixes across requests.", |
| 89 | "OpenRouter supports provider routing to control which upstream providers serve your requests based on cost, latency, or privacy preferences.", |
| 90 | ] |
| 91 | doc_embeddings = embed(chunks) |
| 92 |  |
| 93 | # 2. Retrieve: embed the query and find similar chunks |
| 94 | query = "How does RAG improve LLM responses?" |
| 95 | query_embedding = embed([query])[0] |
| 96 | top_matches = retrieve(query_embedding, doc_embeddings, top_n=5) |
| 97 | retrieved_texts = [chunks[i] for i, _ in top_matches] |
| 98 |  |
| 99 | # 3. Rerank: re-score with a cross-encoder for better precision |
| 100 | reranked = rerank(query, retrieved_texts, top_n=3) |
| 101 | context_texts = [r["document"]["text"] for r in reranked] |
| 102 |  |
| 103 | # 4. Generate: produce a grounded answer |
| 104 | answer = generate(query, context_texts) |
| 105 | print(f"Q: {query}\nA: {answer}") |
```

## When to Use Rerank

Reranking adds an extra API call, so it’s worth understanding when it helps most:

**Use rerank when:**

- Your knowledge base is large (hundreds or thousands of chunks) and embedding retrieval alone returns noisy results
- Precision matters more than latency (e.g., customer-facing Q&A, legal or medical documents)
- You retrieve many candidates (e.g., top 20) and need to narrow to the best 3-5

**Skip rerank when:**

- Your knowledge base is small and embedding retrieval already returns highly relevant results
- You need the lowest possible latency (rerank adds one additional API call)
- You’re building a prototype and want to keep the pipeline simple

## Chunking Strategies

How you split documents significantly affects retrieval quality:

- **By paragraph or section** — preserves semantic coherence and works well for structured documents
- **Fixed-size with overlap** — split into chunks of ~200-500 tokens with ~50-token overlap to avoid losing context at boundaries
- **By semantic boundary** — use headings, section breaks, or sentence boundaries to create natural chunks

##### 

Smaller chunks (200-300 tokens) tend to produce more precise retrieval but may lose surrounding context. Larger chunks (500-1000 tokens) preserve more context but may dilute relevance signals. Experiment with your specific data to find the right balance.

## Best Practices

**Use the same embedding model for indexing and querying.** Mixing models produces incompatible vector spaces and will give poor retrieval results.

**Batch your embedding requests.** Send multiple texts in a single API call to reduce latency and costs. The embeddings API accepts arrays of inputs.

**Cache embeddings.** Embeddings for the same text are deterministic. Store them in a database to avoid recomputing.

**Retrieve more than you need, then rerank.** A common pattern is to retrieve 10-20 candidates via embeddings, then rerank to the top 3-5. This combines the speed of embedding search with the precision of cross-encoder reranking.

**Include metadata in your prompt.** When generating, include source metadata (document title, section, URL) alongside the text so the LLM can produce proper citations.

**Set a relevance threshold.** After reranking, filter out documents below a minimum relevance score to avoid injecting irrelevant context that could confuse the LLM.

## Available Models

Browse available models for each step:

- **Embedding models**: [openrouter.ai/models?output\_modalities=embeddings](https://openrouter.ai/models)
- **Rerank models**: [openrouter.ai/models?output\_modalities=rerank](https://openrouter.ai/models)
- **Chat models**: [openrouter.ai/models](https://openrouter.ai/models)

## Related Resources

- [Embeddings API](../../../api/reference/embeddings/index.md) — full API reference for generating embeddings
- [Provider Routing](../../../features/provider-routing/index.md) — control which providers serve your requests
- [Prompt Caching](../../best-practices/prompt-caching/index.md) — reduce costs for repeated prompt prefixes
- [Structured Outputs](../../features/structured-outputs/index.md) — enforce JSON schema on LLM responses for structured RAG output
