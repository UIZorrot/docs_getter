---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/next-turn-params"
title: "Next Turn Params | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:09.667489+00:00"
---
[TypeScript SDK](../../overview/index.md)[Call Model](../overview/index.md)

# Next Turn Params

Build encapsulated, context-aware tools with `nextTurnParams`. Create skills systems, plugins, and adaptive multi-turn agents.

## Why nextTurnParams?

Traditional tool execution returns results to the model, but sometimes you need more:

- **Skills/Plugins**: Load domain-specific instructions when a skill is activated
- **Progressive Context**: Build up context as tools are used
- **Adaptive Behavior**: Adjust model parameters based on tool results
- **Clean Separation**: Tools manage their own context requirements

With `nextTurnParams`, tools can modify any `callModel` parameter for the next turn.

## Basic Example

```
|  |  |
| --- | --- |
| 1 | import { tool } from '@openrouter/agent'; |
| 2 | import { z } from 'zod'; |
| 3 |  |
| 4 | const expertModeTool = tool({ |
| 5 | name: 'enable_expert_mode', |
| 6 | description: 'Enable expert mode for detailed technical responses', |
| 7 | inputSchema: z.object({ |
| 8 | domain: z.string().describe('Technical domain (e.g., "kubernetes", "react")'), |
| 9 | }), |
| 10 | outputSchema: z.object({ enabled: z.boolean() }), |
| 11 |  |
| 12 | nextTurnParams: { |
| 13 | instructions: (params, context) => { |
| 14 | const base = context.instructions ?? ''; |
| 15 | return `${base} |
| 16 |  |
| 17 | EXPERT MODE ENABLED for ${params.domain}: |
| 18 | - Provide detailed technical explanations |
| 19 | - Include code examples and best practices |
| 20 | - Reference official documentation |
| 21 | - Assume advanced knowledge`; |
| 22 | }, |
| 23 | temperature: () => 0.3, // More precise for technical content |
| 24 | }, |
| 25 |  |
| 26 | execute: async (params) => { |
| 27 | return { enabled: true }; |
| 28 | }, |
| 29 | }); |
```

## The Claude Code Skills Pattern

This example shows how to recreate Claude Code’s skills system as a single encapsulated tool:

```
|  |  |
| --- | --- |
| 1 | import { tool } from '@openrouter/agent'; |
| 2 | import { readFileSync } from 'fs'; |
| 3 | import { z } from 'zod'; |
| 4 |  |
| 5 | const skillsTool = tool({ |
| 6 | name: "skill", |
| 7 | description: `Load a specialized skill to enhance the assistant's capabilities. |
| 8 | Available skills: pdf-processing, data-analysis, code-review, etc. |
| 9 | Each skill provides domain-specific instructions and capabilities.`, |
| 10 | inputSchema: z.object({ |
| 11 | type: z.string().describe("The skill type to load (e.g., 'pdf-processing')"), |
| 12 | }), |
| 13 | outputSchema: z.string(), |
| 14 |  |
| 15 | // nextTurnParams runs after all tool calls execute, before responses go to model |
| 16 | // Executed in order of tools array. This is where the magic happens. |
| 17 | nextTurnParams: { |
| 18 | input: (params, context) => { |
| 19 | // Prevent duplicate skill loading |
| 20 | if (JSON.stringify(context.input).includes(`Skill ${params.type} is already loaded`)) { |
| 21 | return context.input; |
| 22 | } |
| 23 |  |
| 24 | // Load the skill's instructions from file system |
| 25 | const skill = readFileSync( |
| 26 | `~/.claude/skills/${params.type}/SKILL.md`, |
| 27 | "utf-8" |
| 28 | ); |
| 29 |  |
| 30 | // Inject skill context into the conversation |
| 31 | return [ |
| 32 | ...context.input, |
| 33 | { |
| 34 | role: "user", |
| 35 | content: `Base directory for this skill: ~/.claude/skills/${params.type}/ |
| 36 |  |
| 37 | ${skill}`, |
| 38 | }, |
| 39 | ]; |
| 40 | }, |
| 41 | }, |
| 42 |  |
| 43 | execute: async (params, context) => { |
| 44 | // Check if already loaded |
| 45 | if (JSON.stringify(context.input).includes(`Skill ${params.type} is already loaded`)) { |
| 46 | return `Skill ${params.type} is already loaded`; |
| 47 | } |
| 48 |  |
| 49 | return `Launching skill ${params.type}`; |
| 50 | }, |
| 51 | }); |
| 52 |  |
| 53 | // Usage - the skill automatically enriches future turns |
| 54 | const result = openrouter.callModel({ |
| 55 | model: 'anthropic/claude-sonnet-4.5', |
| 56 | input: 'Process this PDF and extract the key findings', |
| 57 | tools: [skillsTool], |
| 58 | }); |
```

### Key Benefits

1. **Encapsulation**: Skill loading logic is entirely contained in the tool
2. **Idempotency**: Built-in check prevents loading the same skill twice
3. **Clean API**: Callers don’t need to know about skill file locations
4. **Composability**: Multiple skills can be loaded across turns

## Execution Order

Understanding when `nextTurnParams` runs is crucial:

```
|  |
| --- |
| 1. Model generates tool calls |
| ↓ |
| 2. All tool `execute` functions run |
| ↓ |
| 3. `nextTurnParams` functions run for each tool (in tools array order) |
| ↓ |
| 4. Modified parameters used for next model turn |
| ↓ |
| 5. Repeat until model stops calling tools |
```

## Available Context

`nextTurnParams` functions receive two arguments:

### params

The validated input parameters that were passed to the tool:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | instructions: (params, context) => { |
| 3 | // params is typed based on inputSchema |
| 4 | console.log(params.type); // e.g., "pdf-processing" |
| 5 | return `Handle ${params.type}`; |
| 6 | }, |
| 7 | }, |
```

### context

The current request context, including:

| Property | Type | Description |
| --- | --- | --- |
| `input` | `OpenResponsesInput` | Current message history |
| `model` | `string | undefined` | Current model selection |
| `models` | `string[] | undefined` | Model fallback array |
| `instructions` | `string | undefined` | Current system instructions |
| `temperature` | `number | undefined` | Current temperature |
| `maxOutputTokens` | `number | undefined` | Current max tokens |
| `topP` | `number | undefined` | Current top-p sampling |
| `topK` | `number | undefined` | Current top-k sampling |

## Modifiable Parameters

You can modify `CallModelInput` parameters:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | // Modify message history |
| 3 | input: (params, ctx) => [...ctx.input, newMessage], |
| 4 |  |
| 5 | // Change model |
| 6 | model: (params, ctx) => 'anthropic/claude-sonnet-4.5', |
| 7 |  |
| 8 | // Update instructions |
| 9 | instructions: (params, ctx) => `${ctx.instructions}\n\nNew context...`, |
| 10 |  |
| 11 | // Adjust generation parameters |
| 12 | temperature: (params, ctx) => 0.5, |
| 13 | maxOutputTokens: (params, ctx) => 2000, |
| 14 | }, |
```

## Patterns

### Research Context Accumulation

Build up context as research progresses:

```
|  |  |
| --- | --- |
| 1 | const researchTool = tool({ |
| 2 | name: "research", |
| 3 | inputSchema: z.object({ topic: z.string() }), |
| 4 | outputSchema: z.object({ findings: z.array(z.string()) }), |
| 5 |  |
| 6 | nextTurnParams: { |
| 7 | instructions: (params, context) => { |
| 8 | const base = context.instructions ?? ''; |
| 9 | return `${base} |
| 10 |  |
| 11 | Previous research on "${params.topic}" found important context. |
| 12 | Build upon these findings in your response.`; |
| 13 | }, |
| 14 | }, |
| 15 |  |
| 16 | execute: async (params) => { |
| 17 | const results = await searchDatabase(params.topic); |
| 18 | return { findings: results }; |
| 19 | }, |
| 20 | }); |
```

### Complexity-Based Model Selection

Upgrade to better models when needed:

```
|  |  |
| --- | --- |
| 1 | const complexityAnalyzer = tool({ |
| 2 | name: "analyze_complexity", |
| 3 | inputSchema: z.object({ code: z.string() }), |
| 4 | outputSchema: z.object({ complexity: z.enum(['low', 'medium', 'high']) }), |
| 5 |  |
| 6 | nextTurnParams: { |
| 7 | model: (params, context) => { |
| 8 | // Upgrade to more capable model for complex code |
| 9 | if (params.complexity === 'high') { |
| 10 | return 'anthropic/claude-sonnet-4.5'; |
| 11 | } |
| 12 | return context.model ?? 'openai/gpt-5-nano'; |
| 13 | }, |
| 14 | temperature: (params, context) => { |
| 15 | // Lower temperature for complex analysis |
| 16 | return params.complexity === 'high' ? 0.3 : 0.7; |
| 17 | }, |
| 18 | }, |
| 19 |  |
| 20 | execute: async (params) => { |
| 21 | return analyzeCodeComplexity(params.code); |
| 22 | }, |
| 23 | }); |
```

### Multi-Skill Loading

Load multiple skills at once:

```
|  |  |
| --- | --- |
| 1 | const multiSkillLoader = tool({ |
| 2 | name: 'load_skills', |
| 3 | description: 'Load multiple skills at once', |
| 4 | inputSchema: z.object({ |
| 5 | skills: z.array(z.string()).describe('Array of skill names to load'), |
| 6 | }), |
| 7 | outputSchema: z.object({ |
| 8 | loaded: z.array(z.string()), |
| 9 | failed: z.array(z.object({ name: z.string(), reason: z.string() })), |
| 10 | }), |
| 11 |  |
| 12 | nextTurnParams: { |
| 13 | input: (params, context) => { |
| 14 | let newInput = context.input; |
| 15 |  |
| 16 | for (const skillName of params.skills) { |
| 17 | const skillPath = `~/.skills/${skillName}/SKILL.md`; |
| 18 | if (!existsSync(skillPath)) continue; |
| 19 |  |
| 20 | const skillMarker = `[Skill: ${skillName}]`; |
| 21 | if (JSON.stringify(newInput).includes(skillMarker)) continue; |
| 22 |  |
| 23 | const skillContent = readFileSync(skillPath, 'utf-8'); |
| 24 | newInput = [ |
| 25 | ...(Array.isArray(newInput) ? newInput : [newInput]), |
| 26 | { role: 'user', content: `${skillMarker}\n${skillContent}` }, |
| 27 | ]; |
| 28 | } |
| 29 |  |
| 30 | return newInput; |
| 31 | }, |
| 32 | }, |
| 33 |  |
| 34 | execute: async ({ skills }) => { |
| 35 | const loaded = []; |
| 36 | const failed = []; |
| 37 |  |
| 38 | for (const skill of skills) { |
| 39 | if (existsSync(`~/.skills/${skill}/SKILL.md`)) { |
| 40 | loaded.push(skill); |
| 41 | } else { |
| 42 | failed.push({ name: skill, reason: 'Not found' }); |
| 43 | } |
| 44 | } |
| 45 |  |
| 46 | return { loaded, failed }; |
| 47 | }, |
| 48 | }); |
```

### Language/Locale Switching

Adapt to user language preferences:

```
|  |  |
| --- | --- |
| 1 | const languageTool = tool({ |
| 2 | name: 'set_language', |
| 3 | inputSchema: z.object({ |
| 4 | language: z.enum(['en', 'es', 'fr', 'de', 'ja']), |
| 5 | }), |
| 6 | outputSchema: z.object({ set: z.boolean() }), |
| 7 |  |
| 8 | nextTurnParams: { |
| 9 | instructions: (params, context) => { |
| 10 | const base = context.instructions ?? ''; |
| 11 | const languageInstructions = { |
| 12 | en: 'Respond in English.', |
| 13 | es: 'Responde en español.', |
| 14 | fr: 'Répondez en français.', |
| 15 | de: 'Antworten Sie auf Deutsch.', |
| 16 | ja: '日本語で回答してください。', |
| 17 | }; |
| 18 |  |
| 19 | return `${base}\n\n${languageInstructions[params.language]}`; |
| 20 | }, |
| 21 | }, |
| 22 |  |
| 23 | execute: async (params) => ({ set: true }), |
| 24 | }); |
```

## Best Practices

### Idempotency Checks

Always check if context was already added:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | input: (params, context) => { |
| 3 | const marker = `[Context: ${params.id}]`; |
| 4 |  |
| 5 | // Don't add if already present |
| 6 | if (JSON.stringify(context.input).includes(marker)) { |
| 7 | return context.input; |
| 8 | } |
| 9 |  |
| 10 | return [...context.input, { |
| 11 | role: 'user', |
| 12 | content: `${marker}\n${newContent}`, |
| 13 | }]; |
| 14 | }, |
| 15 | }, |
```

### Type Safety

Use proper typing for context access:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | instructions: (params, context) => { |
| 3 | // Safe access with fallback |
| 4 | const base = context.instructions ?? 'You are a helpful assistant.'; |
| 5 | return `${base}\n\nAdditional context: ${params.data}`; |
| 6 | }, |
| 7 | }, |
```

### Minimal Modifications

Only modify what’s necessary:

```
|  |  |
| --- | --- |
| 1 | // Good: Minimal, targeted change |
| 2 | nextTurnParams: { |
| 3 | temperature: (params) => params.needsPrecision ? 0.2 : undefined, |
| 4 | }, |
| 5 |  |
| 6 | // Avoid: Unnecessary spreading |
| 7 | nextTurnParams: { |
| 8 | temperature: (params, ctx) => { |
| 9 | return params.needsPrecision ? 0.2 : ctx.temperature; |
| 10 | }, |
| 11 | }, |
```

## See Also

- **[Skills Loader Example](../examples/skills-loader/index.md)** - Complete implementation
- **[Dynamic Parameters](../dynamic-parameters/index.md)** - Async parameter functions
- **[Stop Conditions](../stop-conditions/index.md)** - Execution control
