---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/streaming"
title: "Streaming | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:10.620520+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Streaming

Stream responses in real-time with multiple consumption patterns. All streams are built on a reusable stream architecture that supports concurrent consumers.

## Text Streaming

### getTextStream()

Stream text content as it’s generated:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/agent'; |
| 2 |  |
| 3 | const openrouter = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY, |
| 5 | }); |
| 6 |  |
| 7 | const result = openrouter.callModel({ |
| 8 | model: 'openai/gpt-5-nano', |
| 9 | input: 'Write a short poem about the ocean.', |
| 10 | }); |
| 11 |  |
| 12 | for await (const delta of result.getTextStream()) { |
| 13 | process.stdout.write(delta); |
| 14 | } |
```

Each iteration yields a small chunk of text (typically a few characters or a word).

## Reasoning Streaming

### getReasoningStream()

For models that support reasoning (like o1 or Claude with thinking), stream the
reasoning process:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/o1-preview', |
| 3 | input: 'Solve this step by step: If x + 5 = 12, what is x?', |
| 4 | }); |
| 5 |  |
| 6 | console.log('Reasoning:'); |
| 7 | for await (const delta of result.getReasoningStream()) { |
| 8 | process.stdout.write(delta); |
| 9 | } |
| 10 |  |
| 11 | console.log('\n\nFinal answer:'); |
| 12 | const text = await result.getText(); |
| 13 | console.log(text); |
```

## Items Streaming

### getItemsStream()

Stream complete items as they update. This is the **recommended way** to handle
streaming when you need structured access to all output types (messages, tool
calls, reasoning, etc.). See
[Working with Items](../items/index.md) for the full
paradigm explanation.

```
|  |  |
| --- | --- |
| 1 | import type { StreamableOutputItem } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4', |
| 5 | input: 'Hello!', |
| 6 | tools: [myTool], |
| 7 | }); |
| 8 |  |
| 9 | for await (const item of result.getItemsStream()) { |
| 10 | switch (item.type) { |
| 11 | case 'message': |
| 12 | console.log('Message:', item.content); |
| 13 | break; |
| 14 | case 'function_call': |
| 15 | console.log('Tool call:', item.name, item.arguments); |
| 16 | break; |
| 17 | case 'reasoning': |
| 18 | console.log('Thinking:', item.summary); |
| 19 | break; |
| 20 | case 'function_call_output': |
| 21 | console.log('Tool result:', item.output); |
| 22 | break; |
| 23 | } |
| 24 | } |
```

**Key insight**: Each iteration yields a **complete item** with the same ID but
updated content. Replace items by ID rather than accumulating deltas.

This stream yields all item types:

| Type | Description |
| --- | --- |
| `message` | Assistant text responses |
| `function_call` | Tool invocations with arguments |
| `reasoning` | Model thinking (extended thinking) |
| `web_search_call` | Web search operations |
| `file_search_call` | File search operations |
| `image_generation_call` | Image generation operations |
| `function_call_output` | Results from executed tools |

## Message Streaming (Deprecated)

### getNewMessagesStream()

##### 

`getNewMessagesStream()` is deprecated. Use `getItemsStream()` instead, which
includes all item types and follows the items-based paradigm.

Stream cumulative message snapshots in the OpenResponses format:

```
|  |  |
| --- | --- |
| 1 | // Deprecated - use getItemsStream() instead |
| 2 | const result = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Hello!', |
| 5 | tools: [myTool], |
| 6 | }); |
| 7 |  |
| 8 | for await (const message of result.getNewMessagesStream()) { |
| 9 | if (message.type === 'message') { |
| 10 | console.log('Assistant message:', message.content); |
| 11 | } else if (message.type === 'function_call_output') { |
| 12 | console.log('Tool result:', message.output); |
| 13 | } |
| 14 | } |
```

This stream yields:

- `ResponsesOutputMessage` - Assistant text/content updates
- `OpenResponsesFunctionCallOutput` - Tool execution results (after tools
  complete)

## Full Event Streaming

### getFullResponsesStream()

Stream all response events including tool preliminary results:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Search for documents', |
| 4 | tools: [searchTool], // Generator tool with eventSchema |
| 5 | }); |
| 6 |  |
| 7 | for await (const event of result.getFullResponsesStream()) { |
| 8 | switch (event.type) { |
| 9 | case 'response.output_text.delta': |
| 10 | process.stdout.write(event.delta); |
| 11 | break; |
| 12 | case 'response.function_call_arguments.delta': |
| 13 | console.log('Tool argument delta:', event.delta); |
| 14 | break; |
| 15 | case 'response.completed': |
| 16 | console.log('Response complete'); |
| 17 | break; |
| 18 | case 'tool.preliminary_result': |
| 19 | // Intermediate progress from generator tools |
| 20 | console.log('Progress:', event.result); |
| 21 | break; |
| 22 | case 'tool.result': |
| 23 | // Final result when tool execution completes |
| 24 | console.log('Tool completed:', event.toolCallId); |
| 25 | console.log('Result:', event.result); |
| 26 | // Access any preliminary results that were emitted |
| 27 | if (event.preliminaryResults) { |
| 28 | console.log('Preliminary results:', event.preliminaryResults); |
| 29 | } |
| 30 | break; |
| 31 | } |
| 32 | } |
```

### Event Types

The full stream includes these event types:

| Event Type | Description |
| --- | --- |
| `response.created` | Response object created |
| `response.in_progress` | Generation started |
| `response.output_text.delta` | Text content chunk |
| `response.output_text.done` | Text content complete |
| `response.reasoning.delta` | Reasoning content chunk |
| `response.reasoning.done` | Reasoning complete |
| `response.function_call_arguments.delta` | Tool call argument chunk |
| `response.function_call_arguments.done` | Tool call arguments complete |
| `response.completed` | Full response complete |
| `tool.preliminary_result` | Progress from generator tools (intermediate yields) |
| `tool.result` | Final result from tool execution |

## Tool Call Streaming

### getToolCallsStream()

Stream structured tool calls as they complete:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather in Paris and Tokyo?', |
| 4 | tools: [weatherTool], |
| 5 | maxToolRounds: 0, // Don't auto-execute, just get tool calls |
| 6 | }); |
| 7 |  |
| 8 | for await (const toolCall of result.getToolCallsStream()) { |
| 9 | console.log(`Tool: ${toolCall.name}`); |
| 10 | console.log(`Arguments:`, toolCall.arguments); |
| 11 | console.log(`ID: ${toolCall.id}`); |
| 12 | } |
```

### getToolStream()

Stream tool deltas and preliminary results:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Search for TypeScript tutorials', |
| 4 | tools: [searchTool], // Generator tool |
| 5 | }); |
| 6 |  |
| 7 | for await (const event of result.getToolStream()) { |
| 8 | if (event.type === 'delta') { |
| 9 | // Raw argument deltas |
| 10 | process.stdout.write(event.content); |
| 11 | } else if (event.type === 'preliminary_result') { |
| 12 | // Progress from generator tools |
| 13 | console.log(`\nProgress (${event.toolCallId}):`, event.result); |
| 14 | } |
| 15 | } |
```

## Concurrent Consumers

Multiple consumers can read from the same result:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Write a story.', |
| 4 | }); |
| 5 |  |
| 6 | // Start both consumers concurrently |
| 7 | const [text, response] = await Promise.all([ |
| 8 | // Consumer 1: Collect text |
| 9 | (async () => { |
| 10 | let text = ''; |
| 11 | for await (const delta of result.getTextStream()) { |
| 12 | text += delta; |
| 13 | } |
| 14 | return text; |
| 15 | })(), |
| 16 |  |
| 17 | // Consumer 2: Get full response |
| 18 | result.getResponse(), |
| 19 | ]); |
| 20 |  |
| 21 | console.log('Text length:', text.length); |
| 22 | console.log('Token usage:', response.usage); |
```

The underlying `ReusableReadableStream` ensures each consumer receives all events.

## Cancellation

Cancel a stream to stop generation:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Write a very long essay...', |
| 4 | }); |
| 5 |  |
| 6 | // Start streaming |
| 7 | const streamPromise = (async () => { |
| 8 | let charCount = 0; |
| 9 | for await (const delta of result.getTextStream()) { |
| 10 | process.stdout.write(delta); |
| 11 | charCount += delta.length; |
| 12 |  |
| 13 | // Cancel after 500 characters |
| 14 | if (charCount > 500) { |
| 15 | await result.cancel(); |
| 16 | break; |
| 17 | } |
| 18 | } |
| 19 | })(); |
| 20 |  |
| 21 | await streamPromise; |
| 22 | console.log('\nCancelled!'); |
```

## Streaming with UI Frameworks

### React Example

```
|  |  |
| --- | --- |
| 1 | import { useState, useEffect } from 'react'; |
| 2 |  |
| 3 | function ChatResponse({ prompt }: { prompt: string }) { |
| 4 | const [text, setText] = useState(''); |
| 5 | const [isStreaming, setIsStreaming] = useState(true); |
| 6 |  |
| 7 | useEffect(() => { |
| 8 | const openrouter = new OpenRouter({ apiKey: API_KEY }); |
| 9 |  |
| 10 | const result = openrouter.callModel({ |
| 11 | model: 'openai/gpt-5-nano', |
| 12 | input: prompt, |
| 13 | }); |
| 14 |  |
| 15 | (async () => { |
| 16 | for await (const delta of result.getTextStream()) { |
| 17 | setText(prev => prev + delta); |
| 18 | } |
| 19 | setIsStreaming(false); |
| 20 | })(); |
| 21 |  |
| 22 | return () => { |
| 23 | result.cancel(); |
| 24 | }; |
| 25 | }, [prompt]); |
| 26 |  |
| 27 | return ( |
| 28 | <div> |
| 29 | <p>{text}</p> |
| 30 | {isStreaming && <span className="cursor">|</span>} |
| 31 | </div> |
| 32 | ); |
| 33 | } |
```

### Server-Sent Events (SSE)

```
|  |  |
| --- | --- |
| 1 | import { Hono } from 'hono'; |
| 2 | import { streamSSE } from 'hono/streaming'; |
| 3 |  |
| 4 | const app = new Hono(); |
| 5 |  |
| 6 | app.get('/stream', (c) => { |
| 7 | return streamSSE(c, async (stream) => { |
| 8 | const result = openrouter.callModel({ |
| 9 | model: 'openai/gpt-5-nano', |
| 10 | input: c.req.query('prompt') || 'Hello!', |
| 11 | }); |
| 12 |  |
| 13 | for await (const delta of result.getTextStream()) { |
| 14 | await stream.writeSSE({ |
| 15 | data: JSON.stringify({ delta }), |
| 16 | event: 'delta', |
| 17 | }); |
| 18 | } |
| 19 |  |
| 20 | await stream.writeSSE({ |
| 21 | data: JSON.stringify({ done: true }), |
| 22 | event: 'done', |
| 23 | }); |
| 24 | }); |
| 25 | }); |
```

## Next Steps

- **[Working with Items](../items/index.md)** - Understand
  the items-based streaming paradigm
- **[Tools](../tools/index.md)** - Create tools and
  multi-turn streaming with tools
