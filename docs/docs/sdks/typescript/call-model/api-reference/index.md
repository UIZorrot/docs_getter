---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/api-reference"
title: "API Reference | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:09.365603+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# API Reference

Complete reference for the callModel API, ModelResult class, tool types, and helper functions.

## callModel

```
|  |  |
| --- | --- |
| 1 | function callModel(request: CallModelInput, options?: RequestOptions): ModelResult |
```

Creates a response using the OpenResponses API with multiple consumption patterns.

### CallModelInput

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | `string | ((ctx: TurnContext) => string)` | Yes\* | Model ID (e.g., “openai/gpt-5-nano”) |
| `models` | `string[]` | Yes\* | Model fallback array |
| `input` | `OpenResponsesInput` | Yes | Input messages or string |
| `instructions` | `string | ((ctx: TurnContext) => string)` | No | System instructions |
| `tools` | `Tool[]` | No | Tools available to the model |
| `maxToolRounds` | `MaxToolRounds` | No | Tool execution limit (deprecated) |
| `stopWhen` | `StopWhen` | No | Stop conditions |
| `temperature` | `number | ((ctx: TurnContext) => number)` | No | Sampling temperature (0-2) |
| `maxOutputTokens` | `number | ((ctx: TurnContext) => number)` | No | Maximum tokens to generate |
| `topP` | `number` | No | Top-p sampling |
| `text` | `ResponseTextConfig` | No | Text format configuration |
| `provider` | `ProviderPreferences` | No | Provider routing and configuration |
| `topK` | `number` | No | Top-k sampling |
| `metadata` | `Record<string, string>` | No | Request metadata |
| `toolChoice` | `ToolChoice` | No | Tool choice configuration |
| `parallelToolCalls` | `boolean` | No | Enable parallel tool calling |
| `reasoning` | `ReasoningConfig` | No | Reasoning configuration |
| `promptCacheKey` | `string` | No | Cache key for prompt caching |
| `previousResponseId` | `string` | No | Context from previous response |
| `include` | `string[]` | No | Include extra fields in response |
| `background` | `boolean` | No | Run request in background |
| `safetyIdentifier` | `string` | No | User safety identifier |
| `serviceTier` | `string` | No | Service tier preference |
| `truncation` | `string` | No | Truncation mode |
| `plugins` | `Plugin[]` | No | Enabled plugins |
| `user` | `string` | No | End-user identifier |
| `sessionId` | `string` | No | Session identifier |
| `store` | `boolean` | No | Store request data |
| `context` | `ContextInput<ToolContextMap>` | No | Tool context keyed by tool name |

\*Either `model` or `models` is required.

### ProviderPreferences

Configuration for routing and provider selection.

| Parameter | Type | Description |
| --- | --- | --- |
| `allowFallbacks` | `boolean` | Allow backup providers when primary is unavailable (default: true) |
| `requireParameters` | `boolean` | Only use providers that support all requested parameters |
| `dataCollection` | `"allow" | "deny"` | Data collection policy (allow/deny) |
| `order` | `string[]` | Custom provider routing order |
| `only` | `string[]` | Restrict to specific providers |
| `ignore` | `string[]` | Exclude specific providers |
| `quantizations` | `string[]` | Filter by quantization levels |
| `sort` | `string` | Load balancing strategy (e.g., “throughput”) |
| `maxPrice` | `object` | Maximum price limits |
| `preferredMinThroughput` | `number` | Minimum tokens per second preference |
| `preferredMaxLatency` | `number` | Maximum latency preference |

### RequestOptions

| Parameter | Type | Description |
| --- | --- | --- |
| `timeout` | `number` | Request timeout in milliseconds |
| `signal` | `AbortSignal` | Abort signal for cancellation |

---

## ModelResult

Wrapper providing multiple consumption patterns for a response.

### Methods

#### getText()

```
|  |  |
| --- | --- |
| 1 | getText(): Promise<string> |
```

Get text content after tool execution completes.

#### getResponse()

```
|  |  |
| --- | --- |
| 1 | getResponse(): Promise<OpenResponsesNonStreamingResponse> |
```

Get full response with usage data (inputTokens, outputTokens, cachedTokens).

#### getTextStream()

```
|  |  |
| --- | --- |
| 1 | getTextStream(): AsyncIterableIterator<string> |
```

Stream text deltas.

#### getReasoningStream()

```
|  |  |
| --- | --- |
| 1 | getReasoningStream(): AsyncIterableIterator<string> |
```

Stream reasoning deltas (for reasoning models).

#### getNewMessagesStream()

```
|  |  |
| --- | --- |
| 1 | getNewMessagesStream(): AsyncIterableIterator<ResponsesOutputMessage | OpenResponsesFunctionCallOutput> |
```

Stream cumulative message snapshots in OpenResponses format.

#### getFullResponsesStream()

```
|  |  |
| --- | --- |
| 1 | getFullResponsesStream(): AsyncIterableIterator<EnhancedResponseStreamEvent> |
```

Stream all events including tool preliminary results.

#### getToolCalls()

```
|  |  |
| --- | --- |
| 1 | getToolCalls(): Promise<ParsedToolCall[]> |
```

Get all tool calls from initial response.

#### getToolCallsStream()

```
|  |  |
| --- | --- |
| 1 | getToolCallsStream(): AsyncIterableIterator<ParsedToolCall> |
```

Stream tool calls as they complete.

#### getToolStream()

```
|  |  |
| --- | --- |
| 1 | getToolStream(): AsyncIterableIterator<ToolStreamEvent> |
```

Stream tool deltas and preliminary results.

#### getContextUpdates()

```
|  |  |
| --- | --- |
| 1 | getContextUpdates(): AsyncGenerator<ToolContextMap<TTools>> |
```

Stream context snapshots whenever a tool calls
`setContext()`. Completes when tool execution finishes.

#### cancel()

```
|  |  |
| --- | --- |
| 1 | cancel(): Promise<void> |
```

Cancel the stream and all consumers.

---

## Tool Types

### tool()

```
|  |  |
| --- | --- |
| 1 | function tool<TInput, TOutput>(config: ToolConfig): Tool |
```

Create a typed tool with Zod schema validation.

### ToolConfig

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Tool name |
| `description` | `string` | No | Tool description |
| `inputSchema` | `ZodObject` | Yes | Input parameter schema |
| `outputSchema` | `ZodType` | No | Output schema |
| `eventSchema` | `ZodType` | No | Event schema (triggers generator mode) |
| `contextSchema` | `ZodObject` | No | Context data this tool needs |
| `execute` | `function | false` | Yes | Execute function or false for manual |
| `nextTurnParams` | `NextTurnParamsFunctions` | No | Parameters to modify next turn |

### Tool

Union type of all tool types:

```
|  |  |
| --- | --- |
| 1 | type Tool = |
| 2 | | ToolWithExecute<ZodObject, ZodType> |
| 3 | | ToolWithGenerator<ZodObject, ZodType, ZodType> |
| 4 | | ManualTool<ZodObject, ZodType>; |
```

### ToolWithExecute

Regular tool with execute function:

```
|  |  |
| --- | --- |
| 1 | interface ToolWithExecute< |
| 2 | TInput, TOutput, TContext, TName |
| 3 | > { |
| 4 | type: ToolType.Function; |
| 5 | function: { |
| 6 | name: TName; |
| 7 | description?: string; |
| 8 | inputSchema: TInput; |
| 9 | outputSchema?: TOutput; |
| 10 | contextSchema?: ZodObject; |
| 11 | execute: ( |
| 12 | params: z.infer<TInput>, |
| 13 | context: ToolExecuteContext<TName, TContext>, |
| 14 | ) => Promise<z.infer<TOutput>>; |
| 15 | }; |
| 16 | } |
```

### ToolWithGenerator

Generator tool with eventSchema:

```
|  |  |
| --- | --- |
| 1 | interface ToolWithGenerator< |
| 2 | TInput, TEvent, TOutput, TContext, TName |
| 3 | > { |
| 4 | type: ToolType.Function; |
| 5 | function: { |
| 6 | name: TName; |
| 7 | description?: string; |
| 8 | inputSchema: TInput; |
| 9 | eventSchema: TEvent; |
| 10 | outputSchema: TOutput; |
| 11 | contextSchema?: ZodObject; |
| 12 | execute: ( |
| 13 | params: z.infer<TInput>, |
| 14 | context: ToolExecuteContext<TName, TContext>, |
| 15 | ) => AsyncGenerator<z.infer<TEvent>>; |
| 16 | }; |
| 17 | } |
```

### ManualTool

Tool without execute function:

```
|  |  |
| --- | --- |
| 1 | interface ManualTool<TInput, TOutput> { |
| 2 | type: ToolType.Function; |
| 3 | function: { |
| 4 | name: string; |
| 5 | description?: string; |
| 6 | inputSchema: TInput; |
| 7 | outputSchema?: TOutput; |
| 8 | }; |
| 9 | } |
```

---

## Context Types

### TurnContext

```
|  |  |
| --- | --- |
| 1 | interface TurnContext { |
| 2 | toolCall?: OpenResponsesFunctionToolCall; |
| 3 | numberOfTurns: number; |
| 4 | turnRequest?: OpenResponsesRequest; |
| 5 | } |
```

### ToolExecuteContext

Flat context passed to tool execute functions.
Merges `TurnContext` fields with tool-specific context:

```
|  |  |
| --- | --- |
| 1 | type ToolExecuteContext<TName, TContext> = |
| 2 | TurnContext & { |
| 3 | tools: { |
| 4 | readonly [K in TName]: Readonly<TContext>; |
| 5 | }; |
| 6 | setContext(partial: Partial<TContext>): void; |
| 7 | }; |
```

### ToolContextMap

Context map for `callModel`’s `context` option,
keyed by tool name:

```
|  |  |
| --- | --- |
| 1 | type ToolContextMap<T extends readonly Tool[]> = { |
| 2 | [K in T[number] as K['function']['name']]: |
| 3 | InferToolContext<K>; |
| 4 | }; |
```

### ContextInput

Context can be static, a sync function,
or an async function:

```
|  |  |
| --- | --- |
| 1 | type ContextInput<T> = |
| 2 | | T |
| 3 | | ((turn: TurnContext) => T) |
| 4 | | ((turn: TurnContext) => Promise<T>); |
```

### NextTurnParamsContext

```
|  |  |
| --- | --- |
| 1 | interface NextTurnParamsContext { |
| 2 | input: OpenResponsesInput; |
| 3 | model: string; |
| 4 | models: string[]; |
| 5 | temperature: number | null; |
| 6 | maxOutputTokens: number | null; |
| 7 | topP: number | null; |
| 8 | topK?: number | undefined; |
| 9 | instructions: string | null; |
| 10 | } |
```

---

## Stream Event Types

### EnhancedResponseStreamEvent

```
|  |  |
| --- | --- |
| 1 | type EnhancedResponseStreamEvent = |
| 2 | | OpenResponsesStreamEvent |
| 3 | | ToolPreliminaryResultEvent; |
```

### ToolStreamEvent

```
|  |  |
| --- | --- |
| 1 | type ToolStreamEvent = |
| 2 | | { type: 'delta'; content: string } |
| 3 | | { type: 'preliminary_result'; toolCallId: string; result: unknown }; |
```

### ParsedToolCall

```
|  |  |
| --- | --- |
| 1 | interface ParsedToolCall { |
| 2 | id: string; |
| 3 | name: string; |
| 4 | arguments: unknown; |
| 5 | } |
```

### ToolExecutionResult

```
|  |  |
| --- | --- |
| 1 | interface ToolExecutionResult { |
| 2 | toolCallId: string; |
| 3 | toolName: string; |
| 4 | result: unknown; |
| 5 | preliminaryResults?: unknown[]; |
| 6 | error?: Error; |
| 7 | } |
```

---

## Stop Conditions

### StopWhen

```
|  |  |
| --- | --- |
| 1 | type StopWhen = |
| 2 | | StopCondition |
| 3 | | StopCondition[]; |
```

### StopCondition

```
|  |  |
| --- | --- |
| 1 | type StopCondition = (context: StopConditionContext) => boolean | Promise<boolean>; |
```

### StopConditionContext

```
|  |  |
| --- | --- |
| 1 | interface StopConditionContext { |
| 2 | steps: StepResult[]; |
| 3 | } |
```

### StepResult

```
|  |  |
| --- | --- |
| 1 | interface StepResult { |
| 2 | stepType: 'initial' | 'continue'; |
| 3 | text: string; |
| 4 | toolCalls: TypedToolCallUnion[]; |
| 5 | toolResults: ToolExecutionResultUnion[]; |
| 6 | response: OpenResponsesNonStreamingResponse; |
| 7 | usage?: OpenResponsesUsage; |
| 8 | finishReason?: string; |
| 9 | warnings?: Warning[]; |
| 10 | experimental_providerMetadata?: Record<string, unknown>; |
| 11 | } |
```

### Warning

```
|  |  |
| --- | --- |
| 1 | interface Warning { |
| 2 | type: string; |
| 3 | message: string; |
| 4 | } |
```

### Built-in Helpers

| Function | Signature | Description |
| --- | --- | --- |
| `stepCountIs` | `(n: number) => StopCondition` | Stop after n steps |
| `hasToolCall` | `(name: string) => StopCondition` | Stop when tool is called |
| `maxTokensUsed` | `(n: number) => StopCondition` | Stop after n tokens |
| `maxCost` | `(amount: number) => StopCondition` | Stop after cost limit |
| `finishReasonIs` | `(reason: string) => StopCondition` | Stop on finish reason |

---

## Format Helpers

### fromChatMessages

```
|  |  |
| --- | --- |
| 1 | function fromChatMessages(messages: Message[]): OpenResponsesInput |
```

Convert OpenAI chat format to OpenResponses input.

### toChatMessage

```
|  |  |
| --- | --- |
| 1 | function toChatMessage(response: OpenResponsesNonStreamingResponse): AssistantMessage |
```

Convert response to chat message format.

### fromClaudeMessages

```
|  |  |
| --- | --- |
| 1 | function fromClaudeMessages(messages: ClaudeMessageParam[]): OpenResponsesInput |
```

Convert Anthropic Claude format to OpenResponses input.

### toClaudeMessage

```
|  |  |
| --- | --- |
| 1 | function toClaudeMessage(response: OpenResponsesNonStreamingResponse): ClaudeMessage |
```

Convert response to Claude message format.

---

## Type Utilities

### InferToolInput

```
|  |  |
| --- | --- |
| 1 | type InferToolInput<T> = T extends { function: { inputSchema: infer S } } |
| 2 | ? S extends ZodType ? z.infer<S> : unknown |
| 3 | : unknown; |
```

### InferToolOutput

```
|  |  |
| --- | --- |
| 1 | type InferToolOutput<T> = T extends { function: { outputSchema: infer S } } |
| 2 | ? S extends ZodType ? z.infer<S> : unknown |
| 3 | : unknown; |
```

### InferToolEvent

```
|  |  |
| --- | --- |
| 1 | type InferToolEvent<T> = T extends { function: { eventSchema: infer S } } |
| 2 | ? S extends ZodType ? z.infer<S> : never |
| 3 | : never; |
```

### TypedToolCall

```
|  |  |
| --- | --- |
| 1 | type TypedToolCall<T extends Tool> = { |
| 2 | id: string; |
| 3 | name: T extends { function: { name: infer N } } ? N : string; |
| 4 | arguments: InferToolInput<T>; |
| 5 | }; |
```

---

## Exports

```
|  |  |
| --- | --- |
| 1 | // Agent client |
| 2 | export { OpenRouter } from '@openrouter/agent'; |
| 3 |  |
| 4 | // Tool helpers |
| 5 | export { tool, ToolType } from '@openrouter/agent'; |
| 6 |  |
| 7 | // Format helpers |
| 8 | export { fromChatMessages, toChatMessage, fromClaudeMessages, toClaudeMessage } from '@openrouter/agent'; |
| 9 |  |
| 10 | // Stop condition helpers |
| 11 | export { stepCountIs, hasToolCall, maxTokensUsed, maxCost, finishReasonIs } from '@openrouter/agent'; |
| 12 |  |
| 13 | // Context helpers |
| 14 | export { |
| 15 | buildToolExecuteContext, |
| 16 | ToolContextStore, |
| 17 | } from '@openrouter/agent'; |
| 18 |  |
| 19 | // Types |
| 20 | export type { |
| 21 | CallModelInput, |
| 22 | ContextInput, |
| 23 | Tool, |
| 24 | ToolWithExecute, |
| 25 | ToolWithGenerator, |
| 26 | ManualTool, |
| 27 | ToolExecuteContext, |
| 28 | ToolContextMap, |
| 29 | TurnContext, |
| 30 | ParsedToolCall, |
| 31 | ToolExecutionResult, |
| 32 | StopCondition, |
| 33 | StopWhen, |
| 34 | InferToolInput, |
| 35 | InferToolOutput, |
| 36 | InferToolEvent, |
| 37 | } from '@openrouter/agent'; |
```
