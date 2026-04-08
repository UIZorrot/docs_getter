---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/dynamic-parameters"
title: "Dynamic Parameters | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:09.889618+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Dynamic Parameters

Use async functions for adaptive model behavior across turns

## Basic Usage

Any parameter in `callModel` can be a function that computes its value based on conversation context. This enables adaptive behavior - changing models, adjusting temperature, or modifying instructions as the conversation evolves.

Pass a function instead of a static value:

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
| 8 | // Dynamic model selection based on turn count |
| 9 | model: (ctx) => { |
| 10 | return ctx.numberOfTurns > 3 ? 'openai/gpt-5.2' : 'openai/gpt-5-nano'; |
| 11 | }, |
| 12 | input: 'Hello!', |
| 13 | tools: [myTool], |
| 14 | }); |
```

## Function Signature

Parameter functions receive a `TurnContext` and return the parameter value:

```
|  |  |
| --- | --- |
| 1 | type ParameterFunction<T> = (context: TurnContext) => T | Promise<T>; |
```

### TurnContext

| Property | Type | Description |
| --- | --- | --- |
| `numberOfTurns` | `number` | Current turn number (1-indexed) |
| `turnRequest` | `OpenResponsesRequest | undefined` | Current request object containing messages and model settings |
| `toolCall` | `OpenResponsesFunctionToolCall | undefined` | The specific tool call being executed |

## Async Functions

Functions can be async for fetching external data:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 |  |
| 4 | // Fetch user preferences from database |
| 5 | temperature: async (ctx) => { |
| 6 | const prefs = await fetchUserPreferences(userId); |
| 7 | return prefs.preferredTemperature ?? 0.7; |
| 8 | }, |
| 9 |  |
| 10 | // Load dynamic instructions |
| 11 | instructions: async (ctx) => { |
| 12 | const rules = await fetchBusinessRules(); |
| 13 | return `Follow these rules:\n${rules.join('\n')}`; |
| 14 | }, |
| 15 |  |
| 16 | input: 'Hello!', |
| 17 | }); |
```

## Common Patterns

### Progressive Model Upgrade

Start with a fast model, upgrade for complex tasks:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: (ctx) => { |
| 3 | // First few turns: fast model |
| 4 | if (ctx.numberOfTurns <= 2) { |
| 5 | return 'openai/gpt-5-nano'; |
| 6 | } |
| 7 |  |
| 8 | // Complex conversations: capable model |
| 9 | return 'openai/gpt-5.2'; |
| 10 | }, |
| 11 | input: 'Let me think through this problem...', |
| 12 | tools: [analysisTool], |
| 13 | }); |
```

### Adaptive Temperature

Adjust creativity based on context:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | temperature: (ctx) => { |
| 4 | // Analyze recent messages for task type |
| 5 | const lastMessage = JSON.stringify(ctx.turnRequest?.input).toLowerCase(); |
| 6 |  |
| 7 | if (lastMessage.includes('creative') || lastMessage.includes('brainstorm')) { |
| 8 | return 1.0; // Creative tasks |
| 9 | } |
| 10 | if (lastMessage.includes('code') || lastMessage.includes('calculate')) { |
| 11 | return 0.2; // Precise tasks |
| 12 | } |
| 13 | return 0.7; // Default |
| 14 | }, |
| 15 | input: 'Write a creative story', |
| 16 | }); |
```

### Context-Aware Instructions

Build instructions based on conversation state:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | instructions: (ctx) => { |
| 4 | const base = 'You are a helpful assistant.'; |
| 5 | const turnInfo = `This is turn ${ctx.numberOfTurns} of the conversation.`; |
| 6 |  |
| 7 | // Add context based on history length |
| 8 | if (ctx.numberOfTurns > 5) { |
| 9 | return `${base}\n${turnInfo}\nKeep responses concise - this is a long conversation.`; |
| 10 | } |
| 11 |  |
| 12 | return `${base}\n${turnInfo}`; |
| 13 | }, |
| 14 | input: 'Continue helping me...', |
| 15 | tools: [helpTool], |
| 16 | }); |
```

### Dynamic Max Tokens

Adjust output length based on task:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | maxOutputTokens: (ctx) => { |
| 4 | const lastMessage = JSON.stringify(ctx.turnRequest?.input).toLowerCase(); |
| 5 |  |
| 6 | if (lastMessage.includes('summarize') || lastMessage.includes('brief')) { |
| 7 | return 200; |
| 8 | } |
| 9 | if (lastMessage.includes('detailed') || lastMessage.includes('explain')) { |
| 10 | return 2000; |
| 11 | } |
| 12 | return 500; |
| 13 | }, |
| 14 | input: 'Give me a detailed explanation', |
| 15 | }); |
```

### Feature Flags

Enable features dynamically:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'anthropic/claude-sonnet-4.5', |
| 3 |  |
| 4 | // Enable thinking for complex turns |
| 5 | provider: async (ctx) => { |
| 6 | const enableThinking = ctx.numberOfTurns > 2; |
| 7 |  |
| 8 | return enableThinking ? { |
| 9 | anthropic: { |
| 10 | thinking: { type: 'enabled', budgetTokens: 1000 }, |
| 11 | }, |
| 12 | } : undefined; |
| 13 | }, |
| 14 |  |
| 15 | input: 'Solve this complex problem', |
| 16 | tools: [analysisTool], |
| 17 | }); |
```

## Combining with Tools

Dynamic parameters work alongside tool execution:

```
|  |  |
| --- | --- |
| 1 | const smartAssistant = openrouter.callModel({ |
| 2 | // Upgrade model if tools have been used |
| 3 | model: (ctx) => { |
| 4 | const hasToolUse = JSON.stringify(ctx.turnRequest?.input).includes('function_call'); |
| 5 | return hasToolUse ? 'anthropic/claude-sonnet-4.5' : 'openai/gpt-5-nano'; |
| 6 | }, |
| 7 |  |
| 8 | // Lower temperature after tool execution |
| 9 | temperature: (ctx) => { |
| 10 | return ctx.numberOfTurns > 1 ? 0.3 : 0.7; |
| 11 | }, |
| 12 |  |
| 13 | input: 'Research and analyze this topic', |
| 14 | tools: [searchTool, analysisTool], |
| 15 | }); |
```

## Execution Order

Dynamic parameters are resolved at the start of each turn:

```
|  |
| --- |
| 1. Resolve all parameter functions with current TurnContext |
| 2. Build request with resolved values |
| 3. Send to model |
| 4. Execute tools (if any) |
| 5. Check stop conditions |
| 6. Update TurnContext for next turn |
| 7. Repeat from step 1 |
```

## Error Handling

Handle errors in async parameter functions:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 |  |
| 4 | instructions: async (ctx) => { |
| 5 | try { |
| 6 | const rules = await fetchRules(); |
| 7 | return `Follow these rules: ${rules}`; |
| 8 | } catch (error) { |
| 9 | // Fallback on error |
| 10 | console.error('Failed to fetch rules:', error); |
| 11 | return 'You are a helpful assistant.'; |
| 12 | } |
| 13 | }, |
| 14 |  |
| 15 | input: 'Hello!', |
| 16 | }); |
```

## Best Practices

### Keep Functions Pure

Avoid side effects in parameter functions:

```
|  |  |
| --- | --- |
| 1 | // Good: Pure function |
| 2 | model: (ctx) => ctx.numberOfTurns > 3 ? 'gpt-4' : 'gpt-4o-mini', |
| 3 |  |
| 4 | // Avoid: Side effects |
| 5 | model: (ctx) => { |
| 6 | logToDatabase(ctx); // Side effect |
| 7 | return 'gpt-4'; |
| 8 | }, |
```

### Cache Expensive Operations

Cache results for repeated calls:

```
|  |  |
| --- | --- |
| 1 | let cachedRules: string | null = null; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | instructions: async (ctx) => { |
| 5 | if (!cachedRules) { |
| 6 | cachedRules = await fetchExpensiveRules(); |
| 7 | } |
| 8 | return cachedRules; |
| 9 | }, |
| 10 | input: 'Hello!', |
| 11 | }); |
```

### Use Sensible Defaults

Always have fallback values:

```
|  |  |
| --- | --- |
| 1 | model: (ctx) => { |
| 2 | const preferredModel = getPreferredModel(); |
| 3 | return preferredModel ?? 'openai/gpt-5-nano'; // Default fallback |
| 4 | }, |
```

## See Also

- **[nextTurnParams](../../../call-model/next-turn-params/index.md)** - Tool-driven parameter modification
- **[Stop Conditions](../../../call-model/stop-conditions/index.md)** - Dynamic execution control
- **[Tools](../../../call-model/tools/index.md)** - Multi-turn orchestration
