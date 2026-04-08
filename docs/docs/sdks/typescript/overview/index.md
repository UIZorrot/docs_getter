---
source_url: "https://openrouter.ai/docs/sdks/typescript/overview"
title: "OpenRouter TypeScript SDK | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:50.822357+00:00"
---
[TypeScript SDK](index.md)

# TypeScript SDK

Official OpenRouter TypeScript SDK documentation

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

The OpenRouter TypeScript SDK is a type-safe toolkit for building AI applications with access to 300+ language models through a unified API.

## Why use the OpenRouter SDK?

Integrating AI models into applications involves handling different provider APIs, managing model-specific requirements, and avoiding common implementation mistakes. The OpenRouter SDK standardizes these integrations and protects you from footguns.

```
|  |  |
| --- | --- |
| 1 | import OpenRouter from '@openrouter/sdk'; |
| 2 |  |
| 3 | const client = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY |
| 5 | }); |
| 6 |  |
| 7 | const response = await client.chat.send({ |
| 8 | model: "minimax/minimax-m2", |
| 9 | messages: [ |
| 10 | { role: "user", content: "Explain quantum computing" } |
| 11 | ] |
| 12 | }); |
```

The SDK provides three core benefits:

### Auto-generated from API specifications

The SDK is automatically generated from OpenRouter’s OpenAPI specs and updated with every API change. New models, parameters, and features appear in your IDE autocomplete immediately. No manual updates. No version drift.

```
|  |  |
| --- | --- |
| 1 | // When new models launch, they're available instantly |
| 2 | const response = await client.chat.send({ |
| 3 | model: "minimax/minimax-m2", |
| 4 | }); |
```

### Type-safe by default

Every parameter, response field, and configuration option is fully typed. Invalid configurations are caught at compile time, not in production.

```
|  |  |
| --- | --- |
| 1 | const response = await client.chat.send({ |
| 2 | model: "minimax/minimax-m2", |
| 3 | messages: [ |
| 4 | { role: "user", content: "Hello" } |
| 5 | // ← Your IDE validates message structure |
| 6 | ], |
| 7 | temperature: 0.7, // ← Type-checked |
| 8 | stream: true      // ← Response type changes based on this |
| 9 | }); |
```

**Actionable error messages:**

```
|  |  |
| --- | --- |
| 1 | // Instead of generic errors, get specific guidance: |
| 2 | // "Model 'openai/o1-preview' requires at least 2 messages. |
| 3 | //  You provided 1 message. Add a system or user message." |
```

**Type-safe streaming:**

```
|  |  |
| --- | --- |
| 1 | const stream = await client.chat.send({ |
| 2 | model: "minimax/minimax-m2", |
| 3 | messages: [{ role: "user", content: "Write a story" }], |
| 4 | stream: true |
| 5 | }); |
| 6 |  |
| 7 | for await (const chunk of stream) { |
| 8 | // Full type information for streaming responses |
| 9 | const content = chunk.choices[0]?.delta?.content; |
| 10 | } |
```

## Installation

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/sdk |
```

Get your API key from [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

## Quick start

```
|  |  |
| --- | --- |
| 1 | import OpenRouter from '@openrouter/sdk'; |
| 2 |  |
| 3 | const client = new OpenRouter({ |
| 4 | apiKey: process.env.OPENROUTER_API_KEY |
| 5 | }); |
| 6 |  |
| 7 | const response = await client.chat.send({ |
| 8 | model: "minimax/minimax-m2", |
| 9 | messages: [ |
| 10 | { role: "user", content: "Hello!" } |
| 11 | ] |
| 12 | }); |
| 13 |  |
| 14 | console.log(response.choices[0].message.content); |
```
