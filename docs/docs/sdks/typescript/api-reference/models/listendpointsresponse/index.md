---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/listendpointsresponse"
title: "ListEndpointsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.534633+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ListEndpointsResponse - TypeScript SDK

ListEndpointsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

List of available endpoints for a model

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListEndpointsResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ListEndpointsResponse = { |
| 4 | id: "openai/gpt-4", |
| 5 | name: "GPT-4", |
| 6 | created: 1692901234, |
| 7 | description: |
| 8 | "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.", |
| 9 | architecture: { |
| 10 | tokenizer: "GPT", |
| 11 | instructType: "chatml", |
| 12 | modality: "text->text", |
| 13 | inputModalities: [ |
| 14 | "text", |
| 15 | ], |
| 16 | outputModalities: [ |
| 17 | "text", |
| 18 | ], |
| 19 | }, |
| 20 | endpoints: [ |
| 21 | { |
| 22 | name: "OpenAI: GPT-4", |
| 23 | modelId: "openai/gpt-4", |
| 24 | modelName: "GPT-4", |
| 25 | contextLength: 8192, |
| 26 | pricing: { |
| 27 | prompt: "0.00003", |
| 28 | completion: "0.00006", |
| 29 | }, |
| 30 | providerName: "OpenAI", |
| 31 | tag: "openai", |
| 32 | quantization: "fp16", |
| 33 | maxCompletionTokens: 4096, |
| 34 | maxPromptTokens: 8192, |
| 35 | supportedParameters: [ |
| 36 | "temperature", |
| 37 | "top_p", |
| 38 | "max_tokens", |
| 39 | "frequency_penalty", |
| 40 | "presence_penalty", |
| 41 | ], |
| 42 | uptimeLast30m: 99.5, |
| 43 | uptimeLast5m: 100, |
| 44 | uptimeLast1d: 99.8, |
| 45 | supportsImplicitCaching: true, |
| 46 | latencyLast30m: { |
| 47 | p50: 0.25, |
| 48 | p75: 0.35, |
| 49 | p90: 0.48, |
| 50 | p99: 0.85, |
| 51 | }, |
| 52 | throughputLast30m: { |
| 53 | p50: 45.2, |
| 54 | p75: 38.5, |
| 55 | p90: 28.3, |
| 56 | p99: 15.1, |
| 57 | }, |
| 58 | }, |
| 59 | ], |
| 60 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the model | openai/gpt-4 |
| `name` | *string* | ✔️ | Display name of the model | GPT-4 |
| `created` | *number* | ✔️ | Unix timestamp of when the model was created | 1692901234 |
| `description` | *string* | ✔️ | Description of the model | GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy. |
| `architecture` | [models.Architecture](../architecture/index.md) | ✔️ | N/A | `{"tokenizer": "GPT","instruct_type": "chatml","modality": "text"}` |
| `endpoints` | [models.PublicEndpoint](../publicendpoint/index.md)[] | ✔️ | List of available endpoints for this model |  |
