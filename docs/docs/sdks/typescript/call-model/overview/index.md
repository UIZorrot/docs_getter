---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/overview"
title: "Call Model Overview (Typescript) | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:49.225917+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](index.md)

# 

Call Model (Typescript)

A unified API for calling any LLM with automatic tool execution and multiple consumption patterns

## Why callModel?

- **Items-Based Model**: Built on OpenRouter’s Responses API with structured
  items (messages, tool calls, reasoning) instead of raw message chunks
- **Multiple Consumption Patterns**: Get text, stream responses, or access
  structured data - all from a single call
- **Automatic Tool Execution**: Define tools with Zod schemas and let the SDK
  handle execution loops
- **Type Safety**: Full TypeScript inference for tool inputs, outputs, and
  events
- **Format Compatibility**: Convert to/from OpenAI chat and Anthropic Claude
  message formats
- **Streaming First**: Built on a reusable stream architecture that supports
  concurrent consumers

## Quick Start

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
| 9 | input: 'What is the capital of France?', |
| 10 | }); |
| 11 |  |
| 12 | // Get text (simplest pattern) |
| 13 | const text = await result.getText(); |
| 14 | console.log(text); // "The capital of France is Paris." |
```

## Consumption Patterns

callModel returns a `ModelResult` object that provides multiple ways to consume
the response:

### Text Methods

```
|  |  |
| --- | --- |
| 1 | // Get just the text content |
| 2 | const text = await result.getText(); |
| 3 |  |
| 4 | // Get the full response with usage data |
| 5 | const response = await result.getResponse(); |
| 6 | console.log(response.usage); // { inputTokens, outputTokens, cachedTokens } |
```

### Streaming Methods

```
|  |  |
| --- | --- |
| 1 | // Stream text deltas |
| 2 | for await (const delta of result.getTextStream()) { |
| 3 | process.stdout.write(delta); |
| 4 | } |
| 5 |  |
| 6 | // Stream reasoning (for reasoning models) |
| 7 | for await (const delta of result.getReasoningStream()) { |
| 8 | console.log('Reasoning:', delta); |
| 9 | } |
| 10 |  |
| 11 | // Stream complete items by ID (recommended) |
| 12 | for await (const item of result.getItemsStream()) { |
| 13 | console.log('Item update:', item.type, item.id); |
| 14 | } |
| 15 |  |
| 16 | // Stream all events (including tool preliminary results) |
| 17 | for await (const event of result.getFullResponsesStream()) { |
| 18 | console.log('Event:', event.type); |
| 19 | } |
```

### Tool Methods

```
|  |  |
| --- | --- |
| 1 | // Get all tool calls from the response |
| 2 | const toolCalls = await result.getToolCalls(); |
| 3 |  |
| 4 | // Stream tool calls as they complete |
| 5 | for await (const toolCall of result.getToolCallsStream()) { |
| 6 | console.log(`Tool: ${toolCall.name}`, toolCall.arguments); |
| 7 | } |
| 8 |  |
| 9 | // Stream tool deltas and preliminary results |
| 10 | for await (const event of result.getToolStream()) { |
| 11 | if (event.type === 'delta') { |
| 12 | process.stdout.write(event.content); |
| 13 | } else if (event.type === 'preliminary_result') { |
| 14 | console.log('Progress:', event.result); |
| 15 | } |
| 16 | } |
```

## Input Formats

callModel accepts multiple input formats:

```
|  |  |
| --- | --- |
| 1 | // Simple string |
| 2 | const result1 = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Hello!', |
| 5 | }); |
| 6 |  |
| 7 | // Message array (OpenResponses format) |
| 8 | const result2 = openrouter.callModel({ |
| 9 | model: 'openai/gpt-5-nano', |
| 10 | input: [ |
| 11 | { role: 'user', content: 'Hello!' }, |
| 12 | ], |
| 13 | }); |
| 14 |  |
| 15 | // With system instructions |
| 16 | const result3 = openrouter.callModel({ |
| 17 | model: 'openai/gpt-5-nano', |
| 18 | instructions: 'You are a helpful assistant.', |
| 19 | input: 'Hello!', |
| 20 | }); |
```

## What’s Next?

Explore the guides to learn more about specific features:

- **[Working with Items](../items/index.md)** - Understand
  the items-based streaming paradigm
- **[Text Generation](../text-generation/index.md)** -
  Input formats, model selection, and response handling
- **[Streaming](../streaming/index.md)** - All streaming
  methods and patterns
- **[Tools](../tools/index.md)** - Creating typed tools
  with Zod schemas and multi-turn orchestration
- **[nextTurnParams](../next-turn-params/index.md)** -
  Tool-driven context injection for skills and plugins
- **[Message Formats](../message-formats/index.md)** -
  Converting to/from OpenAI and Claude formats
- **[Dynamic Parameters](../dynamic-parameters/index.md)**
  - Async functions for adaptive behavior
- **[Stop Conditions](../stop-conditions/index.md)** -
  Intelligent execution control
- **[API Reference](../api-reference/index.md)** - Complete
  type definitions and method signatures

### Example Tools

Ready-to-use tool implementations:

- **[Weather Tool](../examples/weather-tool/index.md)** - Basic API integration
- **[Skills Loader](../examples/skills-loader/index.md)** - Claude Code skills pattern
