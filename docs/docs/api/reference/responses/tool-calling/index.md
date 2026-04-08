---
source_url: "https://openrouter.ai/docs/api/reference/responses/tool-calling"
title: "Responses API Beta Tool Calling | Function Calling Integration | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:30.213774+00:00"
---
[API Guides](../../overview/index.md)[Responses API](../overview/index.md)

# Tool Calling

Function calling and tool integration with the Responses API Beta

##### Beta API

This API is in **beta stage** and may have breaking changes.

The Responses API Beta supports comprehensive tool calling capabilities, allowing models to call functions, execute tools in parallel, and handle complex multi-step workflows.

## Basic Tool Definition

Define tools using the OpenAI function calling format:

```
|  |  |
| --- | --- |
| 1 | const weatherTool = { |
| 2 | type: 'function' as const, |
| 3 | name: 'get_weather', |
| 4 | description: 'Get the current weather in a location', |
| 5 | strict: null, |
| 6 | parameters: { |
| 7 | type: 'object', |
| 8 | properties: { |
| 9 | location: { |
| 10 | type: 'string', |
| 11 | description: 'The city and state, e.g. San Francisco, CA', |
| 12 | }, |
| 13 | unit: { |
| 14 | type: 'string', |
| 15 | enum: ['celsius', 'fahrenheit'], |
| 16 | }, |
| 17 | }, |
| 18 | required: ['location'], |
| 19 | }, |
| 20 | }; |
| 21 |  |
| 22 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 23 | method: 'POST', |
| 24 | headers: { |
| 25 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 26 | 'Content-Type': 'application/json', |
| 27 | }, |
| 28 | body: JSON.stringify({ |
| 29 | model: 'openai/o4-mini', |
| 30 | input: [ |
| 31 | { |
| 32 | type: 'message', |
| 33 | role: 'user', |
| 34 | content: [ |
| 35 | { |
| 36 | type: 'input_text', |
| 37 | text: 'What is the weather in San Francisco?', |
| 38 | }, |
| 39 | ], |
| 40 | }, |
| 41 | ], |
| 42 | tools: [weatherTool], |
| 43 | tool_choice: 'auto', |
| 44 | max_output_tokens: 9000, |
| 45 | }), |
| 46 | }); |
| 47 |  |
| 48 | const result = await response.json(); |
| 49 | console.log(result); |
```

## Tool Choice Options

Control when and how tools are called:

| Tool Choice | Description |
| --- | --- |
| `auto` | Model decides whether to call tools |
| `none` | Model will not call any tools |
| `{type: 'function', name: 'tool_name'}` | Force specific tool call |

### Force Specific Tool

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
| 16 | text: 'Hello, how are you?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | tools: [weatherTool], |
| 22 | tool_choice: { type: 'function', name: 'get_weather' }, |
| 23 | max_output_tokens: 9000, |
| 24 | }), |
| 25 | }); |
```

### Disable Tool Calling

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
| 16 | text: 'What is the weather in Paris?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | tools: [weatherTool], |
| 22 | tool_choice: 'none', |
| 23 | max_output_tokens: 9000, |
| 24 | }), |
| 25 | }); |
```

## Multiple Tools

Define multiple tools for complex workflows:

```
|  |  |
| --- | --- |
| 1 | const calculatorTool = { |
| 2 | type: 'function' as const, |
| 3 | name: 'calculate', |
| 4 | description: 'Perform mathematical calculations', |
| 5 | strict: null, |
| 6 | parameters: { |
| 7 | type: 'object', |
| 8 | properties: { |
| 9 | expression: { |
| 10 | type: 'string', |
| 11 | description: 'The mathematical expression to evaluate', |
| 12 | }, |
| 13 | }, |
| 14 | required: ['expression'], |
| 15 | }, |
| 16 | }; |
| 17 |  |
| 18 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 19 | method: 'POST', |
| 20 | headers: { |
| 21 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 22 | 'Content-Type': 'application/json', |
| 23 | }, |
| 24 | body: JSON.stringify({ |
| 25 | model: 'openai/o4-mini', |
| 26 | input: [ |
| 27 | { |
| 28 | type: 'message', |
| 29 | role: 'user', |
| 30 | content: [ |
| 31 | { |
| 32 | type: 'input_text', |
| 33 | text: 'What is 25 * 4?', |
| 34 | }, |
| 35 | ], |
| 36 | }, |
| 37 | ], |
| 38 | tools: [weatherTool, calculatorTool], |
| 39 | tool_choice: 'auto', |
| 40 | max_output_tokens: 9000, |
| 41 | }), |
| 42 | }); |
```

## Parallel Tool Calls

The API supports parallel execution of multiple tools:

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
| 16 | text: 'Calculate 10*5 and also tell me the weather in Miami', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | tools: [weatherTool, calculatorTool], |
| 22 | tool_choice: 'auto', |
| 23 | max_output_tokens: 9000, |
| 24 | }), |
| 25 | }); |
| 26 |  |
| 27 | const result = await response.json(); |
| 28 | console.log(result); |
```

## Tool Call Response

When tools are called, the response includes function call information:

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
| 8 | "type": "function_call", |
| 9 | "id": "fc_abc123", |
| 10 | "call_id": "call_xyz789", |
| 11 | "name": "get_weather", |
| 12 | "arguments": "{\"location\":\"San Francisco, CA\"}" |
| 13 | } |
| 14 | ], |
| 15 | "usage": { |
| 16 | "input_tokens": 45, |
| 17 | "output_tokens": 25, |
| 18 | "total_tokens": 70 |
| 19 | }, |
| 20 | "status": "completed" |
| 21 | } |
```

## Tool Responses in Conversation

Include tool responses in follow-up requests:

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
| 16 | text: 'What is the weather in Boston?', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | { |
| 21 | type: 'function_call', |
| 22 | id: 'fc_1', |
| 23 | call_id: 'call_123', |
| 24 | name: 'get_weather', |
| 25 | arguments: JSON.stringify({ location: 'Boston, MA' }), |
| 26 | }, |
| 27 | { |
| 28 | type: 'function_call_output', |
| 29 | id: 'fc_output_1', |
| 30 | call_id: 'call_123', |
| 31 | output: JSON.stringify({ temperature: '72°F', condition: 'Sunny' }), |
| 32 | }, |
| 33 | { |
| 34 | type: 'message', |
| 35 | role: 'assistant', |
| 36 | id: 'msg_abc123', |
| 37 | status: 'completed', |
| 38 | content: [ |
| 39 | { |
| 40 | type: 'output_text', |
| 41 | text: 'The weather in Boston is currently 72°F and sunny. This looks like perfect weather for a picnic!', |
| 42 | annotations: [] |
| 43 | } |
| 44 | ] |
| 45 | }, |
| 46 | { |
| 47 | type: 'message', |
| 48 | role: 'user', |
| 49 | content: [ |
| 50 | { |
| 51 | type: 'input_text', |
| 52 | text: 'Is that good weather for a picnic?', |
| 53 | }, |
| 54 | ], |
| 55 | }, |
| 56 | ], |
| 57 | max_output_tokens: 9000, |
| 58 | }), |
| 59 | }); |
```

##### Required Field

The `id` field is required for `function_call_output` objects when including tool responses in conversation history.

## Streaming Tool Calls

Monitor tool calls in real-time with streaming:

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
| 16 | text: 'What is the weather like in Tokyo, Japan? Please check the weather.', |
| 17 | }, |
| 18 | ], |
| 19 | }, |
| 20 | ], |
| 21 | tools: [weatherTool], |
| 22 | tool_choice: 'auto', |
| 23 | stream: true, |
| 24 | max_output_tokens: 9000, |
| 25 | }), |
| 26 | }); |
| 27 |  |
| 28 | const reader = response.body?.getReader(); |
| 29 | const decoder = new TextDecoder(); |
| 30 |  |
| 31 | while (true) { |
| 32 | const { done, value } = await reader.read(); |
| 33 | if (done) break; |
| 34 |  |
| 35 | const chunk = decoder.decode(value); |
| 36 | const lines = chunk.split('\n'); |
| 37 |  |
| 38 | for (const line of lines) { |
| 39 | if (line.startsWith('data: ')) { |
| 40 | const data = line.slice(6); |
| 41 | if (data === '[DONE]') return; |
| 42 |  |
| 43 | try { |
| 44 | const parsed = JSON.parse(data); |
| 45 | if (parsed.type === 'response.output_item.added' && |
| 46 | parsed.item?.type === 'function_call') { |
| 47 | console.log('Function call:', parsed.item.name); |
| 48 | } |
| 49 | if (parsed.type === 'response.function_call_arguments.done') { |
| 50 | console.log('Arguments:', parsed.arguments); |
| 51 | } |
| 52 | } catch (e) { |
| 53 | // Skip invalid JSON |
| 54 | } |
| 55 | } |
| 56 | } |
| 57 | } |
```

## Tool Validation

Ensure tool calls have proper structure:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "function_call", |
| 3 | "id": "fc_abc123", |
| 4 | "call_id": "call_xyz789", |
| 5 | "name": "get_weather", |
| 6 | "arguments": "{\"location\":\"Seattle, WA\"}" |
| 7 | } |
```

Required fields:

- `type`: Always “function\_call”
- `id`: Unique identifier for the function call object
- `name`: Function name matching tool definition
- `arguments`: Valid JSON string with function parameters
- `call_id`: Unique identifier for the call

## Best Practices

1. **Clear descriptions**: Provide detailed function descriptions and parameter explanations
2. **Proper schemas**: Use valid JSON Schema for parameters
3. **Error handling**: Handle cases where tools might not be called
4. **Parallel execution**: Design tools to work independently when possible
5. **Conversation flow**: Include tool responses in follow-up requests for context

## Next Steps

- Learn about [Web Search](../web-search/index.md) integration
- Explore [Reasoning](../reasoning/index.md) with tools
- Review [Basic Usage](../basic-usage/index.md) fundamentals
