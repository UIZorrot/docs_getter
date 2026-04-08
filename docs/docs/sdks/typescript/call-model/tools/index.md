---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/tools"
title: "Tools | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:08.910468+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Tools

Create type-safe tools with Zod schemas and automatic execution. Supports regular tools, generator tools with progress, manual tools, and automatic multi-turn execution.

## The tool() Helper

The `tool()` function creates type-safe tools with Zod schema validation:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool } from '@openrouter/agent'; |
| 2 | import { z } from 'zod'; |
| 3 |  |
| 4 | const weatherTool = tool({ |
| 5 | name: 'get_weather', |
| 6 | description: 'Get the current weather for a location', |
| 7 | inputSchema: z.object({ |
| 8 | location: z.string().describe('City name, e.g., "San Francisco, CA"'), |
| 9 | }), |
| 10 | outputSchema: z.object({ |
| 11 | temperature: z.number(), |
| 12 | conditions: z.string(), |
| 13 | }), |
| 14 | execute: async (params) => { |
| 15 | // params is typed as { location: string } |
| 16 | const weather = await fetchWeather(params.location); |
| 17 | return { |
| 18 | temperature: weather.temp, |
| 19 | conditions: weather.description, |
| 20 | }; |
| 21 | }, |
| 22 | }); |
```

## Tool Types

The SDK supports three types of tools, automatically detected from your configuration:

### Regular Tools

Standard tools with an execute function:

```
|  |  |
| --- | --- |
| 1 | const calculatorTool = tool({ |
| 2 | name: 'calculate', |
| 3 | description: 'Perform a mathematical calculation', |
| 4 | inputSchema: z.object({ |
| 5 | expression: z.string().describe('Math expression like "2 + 2"'), |
| 6 | }), |
| 7 | outputSchema: z.object({ |
| 8 | result: z.number(), |
| 9 | }), |
| 10 | execute: async (params) => { |
| 11 | const result = eval(params.expression); // Use a safer eval in production |
| 12 | return { result }; |
| 13 | }, |
| 14 | }); |
```

### Generator Tools

Tools that yield progress updates during execution. Add `eventSchema` to enable generator mode:

```
|  |  |
| --- | --- |
| 1 | const searchTool = tool({ |
| 2 | name: 'search_database', |
| 3 | description: 'Search documents with progress updates', |
| 4 | inputSchema: z.object({ |
| 5 | query: z.string(), |
| 6 | limit: z.number().default(10), |
| 7 | }), |
| 8 | // eventSchema triggers generator mode |
| 9 | eventSchema: z.object({ |
| 10 | progress: z.number().min(0).max(100), |
| 11 | message: z.string(), |
| 12 | }), |
| 13 | outputSchema: z.object({ |
| 14 | results: z.array(z.string()), |
| 15 | totalFound: z.number(), |
| 16 | }), |
| 17 | // execute is now an async generator |
| 18 | execute: async function* (params) { |
| 19 | yield { progress: 0, message: 'Starting search...' }; |
| 20 |  |
| 21 | const results = []; |
| 22 | for (let i = 0; i < 5; i++) { |
| 23 | yield { progress: (i + 1) * 20, message: `Searching batch ${i + 1}...` }; |
| 24 | results.push(...await searchBatch(params.query, i)); |
| 25 | } |
| 26 |  |
| 27 | // Final yield is the output |
| 28 | yield { progress: 100, message: 'Complete!' }; |
| 29 |  |
| 30 | // Return the final result (or yield it as last value) |
| 31 | return { |
| 32 | results: results.slice(0, params.limit), |
| 33 | totalFound: results.length, |
| 34 | }; |
| 35 | }, |
| 36 | }); |
```

Progress events are streamed to consumers via `getToolStream()` and `getFullResponsesStream()`.

### Manual Tools

Tools without automatic execution - you handle the tool calls yourself:

```
|  |  |
| --- | --- |
| 1 | const manualTool = tool({ |
| 2 | name: 'send_email', |
| 3 | description: 'Send an email (requires user confirmation)', |
| 4 | inputSchema: z.object({ |
| 5 | to: z.string().email(), |
| 6 | subject: z.string(), |
| 7 | body: z.string(), |
| 8 | }), |
| 9 | execute: false, // Manual handling required |
| 10 | }); |
```

Use `getToolCalls()` to retrieve manual tool calls for processing.

## Schema Definition

### Input Schema

Define what parameters the tool accepts:

```
|  |  |
| --- | --- |
| 1 | const inputSchema = z.object({ |
| 2 | // Required parameters |
| 3 | query: z.string().describe('Search query'), |
| 4 |  |
| 5 | // Optional with default |
| 6 | limit: z.number().default(10).describe('Max results'), |
| 7 |  |
| 8 | // Optional without default |
| 9 | filter: z.string().optional().describe('Filter expression'), |
| 10 |  |
| 11 | // Enum values |
| 12 | sortBy: z.enum(['relevance', 'date', 'popularity']).default('relevance'), |
| 13 |  |
| 14 | // Nested objects |
| 15 | options: z.object({ |
| 16 | caseSensitive: z.boolean().default(false), |
| 17 | wholeWord: z.boolean().default(false), |
| 18 | }).optional(), |
| 19 |  |
| 20 | // Arrays |
| 21 | tags: z.array(z.string()).optional(), |
| 22 | }); |
```

### Output Schema

Define the structure of results returned to the model:

```
|  |  |
| --- | --- |
| 1 | const outputSchema = z.object({ |
| 2 | results: z.array(z.object({ |
| 3 | id: z.string(), |
| 4 | title: z.string(), |
| 5 | score: z.number(), |
| 6 | })), |
| 7 | metadata: z.object({ |
| 8 | totalCount: z.number(), |
| 9 | searchTimeMs: z.number(), |
| 10 | }), |
| 11 | }); |
```

### Event Schema (Generator Tools)

Define progress/status events for generator tools:

```
|  |  |
| --- | --- |
| 1 | const eventSchema = z.object({ |
| 2 | stage: z.enum(['initializing', 'processing', 'finalizing']), |
| 3 | progress: z.number(), |
| 4 | currentItem: z.string().optional(), |
| 5 | }); |
```

## Type Inference

The SDK provides utilities to extract types from tools:

```
|  |  |
| --- | --- |
| 1 | import type { InferToolInput, InferToolOutput, InferToolEvent } from '@openrouter/agent'; |
| 2 |  |
| 3 | // Get the input type |
| 4 | type WeatherInput = InferToolInput<typeof weatherTool>; |
| 5 | // { location: string } |
| 6 |  |
| 7 | // Get the output type |
| 8 | type WeatherOutput = InferToolOutput<typeof weatherTool>; |
| 9 | // { temperature: number; conditions: string } |
| 10 |  |
| 11 | // Get event type (generator tools only) |
| 12 | type SearchEvent = InferToolEvent<typeof searchTool>; |
| 13 | // { progress: number; message: string } |
```

## Using Tools with callModel

### Single Tool

```
|  |  |
| --- | --- |
| 1 | const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY }); |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5-nano', |
| 5 | input: 'What is the weather in Tokyo?', |
| 6 | tools: [weatherTool], |
| 7 | }); |
| 8 |  |
| 9 | // Tools are automatically executed |
| 10 | const text = await result.getText(); |
| 11 | // "The weather in Tokyo is 22°C and sunny." |
```

### Multiple Tools

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Search for TypeScript tutorials and calculate 2+2', |
| 4 | tools: [searchTool, calculatorTool], |
| 5 | }); |
```

### Type-Safe Tool Calls with `as const`

Use `as const` for full type inference on tool calls:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather?', |
| 4 | tools: [weatherTool, searchTool] as const, |
| 5 | maxToolRounds: 0, // Get tool calls without executing |
| 6 | }); |
| 7 |  |
| 8 | // Tool calls are typed as union of tool inputs |
| 9 | for await (const toolCall of result.getToolCallsStream()) { |
| 10 | if (toolCall.name === 'get_weather') { |
| 11 | // toolCall.arguments is typed as { location: string } |
| 12 | console.log('Weather for:', toolCall.arguments.location); |
| 13 | } |
| 14 | } |
```

## Execute Context

Tool execute functions receive a flat context object as
their second argument. It merges `TurnContext` fields
with a `tools` map and a `setContext()` method:

```
|  |  |
| --- | --- |
| 1 | const contextAwareTool = tool({ |
| 2 | name: 'context_tool', |
| 3 | inputSchema: z.object({ data: z.string() }), |
| 4 | outputSchema: z.object({ result: z.string() }), |
| 5 | execute: async (params, context) => { |
| 6 | // TurnContext fields are available directly |
| 7 | console.log('Turn:', context.numberOfTurns); |
| 8 | console.log('History:', context.turnRequest?.input); |
| 9 | console.log('Model:', context.turnRequest?.model); |
| 10 |  |
| 11 | return { |
| 12 | result: `Processed on turn ${context.numberOfTurns}`, |
| 13 | }; |
| 14 | }, |
| 15 | }); |
```

### Context Properties

| Property | Type | Description |
| --- | --- | --- |
| `numberOfTurns` | `number` | Current turn number (1-indexed) |
| `turnRequest` | `OpenResponsesRequest | undefined` | Current request object |
| `toolCall` | `OpenResponsesFunctionToolCall | undefined` | The tool call being executed |
| `local` | `Readonly<TContext>` | This tool’s own context (read-only) |
| `setContext` | `(partial: Partial<TContext>) => void` | Mutate this tool’s context |
| `shared` | `Readonly<TShared>` | Shared context visible to all tools |
| `setSharedContext` | `(partial: Partial<TShared>) => void` | Mutate shared context |

## Tool Context

Tools can declare a `contextSchema` to receive typed,
persistent context data from the caller. Context is
keyed by tool name and persists across turns.

### Declaring contextSchema

```
|  |  |
| --- | --- |
| 1 | const weatherTool = tool({ |
| 2 | name: 'get_weather', |
| 3 | description: 'Get weather for a location', |
| 4 | inputSchema: z.object({ |
| 5 | location: z.string(), |
| 6 | }), |
| 7 | outputSchema: z.object({ |
| 8 | temperature: z.number(), |
| 9 | }), |
| 10 | // Declare what context this tool needs |
| 11 | contextSchema: z.object({ |
| 12 | apiKey: z.string(), |
| 13 | units: z.enum(['celsius', 'fahrenheit']), |
| 14 | }), |
| 15 | execute: async (params, context) => { |
| 16 | // Access this tool's own context via local |
| 17 | const { apiKey, units } = context.local; |
| 18 |  |
| 19 | const weather = await fetchWeather( |
| 20 | params.location, |
| 21 | apiKey, |
| 22 | units, |
| 23 | ); |
| 24 | return { temperature: weather.temp }; |
| 25 | }, |
| 26 | }); |
```

### Providing Context in callModel

Pass context keyed by tool name:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather in Tokyo?', |
| 4 | tools: [weatherTool, dbTool] as const, |
| 5 |  |
| 6 | // Static context — keyed by tool name |
| 7 | context: { |
| 8 | get_weather: { apiKey: 'sk-...', units: 'celsius' }, |
| 9 | db_query: { connectionString: 'postgres://...' }, |
| 10 | }, |
| 11 | }); |
```

### Dynamic Context

Use an async function for one-time initialization
that needs to fetch data:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather?', |
| 4 | tools: [weatherTool] as const, |
| 5 |  |
| 6 | // Resolved once at turn 0 to seed the store |
| 7 | context: async () => ({ |
| 8 | get_weather: { |
| 9 | apiKey: await fetchApiKey(), |
| 10 | units: 'celsius', |
| 11 | }, |
| 12 | }), |
| 13 | }); |
```

##### 

`resolveContext` runs once at turn 0 to seed the
context store. For per-turn mutations, use
`setContext()` inside your tool’s `execute` function.

### Mutating Context with setContext

Tools can update their own context using `setContext()`.
Changes persist across turns via the shared store and
are visible immediately — `context.local` is a live
getter that always reads the latest values:

```
|  |  |
| --- | --- |
| 1 | const authTool = tool({ |
| 2 | name: 'auth', |
| 3 | inputSchema: z.object({ action: z.string() }), |
| 4 | contextSchema: z.object({ |
| 5 | token: z.string(), |
| 6 | refreshCount: z.number(), |
| 7 | }), |
| 8 | execute: async (params, context) => { |
| 9 | const { token } = context.local; |
| 10 |  |
| 11 | if (isExpired(token)) { |
| 12 | const newToken = await refreshToken(token); |
| 13 | // Mutate own context — persists to next turn |
| 14 | context.setContext({ |
| 15 | token: newToken, |
| 16 | refreshCount: |
| 17 | context.local.refreshCount + 1, |
| 18 | }); |
| 19 | } |
| 20 |  |
| 21 | return { success: true }; |
| 22 | }, |
| 23 | }); |
```

### Observing Context Changes

Use `getContextUpdates()` on `ModelResult` to observe
context mutations in real time:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Authenticate and fetch data', |
| 4 | tools: [authTool] as const, |
| 5 | context: { |
| 6 | auth: { token: 'initial', refreshCount: 0 }, |
| 7 | }, |
| 8 | }); |
| 9 |  |
| 10 | for await (const snapshot of result.getContextUpdates()) { |
| 11 | console.log('Context changed:', snapshot); |
| 12 | // { auth: { token: 'new-token', refreshCount: 1 } } |
| 13 | } |
```

### Shared Context

Use `sharedSchema` on `tool()` and `sharedContextSchema`
on `callModel` to share typed state across tools:

```
|  |  |
| --- | --- |
| 1 | const SharedContextSchema = z.object({ |
| 2 | _sessionId: z.string().optional(), |
| 3 | }); |
| 4 |  |
| 5 | const execTool = tool({ |
| 6 | name: 'sandbox_exec', |
| 7 | inputSchema: z.object({ command: z.string() }), |
| 8 | sharedSchema: SharedContextSchema, |
| 9 | execute: async (input, ctx) => { |
| 10 | // Read shared state set by any tool |
| 11 | const sid = ctx.shared._sessionId; |
| 12 | const session = await connect(sid); |
| 13 | // Write shared state for other tools |
| 14 | ctx.setSharedContext({ _sessionId: session.id }); |
| 15 | return await session.exec(input.command); |
| 16 | }, |
| 17 | }); |
| 18 |  |
| 19 | const result = openrouter.callModel({ |
| 20 | model: 'openai/gpt-5-nano', |
| 21 | input: 'Run a command', |
| 22 | tools: [execTool] as const, |
| 23 | sharedContextSchema: SharedContextSchema, |
| 24 | context: { |
| 25 | shared: { _sessionId: 'existing-session' }, |
| 26 | sandbox_exec: {}, |
| 27 | }, |
| 28 | }); |
```

##### 

`context.local` is scoped to one tool.
`context.shared` is visible to all tools and persists
across turns. Pass the same `sharedSchema` to each tool
for typed access, and `sharedContextSchema` to
`callModel` for runtime validation.

## Tool Execution

callModel automatically executes tools and handles multi-turn conversations. When the model calls a tool, the SDK executes it, sends the result back, and continues until the model provides a final response.

### Automatic Execution Flow

When you provide tools with execute functions:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool } from '@openrouter/agent'; |
| 2 | import { z } from 'zod'; |
| 3 |  |
| 4 | const weatherTool = tool({ |
| 5 | name: 'get_weather', |
| 6 | inputSchema: z.object({ location: z.string() }), |
| 7 | outputSchema: z.object({ temperature: z.number() }), |
| 8 | execute: async ({ location }) => { |
| 9 | return { temperature: await fetchTemperature(location) }; |
| 10 | }, |
| 11 | }); |
| 12 |  |
| 13 | const result = openrouter.callModel({ |
| 14 | model: 'openai/gpt-5-nano', |
| 15 | input: 'What is the weather in Paris?', |
| 16 | tools: [weatherTool], |
| 17 | }); |
| 18 |  |
| 19 | // getText() waits for all tool execution to complete |
| 20 | const text = await result.getText(); |
| 21 | // "The weather in Paris is 18°C." |
```

### Execution Sequence

1. Model receives prompt and generates tool call
2. SDK extracts tool call and validates arguments
3. Tool’s execute function runs
4. Result is formatted and sent back to model
5. Model generates final response (or more tool calls)
6. Process repeats until model is done

### Controlling Execution Rounds

#### maxToolRounds (Number)

Limit the maximum number of tool execution rounds:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Research this topic thoroughly', |
| 4 | tools: [searchTool, analyzeTool], |
| 5 | maxToolRounds: 3, // Stop after 3 rounds of tool execution |
| 6 | }); |
```

Setting `maxToolRounds: 0` disables automatic execution - you get raw tool calls.

#### maxToolRounds (Function)

Use a function for dynamic control:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Research and analyze', |
| 4 | tools: [searchTool], |
| 5 | maxToolRounds: (context) => { |
| 6 | // Continue if under 5 turns |
| 7 | return context.numberOfTurns < 5; |
| 8 | }, |
| 9 | }); |
```

The function receives `TurnContext` and returns `true` to continue or `false` to stop.

### Accessing Tool Calls

#### getToolCalls()

Get all tool calls from the initial response (before auto-execution):

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather in Tokyo and Paris?', |
| 4 | tools: [weatherTool], |
| 5 | maxToolRounds: 0, // Don't auto-execute |
| 6 | }); |
| 7 |  |
| 8 | const toolCalls = await result.getToolCalls(); |
| 9 |  |
| 10 | for (const call of toolCalls) { |
| 11 | console.log(`Tool: ${call.name}`); |
| 12 | console.log(`ID: ${call.id}`); |
| 13 | console.log(`Arguments:`, call.arguments); |
| 14 | } |
```

#### getToolCallsStream()

Stream tool calls as they complete:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Check weather in multiple cities', |
| 4 | tools: [weatherTool], |
| 5 | maxToolRounds: 0, |
| 6 | }); |
| 7 |  |
| 8 | for await (const toolCall of result.getToolCallsStream()) { |
| 9 | console.log(`Received tool call: ${toolCall.name}`); |
| 10 |  |
| 11 | // Process each tool call as it arrives |
| 12 | const weatherResult = await processWeatherRequest(toolCall.arguments); |
| 13 | console.log('Result:', weatherResult); |
| 14 | } |
```

### Tool Stream Events

#### getToolStream()

Stream both argument deltas and preliminary results:

```
|  |  |
| --- | --- |
| 1 | const searchTool = tool({ |
| 2 | name: 'search', |
| 3 | inputSchema: z.object({ query: z.string() }), |
| 4 | eventSchema: z.object({ progress: z.number(), status: z.string() }), |
| 5 | outputSchema: z.object({ results: z.array(z.string()) }), |
| 6 | execute: async function* ({ query }) { |
| 7 | yield { progress: 25, status: 'Searching...' }; |
| 8 | yield { progress: 50, status: 'Processing...' }; |
| 9 | yield { progress: 75, status: 'Ranking...' }; |
| 10 | yield { progress: 100, status: 'Complete' }; |
| 11 | return { results: ['result1', 'result2'] }; |
| 12 | }, |
| 13 | }); |
| 14 |  |
| 15 | const result = openrouter.callModel({ |
| 16 | model: 'openai/gpt-5-nano', |
| 17 | input: 'Search for TypeScript tutorials', |
| 18 | tools: [searchTool], |
| 19 | }); |
| 20 |  |
| 21 | for await (const event of result.getToolStream()) { |
| 22 | switch (event.type) { |
| 23 | case 'delta': |
| 24 | // Raw argument delta from the model |
| 25 | process.stdout.write(event.content); |
| 26 | break; |
| 27 | case 'preliminary_result': |
| 28 | // Progress from generator tool |
| 29 | console.log(`Progress: ${event.result.progress}% - ${event.result.status}`); |
| 30 | break; |
| 31 | } |
| 32 | } |
```

#### Event Types

| Type | Description |
| --- | --- |
| `delta` | Raw tool call argument chunks from model |
| `preliminary_result` | Progress events from generator tools (intermediate yields) |

### Tool Result Events

When using `getFullResponsesStream()`, you can also receive `tool.result` events that fire when a tool execution completes:

```
|  |  |
| --- | --- |
| 1 | for await (const event of result.getFullResponsesStream()) { |
| 2 | switch (event.type) { |
| 3 | case 'tool.preliminary_result': |
| 4 | // Intermediate progress from generator tools |
| 5 | console.log(`Progress (${event.toolCallId}):`, event.result); |
| 6 | break; |
| 7 | case 'tool.result': |
| 8 | // Final result when tool execution completes |
| 9 | console.log(`Tool ${event.toolCallId} completed`); |
| 10 | console.log('Result:', event.result); |
| 11 | // Access any preliminary results that were emitted during execution |
| 12 | if (event.preliminaryResults) { |
| 13 | console.log('All progress events:', event.preliminaryResults); |
| 14 | } |
| 15 | break; |
| 16 | } |
| 17 | } |
```

#### ToolResultEvent Type

```
|  |  |
| --- | --- |
| 1 | type ToolResultEvent<TResult = unknown, TPreliminaryResults = unknown> = { |
| 2 | type: 'tool.result'; |
| 3 | toolCallId: string; |
| 4 | result: TResult; |
| 5 | timestamp: number; |
| 6 | preliminaryResults?: TPreliminaryResults[]; |
| 7 | }; |
```

The `tool.result` event provides the final output from tool execution along with all intermediate `preliminaryResults` that were yielded during execution (for generator tools). This is useful when you need both real-time progress updates and a summary of all progress at completion.

### Parallel Tool Execution

When the model calls multiple tools, they execute in parallel:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Get weather in Paris, Tokyo, and New York simultaneously', |
| 4 | tools: [weatherTool], |
| 5 | }); |
| 6 |  |
| 7 | // All three weather calls execute in parallel |
| 8 | const text = await result.getText(); |
```

### Manual Tool Handling

For tools without execute functions:

```
|  |  |
| --- | --- |
| 1 | const confirmTool = tool({ |
| 2 | name: 'send_email', |
| 3 | description: 'Send an email (requires confirmation)', |
| 4 | inputSchema: z.object({ |
| 5 | to: z.string().email(), |
| 6 | subject: z.string(), |
| 7 | body: z.string(), |
| 8 | }), |
| 9 | execute: false, // Manual handling |
| 10 | }); |
| 11 |  |
| 12 | const result = openrouter.callModel({ |
| 13 | model: 'openai/gpt-5-nano', |
| 14 | input: 'Send an email to alice@example.com', |
| 15 | tools: [confirmTool], |
| 16 | maxToolRounds: 0, |
| 17 | }); |
| 18 |  |
| 19 | const toolCalls = await result.getToolCalls(); |
| 20 |  |
| 21 | for (const call of toolCalls) { |
| 22 | if (call.name === 'send_email') { |
| 23 | // Show confirmation UI |
| 24 | const confirmed = await showConfirmDialog(call.arguments); |
| 25 |  |
| 26 | if (confirmed) { |
| 27 | await sendEmail(call.arguments); |
| 28 | } |
| 29 | } |
| 30 | } |
```

### Execution Results

Access execution metadata through getResponse():

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is 2+2 and the weather in Paris?', |
| 4 | tools: [calculatorTool, weatherTool], |
| 5 | }); |
| 6 |  |
| 7 | const response = await result.getResponse(); |
| 8 |  |
| 9 | // Response includes all execution rounds |
| 10 | console.log('Final output:', response.output); |
| 11 | console.log('Usage:', response.usage); |
```

## Error Handling

### Tool Execution Errors

Errors in execute functions are caught and sent back to the model:

```
|  |  |
| --- | --- |
| 1 | const riskyTool = tool({ |
| 2 | name: 'risky_operation', |
| 3 | inputSchema: z.object({ input: z.string() }), |
| 4 | outputSchema: z.object({ result: z.string() }), |
| 5 | execute: async (params) => { |
| 6 | if (params.input === 'fail') { |
| 7 | throw new Error('Operation failed: invalid input'); |
| 8 | } |
| 9 | return { result: 'success' }; |
| 10 | }, |
| 11 | }); |
| 12 |  |
| 13 | const result = openrouter.callModel({ |
| 14 | model: 'openai/gpt-5-nano', |
| 15 | input: 'Try the risky operation with "fail"', |
| 16 | tools: [riskyTool], |
| 17 | }); |
| 18 |  |
| 19 | // Model receives error message and can respond appropriately |
| 20 | const text = await result.getText(); |
| 21 | // "I tried the operation but it failed with: Operation failed: invalid input" |
```

### Validation Errors

Invalid tool arguments are caught before execution:

```
|  |  |
| --- | --- |
| 1 | const strictTool = tool({ |
| 2 | name: 'strict', |
| 3 | inputSchema: z.object({ |
| 4 | email: z.string().email(), |
| 5 | age: z.number().min(0).max(150), |
| 6 | }), |
| 7 | execute: async (params) => { |
| 8 | // Only runs with valid input |
| 9 | return { valid: true }; |
| 10 | }, |
| 11 | }); |
```

### Graceful Error Handling

Handle errors gracefully in execute functions:

```
|  |  |
| --- | --- |
| 1 | const robustTool = tool({ |
| 2 | name: 'fetch_data', |
| 3 | inputSchema: z.object({ url: z.string().url() }), |
| 4 | outputSchema: z.object({ |
| 5 | data: z.unknown().optional(), |
| 6 | error: z.string().optional(), |
| 7 | }), |
| 8 | execute: async (params) => { |
| 9 | try { |
| 10 | const response = await fetch(params.url); |
| 11 | if (!response.ok) { |
| 12 | return { error: `HTTP ${response.status}: ${response.statusText}` }; |
| 13 | } |
| 14 | return { data: await response.json() }; |
| 15 | } catch (error) { |
| 16 | return { error: `Failed to fetch: ${error.message}` }; |
| 17 | } |
| 18 | }, |
| 19 | }); |
```

## Best Practices

### Descriptive Names and Descriptions

```
|  |  |
| --- | --- |
| 1 | // Good: Clear name and description |
| 2 | const tool1 = tool({ |
| 3 | name: 'search_knowledge_base', |
| 4 | description: 'Search the company knowledge base for documents, FAQs, and policies. Returns relevant articles with snippets.', |
| 5 | // ... |
| 6 | }); |
| 7 |  |
| 8 | // Avoid: Vague or generic |
| 9 | const tool2 = tool({ |
| 10 | name: 'search', |
| 11 | description: 'Searches stuff', |
| 12 | // ... |
| 13 | }); |
```

### Schema Descriptions

Add `.describe()` to help the model understand parameters:

```
|  |  |
| --- | --- |
| 1 | const inputSchema = z.object({ |
| 2 | query: z.string().describe('Natural language search query'), |
| 3 | maxResults: z.number() |
| 4 | .min(1) |
| 5 | .max(100) |
| 6 | .default(10) |
| 7 | .describe('Maximum number of results to return (1-100)'), |
| 8 | dateRange: z.enum(['day', 'week', 'month', 'year', 'all']) |
| 9 | .default('all') |
| 10 | .describe('Filter results by time period'), |
| 11 | }); |
```

### Idempotent Tools

Design tools to be safely re-executable:

```
|  |  |
| --- | --- |
| 1 | const createUserTool = tool({ |
| 2 | name: 'create_user', |
| 3 | inputSchema: z.object({ |
| 4 | email: z.string().email(), |
| 5 | name: z.string(), |
| 6 | }), |
| 7 | execute: async (params) => { |
| 8 | // Check if user exists first |
| 9 | const existing = await findUserByEmail(params.email); |
| 10 | if (existing) { |
| 11 | return { userId: existing.id, created: false }; |
| 12 | } |
| 13 |  |
| 14 | const user = await createUser(params); |
| 15 | return { userId: user.id, created: true }; |
| 16 | }, |
| 17 | }); |
```

### Timeout Handling

Wrap long-running operations:

```
|  |  |
| --- | --- |
| 1 | const longRunningTool = tool({ |
| 2 | name: 'process_data', |
| 3 | inputSchema: z.object({ dataId: z.string() }), |
| 4 | execute: async (params) => { |
| 5 | const timeoutMs = 30000; |
| 6 |  |
| 7 | const result = await Promise.race([ |
| 8 | processData(params.dataId), |
| 9 | new Promise((_, reject) => |
| 10 | setTimeout(() => reject(new Error('Operation timed out')), timeoutMs) |
| 11 | ), |
| 12 | ]); |
| 13 |  |
| 14 | return result; |
| 15 | }, |
| 16 | }); |
```

## Next Steps

- **[Tool Approval & State](../approval-and-state/index.md)** - Human-in-the-loop approval and conversation persistence
- **[nextTurnParams](../next-turn-params/index.md)** - Tool-driven context injection
- **[Stop Conditions](../stop-conditions/index.md)** - Advanced execution control
- **[Examples](../examples/weather-tool/index.md)** - Complete tool implementations
