---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/tool-approval-state"
title: "Tool Approval & State Persistence | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:49.055323+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# 

Tool Approval & State Persistence

Add human-in-the-loop approval gates for sensitive tools and persist conversation state across callModel invocations.

## Why Approval Gates?

Some tools — sending emails, making payments, deleting records — should not auto-execute without human review. The SDK provides two mechanisms to control this:

- **`requireApproval`** — pause execution when the model calls sensitive tools, giving users a chance to approve or reject each call
- **`StateAccessor`** — persist conversation state between `callModel` invocations so approval decisions, message history, and tool results survive across runs

Together, these enable human-in-the-loop workflows where a user reviews tool calls before they execute, even across separate request/response cycles (e.g., in a web application).

## Tool-Level Approval

Add `requireApproval` directly on a tool definition. It accepts a boolean or a function:

### Always Require Approval

```
|  |  |
| --- | --- |
| 1 | import { tool } from '@openrouter/agent'; |
| 2 | import { z } from 'zod'; |
| 3 |  |
| 4 | const sendEmailTool = tool({ |
| 5 | name: 'send_email', |
| 6 | description: 'Send an email to a recipient', |
| 7 | inputSchema: z.object({ |
| 8 | to: z.string().email(), |
| 9 | subject: z.string(), |
| 10 | body: z.string(), |
| 11 | }), |
| 12 | outputSchema: z.object({ sent: z.boolean() }), |
| 13 | requireApproval: true, |
| 14 | execute: async (params) => { |
| 15 | await sendEmail(params); |
| 16 | return { sent: true }; |
| 17 | }, |
| 18 | }); |
```

### Conditional Approval

Pass a function to require approval only in certain cases:

```
|  |  |
| --- | --- |
| 1 | const deleteRecordTool = tool({ |
| 2 | name: 'delete_record', |
| 3 | description: 'Delete a record from the database', |
| 4 | inputSchema: z.object({ |
| 5 | id: z.string(), |
| 6 | environment: z.enum(['staging', 'production']), |
| 7 | }), |
| 8 | outputSchema: z.object({ deleted: z.boolean() }), |
| 9 | requireApproval: (params, context) => { |
| 10 | // Only require approval for production deletions |
| 11 | return params.environment === 'production'; |
| 12 | }, |
| 13 | execute: async (params) => { |
| 14 | await deleteRecord(params.id); |
| 15 | return { deleted: true }; |
| 16 | }, |
| 17 | }); |
```

The function receives the parsed tool arguments and a `TurnContext`, and can return a boolean or `Promise<boolean>`.

## Call-Level Approval

Override tool-level settings with a `requireApproval` callback on `callModel` itself:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-4o', |
| 3 | input: 'Send an email and search for documents', |
| 4 | tools: [sendEmailTool, searchTool], |
| 5 | state: myStateAccessor, |
| 6 | requireApproval: (toolCall, context) => { |
| 7 | // Require approval for any tool that modifies data |
| 8 | return toolCall.name === 'send_email' || toolCall.name === 'delete_record'; |
| 9 | }, |
| 10 | }); |
```

The call-level callback takes priority over tool-level `requireApproval` settings when both are present.

## How the Approval Flow Works

When tools with approval gates are called by the model, the SDK follows this flow:

1. **Model generates tool calls** — the model decides which tools to invoke
2. **SDK partitions tool calls** — each call is checked against `requireApproval` and split into two groups: those requiring approval and those that can auto-execute
3. **Auto-execute tools run immediately** — tools that don’t need approval execute in parallel as normal
4. **State saves with pending approvals** — the conversation state updates to `status: 'awaiting_approval'` with the pending tool calls stored
5. **Control returns to the caller** — check `result.requiresApproval()` and inspect pending calls with `result.getPendingToolCalls()`
6. **Resume with decisions** — call `callModel` again with the same `state`, passing `approveToolCalls` and/or `rejectToolCalls` arrays of tool call IDs
7. **Approved tools execute** — the SDK runs approved tools and sends results to the model. Rejected tools send an error message to the model explaining the rejection
8. **Conversation continues** — the model processes tool results and generates the next response

## StateAccessor Interface

The `StateAccessor` interface enables any storage backend:

```
|  |  |
| --- | --- |
| 1 | import type { StateAccessor, ConversationState } from '@openrouter/agent'; |
| 2 |  |
| 3 | interface StateAccessor<TTools> { |
| 4 | /** Load the current conversation state, or null if none exists */ |
| 5 | load: () => Promise<ConversationState<TTools> | null>; |
| 6 | /** Save the conversation state */ |
| 7 | save: (state: ConversationState<TTools>) => Promise<void>; |
| 8 | } |
```

### In-Memory Implementation

```
|  |  |
| --- | --- |
| 1 | const conversations = new Map<string, ConversationState>(); |
| 2 |  |
| 3 | function createStateAccessor(conversationId: string): StateAccessor { |
| 4 | return { |
| 5 | load: async () => conversations.get(conversationId) ?? null, |
| 6 | save: async (state) => { |
| 7 | conversations.set(conversationId, state); |
| 8 | }, |
| 9 | }; |
| 10 | } |
```

For production use, implement `StateAccessor` with a persistent backend like Redis, a database, or file storage to survive process restarts.

## ConversationState

The state object tracks everything needed to resume a conversation:

| Field | Type | Description |
| --- | --- | --- |
| `id` | `string` | Unique conversation identifier |
| `messages` | `OpenResponsesInputUnion` | Full message history |
| `previousResponseId` | `string?` | Previous response ID for server-side chaining |
| `pendingToolCalls` | `ParsedToolCall[]?` | Tool calls awaiting human approval |
| `unsentToolResults` | `UnsentToolResult[]?` | Executed results not yet sent to model |
| `partialResponse` | `PartialResponse?` | Data captured during interruption |
| `interruptedBy` | `string?` | Signal from a new request that interrupted this conversation |
| `status` | `ConversationStatus` | Current state of the conversation |
| `createdAt` | `number` | Creation timestamp (Unix ms) |
| `updatedAt` | `number` | Last update timestamp (Unix ms) |

### Status Values

| Status | Meaning |
| --- | --- |
| `'in_progress'` | Conversation is actively processing |
| `'awaiting_approval'` | Paused, waiting for tool call approval/rejection |
| `'complete'` | Conversation finished normally |
| `'interrupted'` | Conversation was interrupted and can be resumed |

## Complete Example

Here is an end-to-end example showing approval gates with state persistence:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool } from '@openrouter/agent'; |
| 2 | import type { ConversationState, StateAccessor } from '@openrouter/agent'; |
| 3 | import { z } from 'zod'; |
| 4 |  |
| 5 | // 1. Define a tool with approval required |
| 6 | const sendEmailTool = tool({ |
| 7 | name: 'send_email', |
| 8 | description: 'Send an email', |
| 9 | inputSchema: z.object({ |
| 10 | to: z.string().email(), |
| 11 | subject: z.string(), |
| 12 | body: z.string(), |
| 13 | }), |
| 14 | outputSchema: z.object({ sent: z.boolean(), messageId: z.string() }), |
| 15 | requireApproval: true, |
| 16 | execute: async (params) => { |
| 17 | const result = await sendEmail(params); |
| 18 | return { sent: true, messageId: result.id }; |
| 19 | }, |
| 20 | }); |
| 21 |  |
| 22 | // 2. Create a state accessor (in-memory for this example) |
| 23 | const store = new Map<string, ConversationState>(); |
| 24 | const conversationId = 'conv-123'; |
| 25 |  |
| 26 | const state: StateAccessor = { |
| 27 | load: async () => store.get(conversationId) ?? null, |
| 28 | save: async (s) => { store.set(conversationId, s); }, |
| 29 | }; |
| 30 |  |
| 31 | const openrouter = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY }); |
| 32 |  |
| 33 | // 3. First callModel — model will try to call the tool |
| 34 | const result = openrouter.callModel({ |
| 35 | model: 'openai/gpt-4o', |
| 36 | input: 'Send a welcome email to alice@example.com', |
| 37 | tools: [sendEmailTool] as const, |
| 38 | state, |
| 39 | }); |
| 40 |  |
| 41 | // 4. Check if approval is needed |
| 42 | if (await result.requiresApproval()) { |
| 43 | const pending = await result.getPendingToolCalls(); |
| 44 |  |
| 45 | for (const call of pending) { |
| 46 | console.log(`Tool: ${call.name}`); |
| 47 | console.log(`To: ${call.arguments.to}`); |
| 48 | console.log(`Subject: ${call.arguments.subject}`); |
| 49 | console.log(`ID: ${call.id}`); |
| 50 | } |
| 51 |  |
| 52 | // 5. Present to user for decision, then resume |
| 53 | const approved = await askUserForApproval(pending); |
| 54 |  |
| 55 | const approvedIds = approved.filter(a => a.decision === 'approve').map(a => a.id); |
| 56 | const rejectedIds = approved.filter(a => a.decision === 'reject').map(a => a.id); |
| 57 |  |
| 58 | // 6. Second callModel — resume with approval decisions |
| 59 | const resumed = openrouter.callModel({ |
| 60 | model: 'openai/gpt-4o', |
| 61 | input: [], // No new user input needed for resumption |
| 62 | tools: [sendEmailTool] as const, |
| 63 | state, |
| 64 | approveToolCalls: approvedIds, |
| 65 | rejectToolCalls: rejectedIds, |
| 66 | }); |
| 67 |  |
| 68 | // 7. Get the final response |
| 69 | const text = await resumed.getText(); |
| 70 | console.log(text); |
| 71 | // "I've sent the welcome email to alice@example.com." |
| 72 | } else { |
| 73 | // No approval needed — tool ran automatically |
| 74 | const text = await result.getText(); |
| 75 | console.log(text); |
| 76 | } |
```

## Resumption Patterns

### Resuming from Approval

When the state has `status: 'awaiting_approval'`, pass `approveToolCalls` and/or `rejectToolCalls` to resume:

```
|  |  |
| --- | --- |
| 1 | // Load existing state |
| 2 | const loaded = await state.load(); |
| 3 |  |
| 4 | if (loaded?.status === 'awaiting_approval') { |
| 5 | const pending = loaded.pendingToolCalls ?? []; |
| 6 |  |
| 7 | // Approve all pending calls |
| 8 | const result = openrouter.callModel({ |
| 9 | model: 'openai/gpt-4o', |
| 10 | input: [], |
| 11 | tools: [sendEmailTool] as const, |
| 12 | state, |
| 13 | approveToolCalls: pending.map(c => c.id), |
| 14 | }); |
| 15 |  |
| 16 | const text = await result.getText(); |
| 17 | } |
```

### Resuming from Interruption

If a conversation was interrupted (`status: 'interrupted'`), calling `callModel` with the same state resumes automatically. The SDK clears the interruption flag and continues where it left off:

```
|  |  |
| --- | --- |
| 1 | const loaded = await state.load(); |
| 2 |  |
| 3 | if (loaded?.status === 'interrupted') { |
| 4 | // Resume — the SDK picks up from the interruption point |
| 5 | const result = openrouter.callModel({ |
| 6 | model: 'openai/gpt-4o', |
| 7 | input: 'Continue where you left off', |
| 8 | tools: myTools, |
| 9 | state, |
| 10 | }); |
| 11 |  |
| 12 | const text = await result.getText(); |
| 13 | } |
```

### Multi-Run Conversations

Messages accumulate automatically across `callModel` runs that share the same `StateAccessor`. Each run appends its input and response to the state’s message history:

```
|  |  |
| --- | --- |
| 1 | const state: StateAccessor = createStateAccessor('conv-456'); |
| 2 |  |
| 3 | // Turn 1 |
| 4 | const r1 = openrouter.callModel({ |
| 5 | model: 'openai/gpt-4o', |
| 6 | input: 'What is the weather in Tokyo?', |
| 7 | tools: [weatherTool] as const, |
| 8 | state, |
| 9 | }); |
| 10 | console.log(await r1.getText()); |
| 11 | // "The weather in Tokyo is 22°C and sunny." |
| 12 |  |
| 13 | // Turn 2 — state has full history from turn 1 |
| 14 | const r2 = openrouter.callModel({ |
| 15 | model: 'openai/gpt-4o', |
| 16 | input: 'And in Paris?', |
| 17 | tools: [weatherTool] as const, |
| 18 | state, |
| 19 | }); |
| 20 | console.log(await r2.getText()); |
| 21 | // "The weather in Paris is 15°C and cloudy." |
| 22 |  |
| 23 | // Turn 3 — state has history from both prior turns |
| 24 | const r3 = openrouter.callModel({ |
| 25 | model: 'openai/gpt-4o', |
| 26 | input: 'Which city is warmer?', |
| 27 | tools: [weatherTool] as const, |
| 28 | state, |
| 29 | }); |
| 30 | console.log(await r3.getText()); |
| 31 | // "Tokyo is warmer at 22°C compared to Paris at 15°C." |
```

## Next Steps

- **[Tools](../tools/index.md)** - Tool definitions and the `tool()` helper
- **[Stop Conditions](../stop-conditions/index.md)** - Control when tool execution loops terminate
- **[Dynamic Parameters](../dynamic-parameters/index.md)** - Adjust parameters between turns
- **[Examples](../examples/weather-tool/index.md)** - Complete tool implementations
