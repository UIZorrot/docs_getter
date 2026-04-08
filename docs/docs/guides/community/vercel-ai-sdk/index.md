---
source_url: "https://openrouter.ai/docs/guides/community/vercel-ai-sdk"
title: "Vercel AI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:55.393351+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Vercel AI SDK

Using OpenRouter with Vercel AI SDK

## Vercel AI SDK

You can use the [Vercel AI SDK](https://www.npmjs.com/package/ai) to integrate OpenRouter with your Next.js app. To get started, install [@openrouter/ai-sdk-provider](https://github.com/OpenRouterTeam/ai-sdk-provider):

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/ai-sdk-provider |
```

And then you can use [streamText()](https://sdk.vercel.ai/docs/reference/ai-sdk-core/stream-text) API to stream text from OpenRouter.

TypeScript

```
|  |  |
| --- | --- |
| 1 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 2 | import { streamText } from 'ai'; |
| 3 | import { z } from 'zod'; |
| 4 |  |
| 5 | export const getLasagnaRecipe = async (modelName: string) => { |
| 6 | const openrouter = createOpenRouter({ |
| 7 | apiKey: '${API_KEY_REF}', |
| 8 | }); |
| 9 |  |
| 10 | const response = streamText({ |
| 11 | model: openrouter(modelName), |
| 12 | prompt: 'Write a vegetarian lasagna recipe for 4 people.', |
| 13 | }); |
| 14 |  |
| 15 | await response.consumeStream(); |
| 16 | return response.text; |
| 17 | }; |
| 18 |  |
| 19 | export const getWeather = async (modelName: string) => { |
| 20 | const openrouter = createOpenRouter({ |
| 21 | apiKey: '${API_KEY_REF}', |
| 22 | }); |
| 23 |  |
| 24 | const response = streamText({ |
| 25 | model: openrouter(modelName), |
| 26 | prompt: 'What is the weather in San Francisco, CA in Fahrenheit?', |
| 27 | tools: { |
| 28 | getCurrentWeather: { |
| 29 | description: 'Get the current weather in a given location', |
| 30 | parameters: z.object({ |
| 31 | location: z |
| 32 | .string() |
| 33 | .describe('The city and state, e.g. San Francisco, CA'), |
| 34 | unit: z.enum(['celsius', 'fahrenheit']).optional(), |
| 35 | }), |
| 36 | execute: async ({ location, unit = 'celsius' }) => { |
| 37 | // Mock response for the weather |
| 38 | const weatherData = { |
| 39 | 'Boston, MA': { |
| 40 | celsius: '15°C', |
| 41 | fahrenheit: '59°F', |
| 42 | }, |
| 43 | 'San Francisco, CA': { |
| 44 | celsius: '18°C', |
| 45 | fahrenheit: '64°F', |
| 46 | }, |
| 47 | }; |
| 48 |  |
| 49 | const weather = weatherData[location]; |
| 50 | if (!weather) { |
| 51 | return `Weather data for ${location} is not available.`; |
| 52 | } |
| 53 |  |
| 54 | return `The current weather in ${location} is ${weather[unit]}.`; |
| 55 | }, |
| 56 | }, |
| 57 | }, |
| 58 | }); |
| 59 |  |
| 60 | await response.consumeStream(); |
| 61 | return response.text; |
| 62 | }; |
```
