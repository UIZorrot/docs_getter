---
source_url: "https://openrouter.ai/docs/api/reference/embeddings"
title: "Embeddings API | Convert Text and Images to Vector Representations with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:28.850330+00:00"
---
[API Guides](../overview/index.md)

# Embeddings

Generate vector embeddings from text and images

Embeddings are numerical representations of text that capture semantic meaning. They convert text into vectors (arrays of numbers) that can be used for various machine learning tasks. OpenRouter provides a unified API to access embedding models from multiple providers.

## What are Embeddings?

Embeddings transform text into high-dimensional vectors where semantically similar texts are positioned closer together in vector space. For example, “cat” and “kitten” would have similar embeddings, while “cat” and “airplane” would be far apart.

These vector representations enable machines to understand relationships between pieces of text, making them essential for many AI applications.

## Common Use Cases

Embeddings are used in a wide variety of applications:

**RAG (Retrieval-Augmented Generation)**: Build RAG systems that retrieve relevant context from a knowledge base before generating answers. Embeddings help find the most relevant documents to include in the LLM’s context.

**Semantic Search**: Convert documents and queries into embeddings, then find the most relevant documents by comparing vector similarity. This provides more accurate results than traditional keyword matching because it understands meaning rather than just matching words.

**Recommendation Systems**: Generate embeddings for items (products, articles, movies) and user preferences to recommend similar items. By comparing embedding vectors, you can find items that are semantically related even if they don’t share obvious keywords.

**Clustering and Classification**: Group similar documents together or classify text into categories by analyzing embedding patterns. Documents with similar embeddings likely belong to the same topic or category.

**Duplicate Detection**: Identify duplicate or near-duplicate content by comparing embedding similarity. This works even when text is paraphrased or reworded.

**Anomaly Detection**: Detect unusual or outlier content by identifying embeddings that are far from typical patterns in your dataset.

## How to Use Embeddings

### Basic Request

To generate embeddings, send a POST request to `/embeddings` with your text input and chosen model:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const response = await openRouter.embeddings.generate({ |
| 8 | model: '{{MODEL}}', |
| 9 | input: 'The quick brown fox jumps over the lazy dog', |
| 10 | }); |
| 11 |  |
| 12 | console.log(response.data[0].embedding); |
```

### Batch Processing

You can generate embeddings for multiple texts in a single request by passing an array of strings:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const response = await openRouter.embeddings.generate({ |
| 8 | model: '{{MODEL}}', |
| 9 | input: [ |
| 10 | 'Machine learning is a subset of artificial intelligence', |
| 11 | 'Deep learning uses neural networks with multiple layers', |
| 12 | 'Natural language processing enables computers to understand text' |
| 13 | ], |
| 14 | }); |
| 15 |  |
| 16 | // Process each embedding |
| 17 | response.data.forEach((item, index) => { |
| 18 | console.log(`Embedding ${index}: ${item.embedding.length} dimensions`); |
| 19 | }); |
```

### Image Input

Some embedding models support image inputs, enabling multimodal embeddings that capture visual content alongside text. This is useful for image search, visual similarity, and cross-modal retrieval tasks.

To send an image, wrap your input in the multimodal format with a `content` array containing `image_url` objects. You can also combine text and images in a single input block.

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 |  |
| 3 | response = requests.post( |
| 4 | "https://openrouter.ai/api/v1/embeddings", |
| 5 | headers={ |
| 6 | "Authorization": f"Bearer {{API_KEY_REF}}", |
| 7 | "Content-Type": "application/json", |
| 8 | }, |
| 9 | json={ |
| 10 | "model": "{{MODEL}}", |
| 11 | "input": [ |
| 12 | { |
| 13 | "content": [ |
| 14 | {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/640px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"}} |
| 15 | ] |
| 16 | } |
| 17 | ], |
| 18 | "encoding_format": "float", |
| 19 | } |
| 20 | ) |
| 21 |  |
| 22 | data = response.json() |
| 23 | embedding = data["data"][0]["embedding"] |
| 24 | print(f"Embedding dimension: {len(embedding)}") |
```

You can also combine text and images in a single input to generate a joint embedding:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 |  |
| 3 | response = requests.post( |
| 4 | "https://openrouter.ai/api/v1/embeddings", |
| 5 | headers={ |
| 6 | "Authorization": f"Bearer {{API_KEY_REF}}", |
| 7 | "Content-Type": "application/json", |
| 8 | }, |
| 9 | json={ |
| 10 | "model": "{{MODEL}}", |
| 11 | "input": [ |
| 12 | { |
| 13 | "content": [ |
| 14 | {"type": "text", "text": "A scenic boardwalk through a green meadow"}, |
| 15 | {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/640px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"}} |
| 16 | ] |
| 17 | } |
| 18 | ], |
| 19 | "encoding_format": "float", |
| 20 | } |
| 21 | ) |
| 22 |  |
| 23 | data = response.json() |
| 24 | embedding = data["data"][0]["embedding"] |
| 25 | print(f"Embedding dimension: {len(embedding)}") |
```

## API Reference

For detailed information about request parameters, response format, and all available options, see the [Embeddings API Reference](../../../api-reference/embeddings/create-embeddings/index.md).

## Available Models

OpenRouter provides access to various embedding models from different providers. You can view all available embedding models at:

[https://openrouter.ai/models?fmt=cards&output\_modalities=embeddings](https://openrouter.ai/models)

To list all available embedding models programmatically:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const models = await openRouter.embeddings.listModels(); |
| 8 | console.log(models.data); |
```

## Practical Example: Semantic Search

Here’s a complete example of building a semantic search system using embeddings:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | // Sample documents |
| 8 | const documents = [ |
| 9 | "The cat sat on the mat", |
| 10 | "Dogs are loyal companions", |
| 11 | "Python is a programming language", |
| 12 | "Machine learning models require training data", |
| 13 | "The weather is sunny today" |
| 14 | ]; |
| 15 |  |
| 16 | // Function to calculate cosine similarity |
| 17 | function cosineSimilarity(a: number[], b: number[]): number { |
| 18 | const dotProduct = a.reduce((sum, val, i) => sum + val * b[i], 0); |
| 19 | const magnitudeA = Math.sqrt(a.reduce((sum, val) => sum + val * val, 0)); |
| 20 | const magnitudeB = Math.sqrt(b.reduce((sum, val) => sum + val * val, 0)); |
| 21 | return dotProduct / (magnitudeA * magnitudeB); |
| 22 | } |
| 23 |  |
| 24 | async function semanticSearch(query: string, documents: string[]) { |
| 25 | // Generate embeddings for all documents and the query |
| 26 | const response = await openRouter.embeddings.generate({ |
| 27 | model: '{{MODEL}}', |
| 28 | input: [query, ...documents], |
| 29 | }); |
| 30 |  |
| 31 | const queryEmbedding = response.data[0].embedding; |
| 32 | const docEmbeddings = response.data.slice(1); |
| 33 |  |
| 34 | // Calculate similarity scores |
| 35 | const results = documents.map((doc, i) => ({ |
| 36 | document: doc, |
| 37 | similarity: cosineSimilarity( |
| 38 | queryEmbedding as number[], |
| 39 | docEmbeddings[i].embedding as number[] |
| 40 | ), |
| 41 | })); |
| 42 |  |
| 43 | // Sort by similarity (highest first) |
| 44 | results.sort((a, b) => b.similarity - a.similarity); |
| 45 |  |
| 46 | return results; |
| 47 | } |
| 48 |  |
| 49 | // Search for documents related to pets |
| 50 | const results = await semanticSearch("pets and animals", documents); |
| 51 | console.log("Search results:"); |
| 52 | results.forEach((result, i) => { |
| 53 | console.log(`${i + 1}. ${result.document} (similarity: ${result.similarity.toFixed(4)})`); |
| 54 | }); |
```

Expected output:

```
|  |
| --- |
| Search results: |
| 1. Dogs are loyal companions (similarity: 0.8234) |
| 2. The cat sat on the mat (similarity: 0.7891) |
| 3. The weather is sunny today (similarity: 0.3456) |
| 4. Machine learning models require training data (similarity: 0.2987) |
| 5. Python is a programming language (similarity: 0.2654) |
```

## Best Practices

**Choose the Right Model**: Different embedding models have different strengths. Smaller models (like qwen/qwen3-embedding-0.6b or openai/text-embedding-3-small) are faster and cheaper, while larger models (like openai/text-embedding-3-large) provide better quality. Test multiple models to find the best fit for your use case.

**Batch Your Requests**: When processing multiple texts, send them in a single request rather than making individual API calls. This reduces latency and costs.

**Cache Embeddings**: Embeddings for the same text are deterministic (they don’t change). Store embeddings in a database or vector store to avoid regenerating them repeatedly.

**Normalize for Comparison**: When comparing embeddings, use cosine similarity rather than Euclidean distance. Cosine similarity is scale-invariant and works better for high-dimensional vectors.

**Consider Context Length**: Each model has a maximum input length (context window). Longer texts may need to be chunked or truncated. Check the model’s specifications before processing long documents.

**Use Appropriate Chunking**: For long documents, split them into meaningful chunks (paragraphs, sections) rather than arbitrary character limits. This preserves semantic coherence.

## Provider Routing

You can control which providers serve your embedding requests using the `provider` parameter. This is useful for:

- Ensuring data privacy with specific providers
- Optimizing for cost or latency
- Using provider-specific features

Example with provider preferences:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/text-embedding-3-small", |
| 3 | "input": "Your text here", |
| 4 | "provider": { |
| 5 | "order": ["openai", "azure"], |
| 6 | "allow_fallbacks": true, |
| 7 | "data_collection": "deny" |
| 8 | } |
| 9 | } |
```

For more information, see [Provider Routing](../../../features/provider-routing/index.md).

## Error Handling

Common errors you may encounter:

**400 Bad Request**: Invalid input format or missing required parameters. Check that your `input` and `model` parameters are correctly formatted.

**401 Unauthorized**: Invalid or missing API key. Verify your API key is correct and included in the Authorization header.

**402 Payment Required**: Insufficient credits. Add credits to your OpenRouter account.

**404 Not Found**: The specified model doesn’t exist or isn’t available for embeddings. Check the model name and verify it’s an embedding model.

**429 Too Many Requests**: Rate limit exceeded. Implement exponential backoff and retry logic.

**529 Provider Overloaded**: The provider is temporarily overloaded. Enable `allow_fallbacks: true` to automatically use backup providers.

## Limitations

- **No Streaming**: Unlike chat completions, embeddings are returned as complete responses. Streaming is not supported.
- **Token Limits**: Each model has a maximum input length. Texts exceeding this limit will be truncated or rejected.
- **Deterministic Output**: Embeddings for the same input text will always be identical (no temperature or randomness).
- **Language Support**: Some models are optimized for specific languages. Check model documentation for language capabilities.

## Related Resources

- [Models Page](https://openrouter.ai/models) - Browse all available embedding models
- [Provider Routing](../../../features/provider-routing/index.md) - Control which providers serve your requests
- [Authentication](../../authentication/index.md) - Learn about API key authentication
- [Errors](../errors-and-debugging/index.md) - Detailed error codes and handling
