---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/text-generation"
title: "Text Generation | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:09.051073+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Text Generation

Generate text with callModel using various input formats and model configurations. Supports multiple consumption patterns including text, streaming, and structured output.

## Basic Usage

The simplest way to generate text:

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
| 9 | input: 'Explain quantum computing in one sentence.', |
| 10 | }); |
| 11 |  |
| 12 | const text = await result.getText(); |
```

## Input Formats

callModel accepts several input formats to match your use case.

### String Input

The simplest format - a single string becomes a user message:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the speed of light?', |
| 4 | }); |
```

### Message Array

For multi-turn conversations, pass an array of messages:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: [ |
| 4 | { role: 'user', content: 'My name is Alice.' }, |
| 5 | { role: 'assistant', content: 'Hello Alice! How can I help you today?' }, |
| 6 | { role: 'user', content: 'What is my name?' }, |
| 7 | ], |
| 8 | }); |
```

### Multimodal

For rich content including images:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5.2', |
| 3 | input: [ |
| 4 | { |
| 5 | type: 'message', |
| 6 | role: 'user', |
| 7 | content: [ |
| 8 | { type: 'input_text', text: 'What is in this image?' }, |
| 9 | { |
| 10 | type: 'input_image', |
| 11 | imageUrl: 'https://example.com/image.jpg', |
| 12 | detail: 'auto', |
| 13 | }, |
| 14 | ], |
| 15 | }, |
| 16 | ], |
| 17 | }); |
```

## System Instructions

Set the model’s behavior with the `instructions` parameter:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | instructions: 'You are a helpful coding assistant. Be concise and provide working code examples.', |
| 4 | input: 'How do I read a file in Node.js?', |
| 5 | }); |
```

## Model Selection

### Single Model

Specify a model by its OpenRouter ID:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'anthropic/claude-sonnet-4.5', |
| 3 | input: 'Hello!', |
| 4 | }); |
```

### Model Fallback

Provide multiple models for automatic fallback:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | models: ['anthropic/claude-sonnet-4.5', 'openai/gpt-5.2', 'google/gemini-pro'], |
| 3 | input: 'Hello!', |
| 4 | }); |
```

The SDK will try each model in order until one succeeds.

## Response Methods

### getText()

Returns just the text content after tool execution completes:

```
|  |  |
| --- | --- |
| 1 | const text = await result.getText(); |
| 2 | console.log(text); // "The speed of light is approximately 299,792 km/s." |
```

### getResponse()

Returns the full response object including usage data:

```
|  |  |
| --- | --- |
| 1 | const response = await result.getResponse(); |
| 2 |  |
| 3 | console.log(response.output);     // Full output array |
| 4 | console.log(response.usage);      // Token usage information |
| 5 |  |
| 6 | // Usage includes: |
| 7 | // - inputTokens: tokens in the prompt |
| 8 | // - outputTokens: tokens generated |
| 9 | // - cachedTokens: tokens served from cache (cost savings) |
```

## Generation Parameters

Control the generation behavior:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Write a creative story.', |
| 4 |  |
| 5 | // Temperature: 0 = deterministic, 2 = very creative |
| 6 | temperature: 0.7, |
| 7 |  |
| 8 | // Maximum tokens to generate |
| 9 | maxOutputTokens: 1000, |
| 10 |  |
| 11 | // Top-p sampling |
| 12 | topP: 0.9, |
| 13 | }); |
```

## Response Format

Request structured output:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'List three programming languages.', |
| 4 | text: { |
| 5 | format: { |
| 6 | type: 'json_object', |
| 7 | }, |
| 8 | }, |
| 9 | }); |
| 10 |  |
| 11 | const text = await result.getText(); |
| 12 | const data = JSON.parse(text); |
```

## Error Handling

Handle common error cases:

```
|  |  |
| --- | --- |
| 1 | try { |
| 2 | const result = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Hello!', |
| 5 | }); |
| 6 |  |
| 7 | const text = await result.getText(); |
| 8 | } catch (error) { |
| 9 | if (error instanceof Error && 'statusCode' in error) { |
| 10 | if (error.statusCode === 401) { |
| 11 | console.error('Invalid API key'); |
| 12 | } else if (error.statusCode === 429) { |
| 13 | console.error('Rate limited - try again later'); |
| 14 | } else if (error.statusCode === 503) { |
| 15 | console.error('Model unavailable'); |
| 16 | } |
| 17 | } else { |
| 18 | console.error('Unexpected error:', error); |
| 19 | } |
| 20 | } |
```

## Concurrent Requests

Each callModel invocation is independent:

```
|  |  |
| --- | --- |
| 1 | const [result1, result2, result3] = await Promise.all([ |
| 2 | openrouter.callModel({ model: 'openai/gpt-5-nano', input: 'Question 1' }).getText(), |
| 3 | openrouter.callModel({ model: 'openai/gpt-5-nano', input: 'Question 2' }).getText(), |
| 4 | openrouter.callModel({ model: 'openai/gpt-5-nano', input: 'Question 3' }).getText(), |
| 5 | ]); |
```

## Next Steps

- **[Streaming](../../../call-model/streaming/index.md)** - Stream responses in real-time
- **[Tools](../../../call-model/tools/index.md)** - Add tool capabilities to your generation
- **[Message Formats](../../../call-model/message-formats/index.md)** - Convert from OpenAI/Claude formats
