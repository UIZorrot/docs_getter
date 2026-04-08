---
source_url: "https://openrouter.ai/docs/api/reference/responses/basic-usage"
title: "Responses API Beta Basic Usage | Simple Text Requests | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:29.812314+00:00"
---
[API Guides](../../overview/index.md)[Responses API](../overview/index.md)

# Basic Usage

Getting started with the Responses API Beta

##### Beta API

This API is in **beta stage** and may have breaking changes.

The Responses API Beta supports both simple string input and structured message arrays, making it easy to get started with basic text generation.

## Simple String Input

The simplest way to use the API is with a string input:

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
| 9 | input: 'What is the meaning of life?', |
| 10 | max_output_tokens: 9000, |
| 11 | }), |
| 12 | }); |
| 13 |  |
| 14 | const result = await response.json(); |
| 15 | console.log(result); |
```

## Structured Message Input

For more complex conversations, use the message array format:

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
| 16 | text: 'Tell me a joke about programming', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | max_output_tokens: 9000, |
| 22 | }), |
| 23 | }); |
| 24 |  |
| 25 | const result = await response.json(); |
```

## Response Format

The API returns a structured response with the generated content:

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
| 15 | "text": "The meaning of life is a philosophical question that has been pondered for centuries...", |
| 16 | "annotations": [] |
| 17 | } |
| 18 | ] |
| 19 | } |
| 20 | ], |
| 21 | "usage": { |
| 22 | "input_tokens": 12, |
| 23 | "output_tokens": 45, |
| 24 | "total_tokens": 57 |
| 25 | }, |
| 26 | "status": "completed" |
| 27 | } |
```

## Streaming Responses

Enable streaming for real-time response generation:

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
| 9 | input: 'Write a short story about AI', |
| 10 | stream: true, |
| 11 | max_output_tokens: 9000, |
| 12 | }), |
| 13 | }); |
| 14 |  |
| 15 | const reader = response.body?.getReader(); |
| 16 | const decoder = new TextDecoder(); |
| 17 |  |
| 18 | while (true) { |
| 19 | const { done, value } = await reader.read(); |
| 20 | if (done) break; |
| 21 |  |
| 22 | const chunk = decoder.decode(value); |
| 23 | const lines = chunk.split('\n'); |
| 24 |  |
| 25 | for (const line of lines) { |
| 26 | if (line.startsWith('data: ')) { |
| 27 | const data = line.slice(6); |
| 28 | if (data === '[DONE]') return; |
| 29 |  |
| 30 | try { |
| 31 | const parsed = JSON.parse(data); |
| 32 | console.log(parsed); |
| 33 | } catch (e) { |
| 34 | // Skip invalid JSON |
| 35 | } |
| 36 | } |
| 37 | } |
| 38 | } |
```

### Example Streaming Output

The streaming response returns Server-Sent Events (SSE) chunks:

```
|  |
| --- |
| data: {"type":"response.created","response":{"id":"resp_1234567890","object":"response","status":"in_progress"}} |
|  |
| data: {"type":"response.output_item.added","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"in_progress","content":[]}} |
|  |
| data: {"type":"response.content_part.added","response_id":"resp_1234567890","output_index":0,"content_index":0,"part":{"type":"output_text","text":""}} |
|  |
| data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":"Once"} |
|  |
| data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" upon"} |
|  |
| data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" a"} |
|  |
| data: {"type":"response.content_part.delta","response_id":"resp_1234567890","output_index":0,"content_index":0,"delta":" time"} |
|  |
| data: {"type":"response.output_item.done","response_id":"resp_1234567890","output_index":0,"item":{"type":"message","id":"msg_abc123","role":"assistant","status":"completed","content":[{"type":"output_text","text":"Once upon a time, in a world where artificial intelligence had become as common as smartphones..."}]}} |
|  |
| data: {"type":"response.done","response":{"id":"resp_1234567890","object":"response","status":"completed","usage":{"input_tokens":12,"output_tokens":45,"total_tokens":57}}} |
|  |
| data: [DONE] |
```

## Common Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `model` | string | **Required.** Model to use (e.g., `openai/o4-mini`) |
| `input` | string or array | **Required.** Text or message array |
| `stream` | boolean | Enable streaming responses (default: false) |
| `max_output_tokens` | integer | Maximum tokens to generate |
| `temperature` | number | Sampling temperature (0-2) |
| `top_p` | number | Nucleus sampling parameter (0-1) |

## Error Handling

Handle common errors gracefully:

```
|  |  |
| --- | --- |
| 1 | try { |
| 2 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 3 | method: 'POST', |
| 4 | headers: { |
| 5 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 6 | 'Content-Type': 'application/json', |
| 7 | }, |
| 8 | body: JSON.stringify({ |
| 9 | model: 'openai/o4-mini', |
| 10 | input: 'Hello, world!', |
| 11 | }), |
| 12 | }); |
| 13 |  |
| 14 | if (!response.ok) { |
| 15 | const error = await response.json(); |
| 16 | console.error('API Error:', error.error.message); |
| 17 | return; |
| 18 | } |
| 19 |  |
| 20 | const result = await response.json(); |
| 21 | console.log(result); |
| 22 | } catch (error) { |
| 23 | console.error('Network Error:', error); |
| 24 | } |
```

## Multiple Turn Conversations

Since the Responses API Beta is stateless, you must include the full conversation history in each request to maintain context:

```
|  |  |
| --- | --- |
| 1 | // First request |
| 2 | const firstResponse = await fetch('https://openrouter.ai/api/v1/responses', { |
| 3 | method: 'POST', |
| 4 | headers: { |
| 5 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 6 | 'Content-Type': 'application/json', |
| 7 | }, |
| 8 | body: JSON.stringify({ |
| 9 | model: 'openai/o4-mini', |
| 10 | input: [ |
| 11 | { |
| 12 | type: 'message', |
| 13 | role: 'user', |
| 14 | content: [ |
| 15 | { |
| 16 | type: 'input_text', |
| 17 | text: 'What is the capital of France?', |
| 18 | }, |
| 19 | ], |
| 20 | }, |
| 21 | ], |
| 22 | max_output_tokens: 9000, |
| 23 | }), |
| 24 | }); |
| 25 |  |
| 26 | const firstResult = await firstResponse.json(); |
| 27 |  |
| 28 | // Second request - include previous conversation |
| 29 | const secondResponse = await fetch('https://openrouter.ai/api/v1/responses', { |
| 30 | method: 'POST', |
| 31 | headers: { |
| 32 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 33 | 'Content-Type': 'application/json', |
| 34 | }, |
| 35 | body: JSON.stringify({ |
| 36 | model: 'openai/o4-mini', |
| 37 | input: [ |
| 38 | { |
| 39 | type: 'message', |
| 40 | role: 'user', |
| 41 | content: [ |
| 42 | { |
| 43 | type: 'input_text', |
| 44 | text: 'What is the capital of France?', |
| 45 | }, |
| 46 | ], |
| 47 | }, |
| 48 | { |
| 49 | type: 'message', |
| 50 | role: 'assistant', |
| 51 | id: 'msg_abc123', |
| 52 | status: 'completed', |
| 53 | content: [ |
| 54 | { |
| 55 | type: 'output_text', |
| 56 | text: 'The capital of France is Paris.', |
| 57 | annotations: [] |
| 58 | } |
| 59 | ] |
| 60 | }, |
| 61 | { |
| 62 | type: 'message', |
| 63 | role: 'user', |
| 64 | content: [ |
| 65 | { |
| 66 | type: 'input_text', |
| 67 | text: 'What is the population of that city?', |
| 68 | }, |
| 69 | ], |
| 70 | }, |
| 71 | ], |
| 72 | max_output_tokens: 9000, |
| 73 | }), |
| 74 | }); |
| 75 |  |
| 76 | const secondResult = await secondResponse.json(); |
```

##### Required Fields

The `id` and `status` fields are required for any `assistant` role messages included in the conversation history.

##### Conversation History

Always include the complete conversation history in each request. The API does not store previous messages, so context must be maintained client-side.

## Next Steps

- Learn about [Reasoning](../reasoning/index.md) capabilities
- Explore [Tool Calling](../tool-calling/index.md) functionality
- Try [Web Search](../web-search/index.md) integration
