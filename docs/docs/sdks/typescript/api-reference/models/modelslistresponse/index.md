---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/modelslistresponse"
title: "ModelsListResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.095072+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ModelsListResponse - TypeScript SDK

ModelsListResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

List of available models

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ModelsListResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ModelsListResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | id: "openai/gpt-4", |
| 7 | canonicalSlug: "openai/gpt-4", |
| 8 | name: "GPT-4", |
| 9 | created: 1692901234, |
| 10 | pricing: { |
| 11 | prompt: "0.00003", |
| 12 | completion: "0.00006", |
| 13 | }, |
| 14 | contextLength: 8192, |
| 15 | architecture: { |
| 16 | modality: "text->text", |
| 17 | inputModalities: [ |
| 18 | "text", |
| 19 | ], |
| 20 | outputModalities: [ |
| 21 | "text", |
| 22 | ], |
| 23 | }, |
| 24 | topProvider: { |
| 25 | isModerated: true, |
| 26 | }, |
| 27 | perRequestLimits: null, |
| 28 | supportedParameters: [ |
| 29 | "temperature", |
| 30 | "top_p", |
| 31 | "max_tokens", |
| 32 | "frequency_penalty", |
| 33 | "presence_penalty", |
| 34 | ], |
| 35 | defaultParameters: null, |
| 36 | links: { |
| 37 | details: "/api/v1/models/openai/gpt-5.4/endpoints", |
| 38 | }, |
| 39 | }, |
| 40 | ], |
| 41 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.Model](../model/index.md)[] | ✔️ | List of available models | [ `{"id": "openai/gpt-4","canonical_slug": "openai/gpt-4","name": "GPT-4","created": 1692901234,"description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.","pricing": {"prompt": "0.00003","completion": "0.00006","request": "0","image": "0"}`, “context\_length”: 8192, “architecture”: `{"tokenizer": "GPT","instruct_type": "chatml","modality": "text-\u003etext","input_modalities": ["text"],"output_modalities": ["text"]}`, “top\_provider”: `{"context_length": 8192,"max_completion_tokens": 4096,"is_moderated": true}`, “per\_request\_limits”: null, “supported\_parameters”: [ “temperature”, “top\_p”, “max\_tokens” ], “default\_parameters”: null, “knowledge\_cutoff”: null, “expiration\_date”: null, “links”: `{"details": "/api/v1/models/openai/gpt-5.4/endpoints"}` } ] |
