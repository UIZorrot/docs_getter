---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/message-formats"
title: "Message Formats | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:10.370564+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Message Formats

The OpenRouter SDK provides helper functions to convert between popular message formats. This makes it easy to migrate existing code or integrate with different APIs.

## OpenAI Chat Format

### fromChatMessages()

Convert OpenAI chat-style messages to OpenResponses input:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, fromChatMessages } from '@openrouter/agent'; |
| 2 |  |
| 3 | const openrouter = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY, |
| 5 | }); |
| 6 |  |
| 7 | // OpenAI chat format |
| 8 | const chatMessages = [ |
| 9 | { role: 'system', content: 'You are a helpful assistant.' }, |
| 10 | { role: 'user', content: 'Hello!' }, |
| 11 | { role: 'assistant', content: 'Hi there! How can I help you?' }, |
| 12 | { role: 'user', content: 'What is the weather like?' }, |
| 13 | ]; |
| 14 |  |
| 15 | const result = openrouter.callModel({ |
| 16 | model: 'openai/gpt-5-nano', |
| 17 | input: fromChatMessages(chatMessages), |
| 18 | }); |
| 19 |  |
| 20 | const text = await result.getText(); |
```

### toChatMessage()

Convert an OpenResponses response to chat message format:

```
|  |  |
| --- | --- |
| 1 | import { toChatMessage } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5-nano', |
| 5 | input: 'Hello!', |
| 6 | }); |
| 7 |  |
| 8 | const response = await result.getResponse(); |
| 9 | const chatMessage = toChatMessage(response); |
| 10 |  |
| 11 | // chatMessage is now: { role: 'assistant', content: '...' } |
| 12 | console.log(chatMessage.role);    // 'assistant' |
| 13 | console.log(chatMessage.content); // Response text |
```

### Supported Message Types

| Chat Role | Description |
| --- | --- |
| `system` | System instructions |
| `user` | User messages |
| `assistant` | Assistant responses |
| `developer` | Developer instructions |
| `tool` | Tool response messages |

### Tool Messages

Tool responses are converted to function call outputs:

```
|  |  |
| --- | --- |
| 1 | const chatMessages = [ |
| 2 | { role: 'user', content: 'What is the weather?' }, |
| 3 | { |
| 4 | role: 'assistant', |
| 5 | content: null, |
| 6 | tool_calls: [{ |
| 7 | id: 'call_123', |
| 8 | type: 'function', |
| 9 | function: { name: 'get_weather', arguments: '{"location":"Paris"}' }, |
| 10 | }], |
| 11 | }, |
| 12 | { |
| 13 | role: 'tool', |
| 14 | tool_call_id: 'call_123', |
| 15 | content: '{"temperature": 20}', |
| 16 | }, |
| 17 | ]; |
| 18 |  |
| 19 | const input = fromChatMessages(chatMessages); |
```

## Anthropic Claude Format

### fromClaudeMessages()

Convert Anthropic Claude-style messages to OpenResponses input:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, fromClaudeMessages } from '@openrouter/agent'; |
| 2 |  |
| 3 | // Claude format |
| 4 | const claudeMessages = [ |
| 5 | { role: 'user', content: 'Hello!' }, |
| 6 | { role: 'assistant', content: 'Hi there!' }, |
| 7 | { role: 'user', content: 'Tell me about TypeScript.' }, |
| 8 | ]; |
| 9 |  |
| 10 | const result = openrouter.callModel({ |
| 11 | model: 'anthropic/claude-sonnet-4.5', |
| 12 | input: fromClaudeMessages(claudeMessages), |
| 13 | }); |
```

### toClaudeMessage()

Convert an OpenResponses response to Claude message format:

```
|  |  |
| --- | --- |
| 1 | import { toClaudeMessage } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4.5', |
| 5 | input: 'Hello!', |
| 6 | }); |
| 7 |  |
| 8 | const response = await result.getResponse(); |
| 9 | const claudeMessage = toClaudeMessage(response); |
| 10 |  |
| 11 | // Compatible with Anthropic SDK types |
```

### Content Blocks

Claude’s content block format is supported:

```
|  |  |
| --- | --- |
| 1 | const claudeMessages = [ |
| 2 | { |
| 3 | role: 'user', |
| 4 | content: [ |
| 5 | { type: 'text', text: 'What is in this image?' }, |
| 6 | { |
| 7 | type: 'image', |
| 8 | source: { |
| 9 | type: 'url', |
| 10 | url: 'https://example.com/image.jpg', |
| 11 | }, |
| 12 | }, |
| 13 | ], |
| 14 | }, |
| 15 | ]; |
| 16 |  |
| 17 | const input = fromClaudeMessages(claudeMessages); |
```

### Tool Use Blocks

Claude’s tool use format is converted:

```
|  |  |
| --- | --- |
| 1 | const claudeMessages = [ |
| 2 | { role: 'user', content: 'What is the weather?' }, |
| 3 | { |
| 4 | role: 'assistant', |
| 5 | content: [ |
| 6 | { |
| 7 | type: 'tool_use', |
| 8 | id: 'tool_123', |
| 9 | name: 'get_weather', |
| 10 | input: { location: 'Paris' }, |
| 11 | }, |
| 12 | ], |
| 13 | }, |
| 14 | { |
| 15 | role: 'user', |
| 16 | content: [ |
| 17 | { |
| 18 | type: 'tool_result', |
| 19 | tool_use_id: 'tool_123', |
| 20 | content: '{"temperature": 20}', |
| 21 | }, |
| 22 | ], |
| 23 | }, |
| 24 | ]; |
| 25 |  |
| 26 | const input = fromClaudeMessages(claudeMessages); |
```

### Base64 Images

Both URL and base64 images are supported:

```
|  |  |
| --- | --- |
| 1 | const claudeMessages = [ |
| 2 | { |
| 3 | role: 'user', |
| 4 | content: [ |
| 5 | { type: 'text', text: 'Describe this image.' }, |
| 6 | { |
| 7 | type: 'image', |
| 8 | source: { |
| 9 | type: 'base64', |
| 10 | media_type: 'image/png', |
| 11 | data: 'iVBORw0KGgo...', |
| 12 | }, |
| 13 | }, |
| 14 | ], |
| 15 | }, |
| 16 | ]; |
```

### Limitations

Some Claude features are not preserved in conversion.
e.g. `is_error` flag on tool\_result blocks

These features are Claude-specific and not supported by OpenRouter.

## Migration Examples

### From OpenAI SDK

```
|  |  |
| --- | --- |
| 1 | // Before: OpenAI SDK |
| 2 | import OpenAI from 'openai'; |
| 3 |  |
| 4 | const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY }); |
| 5 | const completion = await openai.chat.completions.create({ |
| 6 | model: 'gpt-4', |
| 7 | messages: [ |
| 8 | { role: 'system', content: 'You are helpful.' }, |
| 9 | { role: 'user', content: 'Hello!' }, |
| 10 | ], |
| 11 | }); |
| 12 |  |
| 13 | // After: OpenRouter SDK |
| 14 | import { OpenRouter, fromChatMessages } from '@openrouter/agent'; |
| 15 |  |
| 16 | const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY }); |
| 17 | const result = openrouter.callModel({ |
| 18 | model: 'openai/gpt-5.2', |
| 19 | input: fromChatMessages([ |
| 20 | { role: 'system', content: 'You are helpful.' }, |
| 21 | { role: 'user', content: 'Hello!' }, |
| 22 | ]), |
| 23 | }); |
| 24 |  |
| 25 | const text = await result.getText(); |
```

### From Anthropic SDK

```
|  |  |
| --- | --- |
| 1 | // Before: Anthropic SDK |
| 2 | import Anthropic from '@anthropic-ai/sdk'; |
| 3 |  |
| 4 | const anthropic = new Anthropic(); |
| 5 | const message = await anthropic.messages.create({ |
| 6 | model: 'claude-sonnet-4-20250514', |
| 7 | max_tokens: 1024, |
| 8 | messages: [ |
| 9 | { role: 'user', content: 'Hello!' }, |
| 10 | ], |
| 11 | }); |
| 12 |  |
| 13 | // After: OpenRouter SDK |
| 14 | import { OpenRouter, fromClaudeMessages } from '@openrouter/agent'; |
| 15 |  |
| 16 | const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY }); |
| 17 | const result = openrouter.callModel({ |
| 18 | model: 'anthropic/claude-sonnet-4.5', |
| 19 | input: fromClaudeMessages([ |
| 20 | { role: 'user', content: 'Hello!' }, |
| 21 | ]), |
| 22 | maxOutputTokens: 1024, |
| 23 | }); |
| 24 |  |
| 25 | const text = await result.getText(); |
```

## Building Conversations

Accumulate messages across multiple calls:

```
|  |  |
| --- | --- |
| 1 | import { fromChatMessages, toChatMessage } from '@openrouter/agent'; |
| 2 |  |
| 3 | // Start with initial message |
| 4 | let messages = [ |
| 5 | { role: 'system', content: 'You are a helpful assistant.' }, |
| 6 | { role: 'user', content: 'Hello!' }, |
| 7 | ]; |
| 8 |  |
| 9 | // First call |
| 10 | let result = openrouter.callModel({ |
| 11 | model: 'openai/gpt-5-nano', |
| 12 | input: fromChatMessages(messages), |
| 13 | }); |
| 14 |  |
| 15 | let response = await result.getResponse(); |
| 16 | let assistantMessage = toChatMessage(response); |
| 17 |  |
| 18 | // Add to history |
| 19 | messages.push(assistantMessage); |
| 20 | messages.push({ role: 'user', content: 'What can you help me with?' }); |
| 21 |  |
| 22 | // Continue conversation |
| 23 | result = openrouter.callModel({ |
| 24 | model: 'openai/gpt-5-nano', |
| 25 | input: fromChatMessages(messages), |
| 26 | }); |
```

## Next Steps

- **[Text Generation](../../../call-model/text-generation/index.md)** - Input formats and parameters
- **[Tools](../../../call-model/tools/index.md)** - Add tool capabilities
- **[Streaming](../../../call-model/streaming/index.md)** - Stream format-converted responses
