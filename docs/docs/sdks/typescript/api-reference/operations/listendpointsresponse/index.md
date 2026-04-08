---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listendpointsresponse"
title: "ListEndpointsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.806194+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListEndpointsResponse - TypeScript SDK

ListEndpointsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Returns a list of endpoints

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListEndpointsResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListEndpointsResponse = { |
| 4 | data: { |
| 5 | id: "openai/gpt-4", |
| 6 | name: "GPT-4", |
| 7 | created: 1692901234, |
| 8 | description: |
| 9 | "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.", |
| 10 | architecture: { |
| 11 | tokenizer: "GPT", |
| 12 | instructType: "chatml", |
| 13 | modality: "text->text", |
| 14 | inputModalities: [ |
| 15 | "text", |
| 16 | ], |
| 17 | outputModalities: [ |
| 18 | "text", |
| 19 | ], |
| 20 | }, |
| 21 | endpoints: [ |
| 22 | { |
| 23 | name: "OpenAI: GPT-4", |
| 24 | modelId: "openai/gpt-4", |
| 25 | modelName: "GPT-4", |
| 26 | contextLength: 8192, |
| 27 | pricing: { |
| 28 | prompt: "0.00003", |
| 29 | completion: "0.00006", |
| 30 | }, |
| 31 | providerName: "OpenAI", |
| 32 | tag: "openai", |
| 33 | quantization: "fp16", |
| 34 | maxCompletionTokens: 4096, |
| 35 | maxPromptTokens: 8192, |
| 36 | supportedParameters: [ |
| 37 | "temperature", |
| 38 | "top_p", |
| 39 | "max_tokens", |
| 40 | ], |
| 41 | uptimeLast30m: 99.5, |
| 42 | uptimeLast5m: 100, |
| 43 | uptimeLast1d: 99.8, |
| 44 | supportsImplicitCaching: true, |
| 45 | latencyLast30m: { |
| 46 | p50: 0.25, |
| 47 | p75: 0.35, |
| 48 | p90: 0.48, |
| 49 | p99: 0.85, |
| 50 | }, |
| 51 | throughputLast30m: { |
| 52 | p50: 45.2, |
| 53 | p75: 38.5, |
| 54 | p90: 28.3, |
| 55 | p99: 15.1, |
| 56 | }, |
| 57 | }, |
| 58 | ], |
| 59 | }, |
| 60 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.ListEndpointsResponse](../../models/listendpointsresponse/index.md) | ✔️ | List of available endpoints for a model | `{"id": "openai/gpt-4","name": "GPT-4","created": 1692901234,"description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.","architecture": {"tokenizer": "GPT","instruct_type": "chatml","modality": "text-\u003etext","input_modalities": ["text"],"output_modalities": ["text"]}`, “endpoints”: [ `{"name": "OpenAI: GPT-4","model_name": "GPT-4","context_length": 8192,"pricing": {"prompt": "0.00003","completion": "0.00006","request": "0","image": "0"}`, “provider\_name”: “OpenAI”, “tag”: “openai”, “quantization”: “fp16”, “max\_completion\_tokens”: 4096, “max\_prompt\_tokens”: 8192, “supported\_parameters”: [ “temperature”, “top\_p”, “max\_tokens”, “frequency\_penalty”, “presence\_penalty” ], “status”: “default”, “uptime\_last\_30m”: 99.5, “uptime\_last\_5m”: 100, “uptime\_last\_1d”: 99.8, “supports\_implicit\_caching”: true, “latency\_last\_30m”: `{"p50": 0.25,"p75": 0.35,"p90": 0.48,"p99": 0.85}`, “throughput\_last\_30m”: `{"p50": 45.2,"p75": 38.5,"p90": 28.3,"p99": 15.1}` } ] } |
