---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getgenerationdata"
title: "GetGenerationData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.672709+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetGenerationData - TypeScript SDK

GetGenerationData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Generation data

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetGenerationData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetGenerationData = { |
| 4 | id: "gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG", |
| 5 | upstreamId: "chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946", |
| 6 | totalCost: 0.0015, |
| 7 | cacheDiscount: 0.0002, |
| 8 | upstreamInferenceCost: 0.0012, |
| 9 | createdAt: "2024-07-15T23:33:19.433273+00:00", |
| 10 | model: "sao10k/l3-stheno-8b", |
| 11 | appId: 12345, |
| 12 | streamed: true, |
| 13 | cancelled: false, |
| 14 | providerName: "Infermatic", |
| 15 | latency: 1250, |
| 16 | moderationLatency: 50, |
| 17 | generationTime: 1200, |
| 18 | finishReason: "stop", |
| 19 | tokensPrompt: 10, |
| 20 | tokensCompletion: 25, |
| 21 | nativeTokensPrompt: 10, |
| 22 | nativeTokensCompletion: 25, |
| 23 | nativeTokensCompletionImages: 0, |
| 24 | nativeTokensReasoning: 5, |
| 25 | nativeTokensCached: 3, |
| 26 | numMediaPrompt: 1, |
| 27 | numInputAudioPrompt: 0, |
| 28 | numMediaCompletion: 0, |
| 29 | numSearchResults: 5, |
| 30 | origin: "https://openrouter.ai/", |
| 31 | usage: 0.0015, |
| 32 | isByok: false, |
| 33 | nativeFinishReason: "stop", |
| 34 | externalUser: "user-123", |
| 35 | apiType: "embeddings", |
| 36 | router: "openrouter/auto", |
| 37 | providerResponses: [ |
| 38 | { |
| 39 | status: 200, |
| 40 | }, |
| 41 | ], |
| 42 | userAgent: "<value>", |
| 43 | httpReferer: "<value>", |
| 44 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the generation | gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG |
| `upstreamId` | *string* | ✔️ | Upstream provider’s identifier for this generation | chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946 |
| `totalCost` | *number* | ✔️ | Total cost of the generation in USD | 0.0015 |
| `cacheDiscount` | *number* | ✔️ | Discount applied due to caching | 0.0002 |
| `upstreamInferenceCost` | *number* | ✔️ | Cost charged by the upstream provider | 0.0012 |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the generation was created | 2024-07-15T23:33:19.433273+00:00 |
| `model` | *string* | ✔️ | Model used for the generation | sao10k/l3-stheno-8b |
| `appId` | *number* | ✔️ | ID of the app that made the request | 12345 |
| `streamed` | *boolean* | ✔️ | Whether the response was streamed | true |
| `cancelled` | *boolean* | ✔️ | Whether the generation was cancelled | false |
| `providerName` | *string* | ✔️ | Name of the provider that served the request | Infermatic |
| `latency` | *number* | ✔️ | Total latency in milliseconds | 1250 |
| `moderationLatency` | *number* | ✔️ | Moderation latency in milliseconds | 50 |
| `generationTime` | *number* | ✔️ | Time taken for generation in milliseconds | 1200 |
| `finishReason` | *string* | ✔️ | Reason the generation finished | stop |
| `tokensPrompt` | *number* | ✔️ | Number of tokens in the prompt | 10 |
| `tokensCompletion` | *number* | ✔️ | Number of tokens in the completion | 25 |
| `nativeTokensPrompt` | *number* | ✔️ | Native prompt tokens as reported by provider | 10 |
| `nativeTokensCompletion` | *number* | ✔️ | Native completion tokens as reported by provider | 25 |
| `nativeTokensCompletionImages` | *number* | ✔️ | Native completion image tokens as reported by provider | 0 |
| `nativeTokensReasoning` | *number* | ✔️ | Native reasoning tokens as reported by provider | 5 |
| `nativeTokensCached` | *number* | ✔️ | Native cached tokens as reported by provider | 3 |
| `numMediaPrompt` | *number* | ✔️ | Number of media items in the prompt | 1 |
| `numInputAudioPrompt` | *number* | ✔️ | Number of audio inputs in the prompt | 0 |
| `numMediaCompletion` | *number* | ✔️ | Number of media items in the completion | 0 |
| `numSearchResults` | *number* | ✔️ | Number of search results included | 5 |
| `origin` | *string* | ✔️ | Origin URL of the request | [https://openrouter.ai/](https://openrouter.ai/) |
| `usage` | *number* | ✔️ | Usage amount in USD | 0.0015 |
| `isByok` | *boolean* | ✔️ | Whether this used bring-your-own-key | false |
| `nativeFinishReason` | *string* | ✔️ | Native finish reason as reported by provider | stop |
| `externalUser` | *string* | ✔️ | External user identifier | user-123 |
| `apiType` | [operations.ApiType](../apitype/index.md) | ✔️ | Type of API used for the generation |  |
| `router` | *string* | ✔️ | Router used for the request (e.g., openrouter/auto) | openrouter/auto |
| `providerResponses` | [models.ProviderResponse](../../models/providerresponse/index.md)[] | ✔️ | List of provider responses for this generation, including fallback attempts |  |
| `userAgent` | *string* | ✔️ | User-Agent header from the request |  |
| `httpReferer` | *string* | ✔️ | Referer header from the request |  |
| `requestId` | *string* | ➖ | Unique identifier grouping all generations from a single API request | req-1727282430-aBcDeFgHiJkLmNoPqRsT |
| `sessionId` | *string* | ➖ | Session identifier grouping multiple generations in the same session |  |
