---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getgenerationresponse"
title: "GetGenerationResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.630101+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetGenerationResponse - TypeScript SDK

GetGenerationResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Generation response

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetGenerationResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetGenerationResponse = { |
| 4 | data: { |
| 5 | id: "gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG", |
| 6 | upstreamId: "chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946", |
| 7 | totalCost: 0.0015, |
| 8 | cacheDiscount: 0.0002, |
| 9 | upstreamInferenceCost: 0.0012, |
| 10 | createdAt: "2024-07-15T23:33:19.433273+00:00", |
| 11 | model: "sao10k/l3-stheno-8b", |
| 12 | appId: 12345, |
| 13 | streamed: true, |
| 14 | cancelled: false, |
| 15 | providerName: "Infermatic", |
| 16 | latency: 1250, |
| 17 | moderationLatency: 50, |
| 18 | generationTime: 1200, |
| 19 | finishReason: "stop", |
| 20 | tokensPrompt: 10, |
| 21 | tokensCompletion: 25, |
| 22 | nativeTokensPrompt: 10, |
| 23 | nativeTokensCompletion: 25, |
| 24 | nativeTokensCompletionImages: 0, |
| 25 | nativeTokensReasoning: 5, |
| 26 | nativeTokensCached: 3, |
| 27 | numMediaPrompt: 1, |
| 28 | numInputAudioPrompt: 0, |
| 29 | numMediaCompletion: 0, |
| 30 | numSearchResults: 5, |
| 31 | origin: "https://openrouter.ai/", |
| 32 | usage: 0.0015, |
| 33 | isByok: false, |
| 34 | nativeFinishReason: "stop", |
| 35 | externalUser: "user-123", |
| 36 | apiType: null, |
| 37 | router: "openrouter/auto", |
| 38 | providerResponses: null, |
| 39 | userAgent: "<value>", |
| 40 | httpReferer: "<value>", |
| 41 | }, |
| 42 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | [operations.GetGenerationData](../getgenerationdata/index.md) | ✔️ | Generation data |
