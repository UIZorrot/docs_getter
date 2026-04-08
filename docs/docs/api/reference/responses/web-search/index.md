---
source_url: "https://openrouter.ai/docs/api/reference/responses/web-search"
title: "Responses API Beta Web Search | Real-time Information Retrieval | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:30.788940+00:00"
---
[API Guides](../../overview/index.md)[Responses API](../overview/index.md)

# Web Search

Real-time web search integration with the Responses API Beta

##### Beta API

This API is in **beta stage** and may have breaking changes.

The Responses API Beta supports web search integration, allowing models to access real-time information from the internet and provide responses with proper citations and annotations.

##### Deprecated Plugin Approach

The web search plugin (`plugins: [{ id: "web" }]`) shown below is deprecated. Use the [`openrouter:web_search` server tool](../../../../guides/features/server-tools/web-search/index.md) instead, which works with both the Chat Completions and Responses APIs via the `tools` array.

## Web Search Plugin

Enable web search using the `plugins` parameter:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: 'What is OpenRouter?', |
| 10 | plugins: [{ id: 'web', max_results: 3 }], |
| 11 | max_output_tokens: 9000, |
| 12 | }), |
| 13 | }); |
| 14 |  |
| 15 | const result = await response.json(); |
| 16 | console.log(result); |
```

## Plugin Configuration

Configure web search behavior:

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | string | **Required.** Must be “web” |
| `engine` | string | Search engine: `"native"`, `"exa"`, `"firecrawl"`, `"parallel"`, or omit for auto |
| `max_results` | integer | Maximum search results to retrieve (1-25, default 5) |
| `include_domains` | string[] | Restrict results to these domains (supports wildcards like `*.substack.com`) |
| `exclude_domains` | string[] | Exclude results from these domains |

See the [Web Search plugin docs](../../../../guides/features/plugins/web-search/index.md) for full details on engine selection, domain filter compatibility, and pricing.

## X Search Filters (xAI only)

When using xAI models (e.g. `x-ai/grok-4.1-fast`),
you can pass `x_search_filter` as a top-level
request parameter to filter X/Twitter search
results:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "x-ai/grok-4.1-fast", |
| 3 | "input": "What are people saying about AI?", |
| 4 | "plugins": [{ "id": "web" }], |
| 5 | "x_search_filter": { |
| 6 | "allowed_x_handles": ["OpenRouterAI"], |
| 7 | "from_date": "2025-01-01", |
| 8 | "enable_image_understanding": true |
| 9 | } |
| 10 | } |
```

| Parameter | Type | Description |
| --- | --- | --- |
| `allowed_x_handles` | string[] | Only include posts from these handles (max 10) |
| `excluded_x_handles` | string[] | Exclude posts from these handles (max 10) |
| `from_date` | string | Start date (ISO 8601, e.g. `"2025-01-01"`) |
| `to_date` | string | End date (ISO 8601, e.g. `"2025-12-31"`) |
| `enable_image_understanding` | boolean | Analyze images in posts |
| `enable_video_understanding` | boolean | Analyze videos in posts |

##### 

`allowed_x_handles` and `excluded_x_handles` are
mutually exclusive. See the
[Web Search plugin docs](../../../../guides/features/plugins/web-search/index.md)
for full details.

## Structured Message with Web Search

Use structured messages for more complex queries:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'What was a positive news story from today?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | plugins: [{ id: 'web', max_results: 2 }], |
| 22 | max_output_tokens: 9000, |
| 23 | }), |
| 24 | }); |
| 25 |  |
| 26 | const result = await response.json(); |
| 27 | console.log(result); |
```

## Online Model Variants

##### Deprecated

The `:online` variant is deprecated. Use the [`openrouter:web_search` server tool](../../../../guides/features/server-tools/web-search/index.md) instead.

Some models have built-in web search capabilities using the `:online` variant:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini:online', |
| 9 | input: 'What was a positive news story from today?', |
| 10 | max_output_tokens: 9000, |
| 11 | }), |
| 12 | }); |
| 13 |  |
| 14 | const result = await response.json(); |
| 15 | console.log(result); |
```

## Response with Annotations

Web search responses include citation annotations:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "resp_1234567890", |
| 3 | "object": "response", |
| 4 | "created_at": 1234567890, |
| 5 | "model": "openai/o4-mini", |
| 6 | "output": [ |
| 7 | { |
| 8 | "type": "message", |
| 9 | "id": "msg_abc123", |
| 10 | "status": "completed", |
| 11 | "role": "assistant", |
| 12 | "content": [ |
| 13 | { |
| 14 | "type": "output_text", |
| 15 | "text": "OpenRouter is a unified API for accessing multiple Large Language Model providers through a single interface. It allows developers to access 100+ AI models from providers like OpenAI, Anthropic, Google, and others with intelligent routing and automatic failover.", |
| 16 | "annotations": [ |
| 17 | { |
| 18 | "type": "url_citation", |
| 19 | "url": "https://openrouter.ai/docs", |
| 20 | "start_index": 0, |
| 21 | "end_index": 85 |
| 22 | }, |
| 23 | { |
| 24 | "type": "url_citation", |
| 25 | "url": "https://openrouter.ai/models", |
| 26 | "start_index": 120, |
| 27 | "end_index": 180 |
| 28 | } |
| 29 | ] |
| 30 | } |
| 31 | ] |
| 32 | } |
| 33 | ], |
| 34 | "usage": { |
| 35 | "input_tokens": 15, |
| 36 | "output_tokens": 95, |
| 37 | "total_tokens": 110 |
| 38 | }, |
| 39 | "status": "completed" |
| 40 | } |
```

## Annotation Types

Web search responses can include different annotation types:

### URL Citation

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "url_citation", |
| 3 | "url": "https://example.com/article", |
| 4 | "start_index": 0, |
| 5 | "end_index": 50 |
| 6 | } |
```

## Complex Search Queries

Handle multi-part search queries:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'Compare OpenAI and Anthropic latest models', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | plugins: [{ id: 'web', max_results: 5 }], |
| 22 | max_output_tokens: 9000, |
| 23 | }), |
| 24 | }); |
| 25 |  |
| 26 | const result = await response.json(); |
| 27 | console.log(result); |
```

## Web Search in Conversation

Include web search in multi-turn conversations:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'What is the latest version of React?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | { |
| 21 | type: 'message', |
| 22 | id: 'msg_1', |
| 23 | status: 'in_progress', |
| 24 | role: 'assistant', |
| 25 | content: [ |
| 26 | { |
| 27 | type: 'output_text', |
| 28 | text: 'Let me search for the latest React version.', |
| 29 | annotations: [], |
| 30 | }, |
| 31 | ], |
| 32 | }, |
| 33 | { |
| 34 | type: 'message', |
| 35 | role: 'user', |
| 36 | content: [ |
| 37 | { |
| 38 | type: 'input_text', |
| 39 | text: 'Yes, please find the most recent information', |
| 40 | }, |
| 41 | ], |
| 42 | }, |
| 43 | ], |
| 44 | plugins: [{ id: 'web', max_results: 2 }], |
| 45 | max_output_tokens: 9000, |
| 46 | }), |
| 47 | }); |
| 48 |  |
| 49 | const result = await response.json(); |
| 50 | console.log(result); |
```

## Streaming Web Search

Monitor web search progress with streaming:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: [ |
| 10 | { |
| 11 | type: 'message', |
| 12 | role: 'user', |
| 13 | content: [ |
| 14 | { |
| 15 | type: 'input_text', |
| 16 | text: 'What is the latest news about AI?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | plugins: [{ id: 'web', max_results: 2 }], |
| 22 | stream: true, |
| 23 | max_output_tokens: 9000, |
| 24 | }), |
| 25 | }); |
| 26 |  |
| 27 | const reader = response.body?.getReader(); |
| 28 | const decoder = new TextDecoder(); |
| 29 |  |
| 30 | while (true) { |
| 31 | const { done, value } = await reader.read(); |
| 32 | if (done) break; |
| 33 |  |
| 34 | const chunk = decoder.decode(value); |
| 35 | const lines = chunk.split('\n'); |
| 36 |  |
| 37 | for (const line of lines) { |
| 38 | if (line.startsWith('data: ')) { |
| 39 | const data = line.slice(6); |
| 40 | if (data === '[DONE]') return; |
| 41 |  |
| 42 | try { |
| 43 | const parsed = JSON.parse(data); |
| 44 | if (parsed.type === 'response.output_item.added' && |
| 45 | parsed.item?.type === 'message') { |
| 46 | console.log('Message added'); |
| 47 | } |
| 48 | if (parsed.type === 'response.completed') { |
| 49 | const annotations = parsed.response?.output |
| 50 | ?.find(o => o.type === 'message') |
| 51 | ?.content?.find(c => c.type === 'output_text') |
| 52 | ?.annotations || []; |
| 53 | console.log('Citations:', annotations.length); |
| 54 | } |
| 55 | } catch (e) { |
| 56 | // Skip invalid JSON |
| 57 | } |
| 58 | } |
| 59 | } |
| 60 | } |
```

## Annotation Processing

Extract and process citation information:

```
|  |  |
| --- | --- |
| 1 | function extractCitations(response: any) { |
| 2 | const messageOutput = response.output?.find((o: any) => o.type === 'message'); |
| 3 | const textContent = messageOutput?.content?.find((c: any) => c.type === 'output_text'); |
| 4 | const annotations = textContent?.annotations || []; |
| 5 |  |
| 6 | return annotations |
| 7 | .filter((annotation: any) => annotation.type === 'url_citation') |
| 8 | .map((annotation: any) => ({ |
| 9 | url: annotation.url, |
| 10 | text: textContent.text.slice(annotation.start_index, annotation.end_index), |
| 11 | startIndex: annotation.start_index, |
| 12 | endIndex: annotation.end_index, |
| 13 | })); |
| 14 | } |
| 15 |  |
| 16 | const result = await response.json(); |
| 17 | const citations = extractCitations(result); |
| 18 | console.log('Found citations:', citations); |
```

## Best Practices

1. **Limit results**: Use appropriate `max_results` to balance quality and speed
2. **Handle annotations**: Process citation annotations for proper attribution
3. **Query specificity**: Make search queries specific for better results
4. **Error handling**: Handle cases where web search might fail
5. **Rate limits**: Be mindful of search rate limits

## Next Steps

- Learn about [Tool Calling](../tool-calling/index.md) integration
- Explore [Reasoning](../reasoning/index.md) capabilities
- Review [Basic Usage](../basic-usage/index.md) fundamentals
