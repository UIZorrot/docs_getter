---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/publicendpoint"
title: "PublicEndpoint Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.349526+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

PublicEndpoint - TypeScript SDK

PublicEndpoint type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Information about a specific model endpoint

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { PublicEndpoint } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: PublicEndpoint = { |
| 4 | name: "OpenAI: GPT-4", |
| 5 | modelId: "openai/gpt-4", |
| 6 | modelName: "GPT-4", |
| 7 | contextLength: 8192, |
| 8 | pricing: { |
| 9 | prompt: "0.00003", |
| 10 | completion: "0.00006", |
| 11 | }, |
| 12 | providerName: "OpenAI", |
| 13 | tag: "openai", |
| 14 | quantization: "fp16", |
| 15 | maxCompletionTokens: 4096, |
| 16 | maxPromptTokens: 8192, |
| 17 | supportedParameters: [ |
| 18 | "temperature", |
| 19 | "top_p", |
| 20 | "max_tokens", |
| 21 | ], |
| 22 | uptimeLast30m: 99.5, |
| 23 | uptimeLast5m: 100, |
| 24 | uptimeLast1d: 99.8, |
| 25 | supportsImplicitCaching: true, |
| 26 | latencyLast30m: { |
| 27 | p50: 0.25, |
| 28 | p75: 0.35, |
| 29 | p90: 0.48, |
| 30 | p99: 0.85, |
| 31 | }, |
| 32 | throughputLast30m: { |
| 33 | p50: 45.2, |
| 34 | p75: 38.5, |
| 35 | p90: 28.3, |
| 36 | p99: 15.1, |
| 37 | }, |
| 38 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ✔️ | N/A |  |
| `modelId` | *string* | ✔️ | The unique identifier for the model (permaslug) | openai/gpt-4 |
| `modelName` | *string* | ✔️ | N/A |  |
| `contextLength` | *number* | ✔️ | N/A |  |
| `pricing` | [models.Pricing](../pricing/index.md) | ✔️ | N/A |  |
| `providerName` | [models.ProviderName](../providername/index.md) | ✔️ | N/A | OpenAI |
| `tag` | *string* | ✔️ | N/A |  |
| `quantization` | [models.PublicEndpointQuantization](../publicendpointquantization/index.md) | ✔️ | N/A | fp16 |
| `maxCompletionTokens` | *number* | ✔️ | N/A |  |
| `maxPromptTokens` | *number* | ✔️ | N/A |  |
| `supportedParameters` | [models.Parameter](../parameter/index.md)[] | ✔️ | N/A |  |
| `status` | [models.EndpointStatus](../endpointstatus/index.md) | ➖ | N/A | 0 |
| `uptimeLast30m` | *number* | ✔️ | N/A |  |
| `uptimeLast5m` | *number* | ✔️ | Uptime percentage over the last 5 minutes, calculated as successful requests / (successful + error requests) \* 100. Rate-limited requests are excluded. Returns null if insufficient data. |  |
| `uptimeLast1d` | *number* | ✔️ | Uptime percentage over the last 1 day, calculated as successful requests / (successful + error requests) \* 100. Rate-limited requests are excluded. Returns null if insufficient data. |  |
| `supportsImplicitCaching` | *boolean* | ✔️ | N/A |  |
| `latencyLast30m` | [models.PercentileStats](../percentilestats/index.md) | ✔️ | Latency percentiles in milliseconds over the last 30 minutes. Latency measures time to first token. Only visible when authenticated with an API key or cookie; returns null for unauthenticated requests. | `{"p50": 25.5,"p75": 35.2,"p90": 48.7,"p99": 85.3}` |
| `throughputLast30m` | [models.PercentileStats](../percentilestats/index.md) | ✔️ | N/A | `{"p50": 25.5,"p75": 35.2,"p90": 48.7,"p99": 85.3}` |
