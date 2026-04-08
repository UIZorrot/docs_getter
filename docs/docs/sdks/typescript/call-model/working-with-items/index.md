---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/working-with-items"
title: "Working with Items | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:50.124038+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Working with Items

Understanding the items-based streaming paradigm for callModel

## The Items Paradigm

`callModel` is built on OpenRouter’s Responses API which uses an **items-based
model** rather than the messages-based model used by OpenAI Chat or Vercel AI
SDK.

The key insight: **items are emitted multiple times with the same ID but
progressively updated content**. You replace the entire item by ID rather than
accumulating stream chunks.

## Messages vs Items

| Traditional (OpenAI Chat, Vercel AI) | callModel (Items-native) |
| --- | --- |
| Stream chunks, accumulate text | Stream items, replace by ID |
| Single message type | Multiple item types |
| Reconstruct content at end | Each emission is complete |
| Manual state management | Natural React state updates |

## Item Types

`getItemsStream()` yields these item types:

| Type | Description |
| --- | --- |
| `message` | Assistant text responses |
| `function_call` | Tool invocations with arguments |
| `reasoning` | Model thinking (extended thinking) |
| `web_search_call` | Web search operations |
| `file_search_call` | File search operations |
| `image_generation_call` | Image generation operations |
| `function_call_output` | Results from executed tools |

## How Streaming Works

Each iteration yields a **complete item** with the same ID but updated content:

```
|  |  |
| --- | --- |
| 1 | // Iteration 1 |
| 2 | { |
| 3 | id: "msg_123", |
| 4 | type: "message", |
| 5 | content: [{ type: "output_text", text: "Hello" }] |
| 6 | } |
| 7 |  |
| 8 | // Iteration 2 |
| 9 | { |
| 10 | id: "msg_123", |
| 11 | type: "message", |
| 12 | content: [{ type: "output_text", text: "Hello world" }] |
| 13 | } |
| 14 |  |
| 15 | // Iteration 3 |
| 16 | { |
| 17 | id: "msg_123", |
| 18 | type: "message", |
| 19 | content: [{ type: "output_text", text: "Hello world!" }] |
| 20 | } |
```

The same pattern applies to function calls:

```
|  |  |
| --- | --- |
| 1 | // Iteration 1 |
| 2 | { type: "function_call", callId: "call_456", arguments: "{\"q" } |
| 3 |  |
| 4 | // Iteration 2 |
| 5 | { |
| 6 | type: "function_call", |
| 7 | callId: "call_456", |
| 8 | arguments: "{\"query\": \"weather" |
| 9 | } |
| 10 |  |
| 11 | // Iteration 3 |
| 12 | { |
| 13 | type: "function_call", |
| 14 | callId: "call_456", |
| 15 | arguments: "{\"query\": \"weather in Paris\"}" |
| 16 | } |
```

## React Integration

The items paradigm eliminates manual chunk accumulation. Use a Map keyed by
item ID and let React’s reconciliation handle updates:

```
|  |  |
| --- | --- |
| 1 | import { useState } from 'react'; |
| 2 | import type { StreamableOutputItem } from '@openrouter/agent'; |
| 3 | import { OpenRouter } from '@openrouter/agent'; |
| 4 |  |
| 5 | const client = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY }); |
| 6 |  |
| 7 | function Chat() { |
| 8 | const [items, setItems] = useState<Map<string, StreamableOutputItem>>( |
| 9 | new Map() |
| 10 | ); |
| 11 |  |
| 12 | async function handleSubmit(input: string) { |
| 13 | const result = client.callModel({ |
| 14 | model: 'anthropic/claude-sonnet-4', |
| 15 | input, |
| 16 | }); |
| 17 |  |
| 18 | for await (const item of result.getItemsStream()) { |
| 19 | // Replace the entire item by ID - React re-renders automatically |
| 20 | setItems((prev) => new Map(prev).set(item.id, item)); |
| 21 | } |
| 22 | } |
| 23 |  |
| 24 | return ( |
| 25 | <div> |
| 26 | <form onSubmit={(e) => { e.preventDefault(); handleSubmit(input); }}> |
| 27 | {/* input field */} |
| 28 | </form> |
| 29 | <div> |
| 30 | {[...items.values()].map((item) => ( |
| 31 | <ItemRenderer key={item.id} item={item} /> |
| 32 | ))} |
| 33 | </div> |
| 34 | </div> |
| 35 | ); |
| 36 | } |
| 37 |  |
| 38 | function ItemRenderer({ item }: { item: StreamableOutputItem }) { |
| 39 | switch (item.type) { |
| 40 | case 'message': |
| 41 | return <MessageItem message={item} />; |
| 42 | case 'function_call': |
| 43 | return <ToolCallItem call={item} />; |
| 44 | case 'reasoning': |
| 45 | return <ReasoningItem reasoning={item} />; |
| 46 | default: |
| 47 | return null; |
| 48 | } |
| 49 | } |
```

### Benefits

- **No chunk accumulation** - Each item emission is complete
- **Natural React updates** - Setting state triggers re-render automatically
- **Concurrent item handling** - Function calls and messages stream in parallel
- **Works with React 18+** - Compatible with concurrent features and Suspense
- **Type-safe** - Full TypeScript inference for all item types

## Comparison with Chunk Accumulation

Traditional streaming requires manual accumulation:

```
|  |  |
| --- | --- |
| 1 | // Traditional approach - manual accumulation |
| 2 | const [text, setText] = useState(''); |
| 3 |  |
| 4 | for await (const chunk of result.getTextStream()) { |
| 5 | setText((prev) => prev + chunk); // Must accumulate manually |
| 6 | } |
```

With items, each emission replaces the previous:

```
|  |  |
| --- | --- |
| 1 | // Items approach - replace by ID |
| 2 | for await (const item of result.getItemsStream()) { |
| 3 | setItems((prev) => new Map(prev).set(item.id, item)); // Complete replacement |
| 4 | } |
```

The items approach is especially powerful when the model produces multiple
outputs simultaneously (e.g., thinking + tool calls + text).

## Migrating from getNewMessagesStream()

`getNewMessagesStream()` is deprecated in favor of `getItemsStream()`. The
migration is straightforward:

```
|  |  |
| --- | --- |
| 1 | // Before (deprecated) |
| 2 | for await (const message of result.getNewMessagesStream()) { |
| 3 | if (message.type === 'message') { |
| 4 | console.log(message.content); |
| 5 | } |
| 6 | } |
| 7 |  |
| 8 | // After |
| 9 | for await (const item of result.getItemsStream()) { |
| 10 | if (item.type === 'message') { |
| 11 | console.log(item.content); |
| 12 | } |
| 13 | } |
```

The key difference: `getItemsStream()` includes all item types (reasoning,
function calls, etc.), not just messages.

## Next Steps

- **[Streaming](../streaming/index.md)** - All streaming
  methods including getItemsStream()
- **[Tools](../tools/index.md)** - Creating typed tools
  with Zod schemas
