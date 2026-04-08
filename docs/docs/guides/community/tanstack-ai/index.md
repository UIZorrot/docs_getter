---
source_url: "https://openrouter.ai/docs/guides/community/tanstack-ai"
title: "TanStack AI Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:35.365570+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# TanStack AI

Using OpenRouter with TanStack AI

## TanStack AI

You can use [TanStack AI](https://tanstack.com/ai) to integrate OpenRouter with your React, Solid, or Preact applications. The OpenRouter adapter provides access to 300+ AI models from various providers through a single unified API. To get started, install [@tanstack/ai-openrouter](https://www.npmjs.com/package/@tanstack/ai-openrouter):

```
|  |  |
| --- | --- |
| $ | npm install @tanstack/ai @tanstack/ai-openrouter |
```

### Basic Usage

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("openai/gpt-5.2"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | }); |
```

### Configuration

You can configure the OpenRouter adapter with additional options:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { createOpenRouter, type OpenRouterConfig } from "@tanstack/ai-openrouter"; |
| 2 |  |
| 3 | const config: OpenRouterConfig = { |
| 4 | apiKey: process.env.OPENROUTER_API_KEY!, |
| 5 | baseURL: "https://openrouter.ai/api/v1", // Optional |
| 6 | httpReferer: "https://your-app.com", // Optional, for rankings |
| 7 | xTitle: "Your App Name", // Optional, for rankings |
| 8 | }; |
| 9 |  |
| 10 | const adapter = createOpenRouter(config.apiKey, config); |
```

### Available Models

OpenRouter provides access to 300+ models from various providers. Models use the format `provider/model-name`:

```
|  |  |
| --- | --- |
| 1 | model: "openai/gpt-5.2" |
| 2 | model: "anthropic/claude-sonnet-4.5" |
| 3 | model: "google/gemini-3.1-pro-preview" |
| 4 | model: "z-ai/glm-4.7" |
| 5 | model: "minimax/minimax-m2.1" |
```

See the full list at [openrouter.ai/models](https://openrouter.ai/models).

### Server-Side Example

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat, toServerSentEventsResponse } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | export async function POST(request: Request) { |
| 5 | const { messages } = await request.json(); |
| 6 |  |
| 7 | const stream = chat({ |
| 8 | adapter: openRouterText("openai/gpt-5.2"), |
| 9 | messages, |
| 10 | }); |
| 11 |  |
| 12 | return toServerSentEventsResponse(stream); |
| 13 | } |
```

### Using Tools

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat, toolDefinition } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 | import { z } from "zod"; |
| 4 |  |
| 5 | const getWeatherDef = toolDefinition({ |
| 6 | name: "get_weather", |
| 7 | description: "Get the current weather", |
| 8 | inputSchema: z.object({ |
| 9 | location: z.string(), |
| 10 | }), |
| 11 | }); |
| 12 |  |
| 13 | const getWeather = getWeatherDef.server(async ({ location }) => { |
| 14 | return { temperature: 72, conditions: "sunny" }; |
| 15 | }); |
| 16 |  |
| 17 | const messages = [{ role: "user", content: "What's the weather in NYC?" }]; |
| 18 |  |
| 19 | const stream = chat({ |
| 20 | adapter: openRouterText("openai/gpt-5.2"), |
| 21 | messages, |
| 22 | tools: [getWeather], |
| 23 | }); |
```

### Environment Variables

Set your API key in environment variables:

```
|  |  |
| --- | --- |
| $ | OPENROUTER_API_KEY=sk-or-... |
```

### Model Routing and Provider Preferences

TanStack AI supports OpenRouter’s powerful routing features through the `modelOptions` parameter. You can configure model fallbacks, provider sorting, and data policies.

#### Model Fallbacks

Specify backup models to try if the primary model is unavailable:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("openai/gpt-5.2"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | modelOptions: { |
| 8 | models: ["anthropic/claude-sonnet-4.5", "google/gemini-3.1-pro-preview"], |
| 9 | route: "fallback", |
| 10 | }, |
| 11 | }); |
```

#### Provider Sorting

Sort providers by price, throughput, or latency instead of using the default load balancing:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | // Prioritize fastest providers |
| 5 | const stream = chat({ |
| 6 | adapter: openRouterText("openai/gpt-5.2"), |
| 7 | messages: [{ role: "user", content: "Hello!" }], |
| 8 | modelOptions: { |
| 9 | provider: { |
| 10 | sort: "throughput", |
| 11 | }, |
| 12 | }, |
| 13 | }); |
```

#### Provider Ordering

Specify an explicit order of providers to try:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("anthropic/claude-sonnet-4.5"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | modelOptions: { |
| 8 | provider: { |
| 9 | order: ["anthropic", "amazon-bedrock", "google-vertex"], |
| 10 | allow_fallbacks: true, |
| 11 | }, |
| 12 | }, |
| 13 | }); |
```

#### Data Privacy Controls

Control data collection and use Zero Data Retention (ZDR) providers:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("openai/gpt-5.2"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | modelOptions: { |
| 8 | provider: { |
| 9 | data_collection: "deny", |
| 10 | zdr: true, |
| 11 | }, |
| 12 | }, |
| 13 | }); |
```

#### Filtering Providers

Include or exclude specific providers:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("meta-llama/llama-3.3-70b-instruct"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | modelOptions: { |
| 8 | provider: { |
| 9 | only: ["together", "fireworks"], |
| 10 | ignore: ["azure"], |
| 11 | quantizations: ["fp16", "bf16"], |
| 12 | }, |
| 13 | }, |
| 14 | }); |
```

#### Cost Controls

Set maximum price limits for requests:

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { chat } from "@tanstack/ai"; |
| 2 | import { openRouterText } from "@tanstack/ai-openrouter"; |
| 3 |  |
| 4 | const stream = chat({ |
| 5 | adapter: openRouterText("z-ai/glm-4.7"), |
| 6 | messages: [{ role: "user", content: "Hello!" }], |
| 7 | modelOptions: { |
| 8 | provider: { |
| 9 | max_price: { |
| 10 | prompt: 0.5, |
| 11 | completion: 2, |
| 12 | }, |
| 13 | }, |
| 14 | }, |
| 15 | }); |
```

For more advanced routing options like performance thresholds and partition-based sorting, see the [Provider Routing documentation](../../routing/provider-selection/index.md).

### Resources

For more information and detailed documentation, check out these resources:

- [TanStack AI Documentation](https://tanstack.com/ai/latest/docs/getting-started/overview) - Learn the basics of TanStack AI
- [OpenRouter Adapter Docs](https://tanstack.com/ai/latest/docs/adapters/openrouter) - Official TanStack AI OpenRouter adapter documentation
- [OpenRouter Models](https://openrouter.ai/models) - Browse available models
