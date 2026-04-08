---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/stop-conditions"
title: "Stop Conditions | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:10.132881+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Stop Conditions

Control multi-turn execution with `stopWhen`. Use built-in helpers or custom conditions to stop by step count, tool calls, cost, or tokens.

## Basic Usage

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, stepCountIs } from '@openrouter/agent'; |
| 2 |  |
| 3 | const openrouter = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY, |
| 5 | }); |
| 6 |  |
| 7 | const result = openrouter.callModel({ |
| 8 | model: 'openai/gpt-5-nano', |
| 9 | input: 'Research this topic thoroughly', |
| 10 | tools: [searchTool, analysisTool], |
| 11 | stopWhen: stepCountIs(5), // Stop after 5 steps |
| 12 | }); |
```

## Built-in Stop Conditions

### stepCountIs(n)

Stop after a specific number of steps:

```
|  |  |
| --- | --- |
| 1 | import { stepCountIs } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5-nano', |
| 5 | input: 'Analyze this data', |
| 6 | tools: [analysisTool], |
| 7 | stopWhen: stepCountIs(10), // Stop after 10 steps |
| 8 | }); |
```

### hasToolCall(name)

Stop when a specific tool is called:

```
|  |  |
| --- | --- |
| 1 | import { hasToolCall } from '@openrouter/agent'; |
| 2 |  |
| 3 | const finishTool = tool({ |
| 4 | name: 'finish', |
| 5 | description: 'Call this when the task is complete', |
| 6 | inputSchema: z.object({ |
| 7 | summary: z.string(), |
| 8 | }), |
| 9 | execute: async (params) => ({ done: true }), |
| 10 | }); |
| 11 |  |
| 12 | const result = openrouter.callModel({ |
| 13 | model: 'openai/gpt-5-nano', |
| 14 | input: 'Research until you have enough information, then call finish', |
| 15 | tools: [searchTool, finishTool], |
| 16 | stopWhen: hasToolCall('finish'), // Stop when finish tool is called |
| 17 | }); |
```

### maxTokensUsed(n)

Stop after using a certain number of tokens:

```
|  |  |
| --- | --- |
| 1 | import { maxTokensUsed } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5-nano', |
| 5 | input: 'Generate content', |
| 6 | tools: [writingTool], |
| 7 | stopWhen: maxTokensUsed(5000), // Stop after 5000 total tokens |
| 8 | }); |
```

### maxCost(amount)

Stop after reaching a cost threshold:

```
|  |  |
| --- | --- |
| 1 | import { maxCost } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5.2', |
| 5 | input: 'Perform extensive analysis', |
| 6 | tools: [analysisTool], |
| 7 | stopWhen: maxCost(1.00), // Stop after $1.00 spent |
| 8 | }); |
```

### finishReasonIs(reason)

Stop on a specific finish reason:

```
|  |  |
| --- | --- |
| 1 | import { finishReasonIs } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5-nano', |
| 5 | input: 'Complete this task', |
| 6 | tools: [taskTool], |
| 7 | stopWhen: finishReasonIs('stop'), // Stop when model finishes naturally |
| 8 | }); |
```

## Combining Conditions

Pass an array to stop on any condition:

```
|  |  |
| --- | --- |
| 1 | import { stepCountIs, hasToolCall, maxCost } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5.2', |
| 5 | input: 'Research thoroughly but stay within budget', |
| 6 | tools: [searchTool, finishTool], |
| 7 | stopWhen: [ |
| 8 | stepCountIs(10),        // Maximum 10 steps |
| 9 | maxCost(0.50),          // Maximum $0.50 |
| 10 | hasToolCall('finish'),  // Or when finish is called |
| 11 | ], |
| 12 | }); |
```

Execution stops when **any** condition is met.

## Custom Stop Conditions

Create custom conditions with a function:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Process data', |
| 4 | tools: [processTool], |
| 5 | stopWhen: ({ steps }) => { |
| 6 | // Stop after 20 steps |
| 7 | if (steps.length >= 20) return true; |
| 8 |  |
| 9 | // Stop if last step had no tool calls |
| 10 | const lastStep = steps[steps.length - 1]; |
| 11 | if (lastStep && !lastStep.toolCalls?.length) return true; |
| 12 |  |
| 13 | // Continue otherwise |
| 14 | return false; |
| 15 | }, |
| 16 | }); |
```

### StopConditionContext

Custom functions receive:

| Property | Type | Description |
| --- | --- | --- |
| `steps` | `StepResult[]` | All completed steps including results and usage |

### StepResult

Each step contains:

```
|  |  |
| --- | --- |
| 1 | interface StepResult { |
| 2 | response: Response; |
| 3 | toolCalls?: ParsedToolCall[]; |
| 4 | toolResults?: ToolExecutionResult[]; |
| 5 | tokens: { |
| 6 | input: number; |
| 7 | output: number; |
| 8 | cached: number; |
| 9 | }; |
| 10 | cost: number; |
| 11 | } |
```

## Advanced Patterns

### Time-Based Stopping

Stop after a time limit:

```
|  |  |
| --- | --- |
| 1 | const startTime = Date.now(); |
| 2 | const maxDuration = 30000; // 30 seconds |
| 3 |  |
| 4 | const result = openrouter.callModel({ |
| 5 | model: 'openai/gpt-5-nano', |
| 6 | input: 'Work on this task', |
| 7 | tools: [workTool], |
| 8 | stopWhen: () => { |
| 9 | return Date.now() - startTime > maxDuration; |
| 10 | }, |
| 11 | }); |
```

### Content-Based Stopping

Stop based on response content:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Search until you find the answer', |
| 4 | tools: [searchTool], |
| 5 | stopWhen: ({ steps }) => { |
| 6 | const lastStep = steps[steps.length - 1]; |
| 7 | if (!lastStep) return false; |
| 8 |  |
| 9 | // Check if response contains certain keywords |
| 10 | const content = JSON.stringify(lastStep.response); |
| 11 | return content.includes('ANSWER FOUND') || content.includes('TASK COMPLETE'); |
| 12 | }, |
| 13 | }); |
```

### Quality-Based Stopping

Stop when results meet quality threshold:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Improve this text until it scores above 0.9', |
| 4 | tools: [improverTool, scorerTool], |
| 5 | stopWhen: ({ steps }) => { |
| 6 | // Look for score in tool results |
| 7 | for (const step of steps) { |
| 8 | for (const result of step.toolResults ?? []) { |
| 9 | if (result.toolName === 'scorer' && result.result?.score > 0.9) { |
| 10 | return true; |
| 11 | } |
| 12 | } |
| 13 | } |
| 14 | return false; |
| 15 | }, |
| 16 | }); |
```

### Combination with Early Exit

Combine conditions for complex logic:

```
|  |  |
| --- | --- |
| 1 | import { stepCountIs, maxCost } from '@openrouter/agent'; |
| 2 |  |
| 3 | const result = openrouter.callModel({ |
| 4 | model: 'openai/gpt-5.2', |
| 5 | input: 'Complex research task', |
| 6 | tools: [searchTool, analysisTool, summarizeTool], |
| 7 | stopWhen: [ |
| 8 | // Hard limits |
| 9 | stepCountIs(50), |
| 10 | maxCost(5.00), |
| 11 |  |
| 12 | // Custom success condition |
| 13 | ({ steps }) => { |
| 14 | const lastStep = steps[steps.length - 1]; |
| 15 | const hasSummary = lastStep?.toolCalls?.some( |
| 16 | tc => tc.name === 'summarize' |
| 17 | ); |
| 18 | return hasSummary; |
| 19 | }, |
| 20 | ], |
| 21 | }); |
```

## Migration from maxToolRounds

If you were using `maxToolRounds`, migrate to `stopWhen`:

```
|  |  |
| --- | --- |
| 1 | // Before: maxToolRounds |
| 2 | const result = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Hello', |
| 5 | tools: [myTool], |
| 6 | maxToolRounds: 5, |
| 7 | }); |
| 8 |  |
| 9 | // After: stopWhen |
| 10 | import { stepCountIs } from '@openrouter/agent'; |
| 11 |  |
| 12 | const result = openrouter.callModel({ |
| 13 | model: 'openai/gpt-5-nano', |
| 14 | input: 'Hello', |
| 15 | tools: [myTool], |
| 16 | stopWhen: stepCountIs(5), |
| 17 | }); |
```

### Default Behavior

If `stopWhen` is not specified, the default is `stepCountIs(5)`.

## Best Practices

### Always Set Limits

Always include a hard limit to prevent runaway execution:

```
|  |  |
| --- | --- |
| 1 | stopWhen: [ |
| 2 | stepCountIs(100),    // Hard limit |
| 3 | maxCost(10.00),      // Budget limit |
| 4 | customCondition,     // Your logic |
| 5 | ], |
```

### Log Stop Reasons

Track why execution stopped:

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Task', |
| 4 | tools: [taskTool], |
| 5 | stopWhen: ({ steps }) => { |
| 6 | if (steps.length >= 10) { |
| 7 | console.log('Stopped: step limit'); |
| 8 | return true; |
| 9 | } |
| 10 | const totalCost = steps.reduce((sum, step) => sum + (step.cost ?? 0), 0); |
| 11 | if (totalCost >= 1.00) { |
| 12 | console.log('Stopped: cost limit'); |
| 13 | return true; |
| 14 | } |
| 15 | return false; |
| 16 | }, |
| 17 | }); |
```

### Test Conditions

Verify conditions work as expected:

```
|  |  |
| --- | --- |
| 1 | // Test with low limits first |
| 2 | const testResult = openrouter.callModel({ |
| 3 | model: 'openai/gpt-5-nano', |
| 4 | input: 'Test task', |
| 5 | tools: [testTool], |
| 6 | stopWhen: stepCountIs(2), // Low limit for testing |
| 7 | }); |
```

## See Also

- **[Tools](../../../call-model/tools/index.md)** - Multi-turn orchestration
- **[Dynamic Parameters](../../../call-model/dynamic-parameters/index.md)** - Adaptive behavior
- **[nextTurnParams](../../../call-model/next-turn-params/index.md)** - Tool-driven modifications
