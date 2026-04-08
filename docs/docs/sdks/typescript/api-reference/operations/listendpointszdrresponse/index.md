---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listendpointszdrresponse"
title: "ListEndpointsZdrResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.994193+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListEndpointsZdrResponse - TypeScript SDK

ListEndpointsZdrResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Returns a list of endpoints

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListEndpointsZdrResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListEndpointsZdrResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | name: "OpenAI: GPT-4", |
| 7 | modelId: "openai/gpt-4", |
| 8 | modelName: "GPT-4", |
| 9 | contextLength: 8192, |
| 10 | pricing: { |
| 11 | prompt: "0.00003", |
| 12 | completion: "0.00006", |
| 13 | }, |
| 14 | providerName: "OpenAI", |
| 15 | tag: "openai", |
| 16 | quantization: "fp16", |
| 17 | maxCompletionTokens: 4096, |
| 18 | maxPromptTokens: 8192, |
| 19 | supportedParameters: [ |
| 20 | "temperature", |
| 21 | "top_p", |
| 22 | "max_tokens", |
| 23 | ], |
| 24 | uptimeLast30m: 99.5, |
| 25 | uptimeLast5m: 100, |
| 26 | uptimeLast1d: 99.8, |
| 27 | supportsImplicitCaching: true, |
| 28 | latencyLast30m: { |
| 29 | p50: 0.25, |
| 30 | p75: 0.35, |
| 31 | p90: 0.48, |
| 32 | p99: 0.85, |
| 33 | }, |
| 34 | throughputLast30m: { |
| 35 | p50: 45.2, |
| 36 | p75: 38.5, |
| 37 | p90: 28.3, |
| 38 | p99: 15.1, |
| 39 | }, |
| 40 | }, |
| 41 | ], |
| 42 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | [models.PublicEndpoint](../../models/publicendpoint/index.md)[] | ✔️ | N/A |
