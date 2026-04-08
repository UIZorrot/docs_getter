---
source_url: "https://openrouter.ai/docs/guides/community/effect-ai-sdk"
title: "Effect AI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:54.190529+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Effect AI SDK

Integrate OpenRouter using the Effect AI SDK

## Effect AI SDK

You can use the [Effect AI SDK](https://www.npmjs.com/package/@effect/ai) to integrate OpenRouter with your Effect applications. To get started, install the following packages:

- [effect](https://www.npmjs.com/package/effect): the Effect core (if not already installed)
- [@effect/ai](https://www.npmjs.com/package/@effect/ai): the core Effect AI SDK abstractions
- [@effect/ai-openrouter](https://www.npmjs.com/package/@effect/ai-openrouter): the Effect AI provider integration for OpenRouter
- [@effect/platform](https://www.npmjs.com/package/@effect/platform): platform-agnostic abstractions for Effect

```
|  |  |
| --- | --- |
| $ | npm install effect @effect/ai @effect/ai-openrouter @effect/platform |
```

Once that’s done you can use the [LanguageModel](https://effect.website/docs/ai/getting-started) module to define interactions with a large language model via OpenRouter.

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { LanguageModel } from "@effect/ai" |
| 2 | import { OpenRouterClient, OpenRouterLanguageModel } from "@effect/ai-openrouter" |
| 3 | import { FetchHttpClient } from "@effect/platform" |
| 4 | import { Config, Effect, Layer, Stream } from "effect" |
| 5 |  |
| 6 | const Gpt4o = OpenRouterLanguageModel.model("openai/gpt-4o") |
| 7 |  |
| 8 | const program = LanguageModel.streamText({ |
| 9 | prompt: [ |
| 10 | { role: "system", content: "You are a comedian with a penchant for groan-inducing puns" }, |
| 11 | { role: "user", content: [{ type: "text", text: "Tell me a dad joke" }] } |
| 12 | ] |
| 13 | }).pipe( |
| 14 | Stream.filter((part) => part.type === "text-delta"), |
| 15 | Stream.runForEach((part) => Effect.sync(() => process.stdout.write(part.delta))), |
| 16 | Effect.provide(Gpt4o) |
| 17 | ) |
| 18 |  |
| 19 | const OpenRouter = OpenRouterClient.layerConfig({ |
| 20 | apiKey: Config.redacted("OPENROUTER_API_KEY") |
| 21 | }).pipe(Layer.provide(FetchHttpClient.layer)) |
| 22 |  |
| 23 | program.pipe( |
| 24 | Effect.provide(OpenRouter), |
| 25 | Effect.runPromise |
| 26 | ) |
```
