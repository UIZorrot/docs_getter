---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/model"
title: "Model Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.061503+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Model - TypeScript SDK

Model type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Information about an AI model available on OpenRouter

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Model } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Model = { |
| 4 | id: "openai/gpt-4", |
| 5 | canonicalSlug: "openai/gpt-4", |
| 6 | name: "GPT-4", |
| 7 | created: 1692901234, |
| 8 | pricing: { |
| 9 | prompt: "0.00003", |
| 10 | completion: "0.00006", |
| 11 | }, |
| 12 | contextLength: 8192, |
| 13 | architecture: { |
| 14 | modality: "text->text", |
| 15 | inputModalities: [ |
| 16 | "text", |
| 17 | ], |
| 18 | outputModalities: [ |
| 19 | "text", |
| 20 | ], |
| 21 | }, |
| 22 | topProvider: { |
| 23 | isModerated: true, |
| 24 | }, |
| 25 | perRequestLimits: null, |
| 26 | supportedParameters: [ |
| 27 | "temperature", |
| 28 | "top_p", |
| 29 | "max_tokens", |
| 30 | ], |
| 31 | defaultParameters: null, |
| 32 | links: { |
| 33 | details: "/api/v1/models/openai/gpt-5.4/endpoints", |
| 34 | }, |
| 35 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the model | openai/gpt-4 |
| `canonicalSlug` | *string* | ✔️ | Canonical slug for the model | openai/gpt-4 |
| `huggingFaceId` | *string* | ➖ | Hugging Face model identifier, if applicable | microsoft/DialoGPT-medium |
| `name` | *string* | ✔️ | Display name of the model | GPT-4 |
| `created` | *number* | ✔️ | Unix timestamp of when the model was created | 1692901234 |
| `description` | *string* | ➖ | Description of the model | GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy. |
| `pricing` | [models.PublicPricing](../publicpricing/index.md) | ✔️ | Pricing information for the model | `{"prompt": "0.00003","completion": "0.00006","request": "0","image": "0"}` |
| `contextLength` | *number* | ✔️ | Maximum context length in tokens | 8192 |
| `architecture` | [models.ModelArchitecture](../modelarchitecture/index.md) | ✔️ | Model architecture information | `{"tokenizer": "GPT","instruct_type": "chatml","modality": "text-\u003etext","input_modalities": ["text"],"output_modalities": ["text"]}` |
| `topProvider` | [models.TopProviderInfo](../topproviderinfo/index.md) | ✔️ | Information about the top provider for this model | `{"context_length": 8192,"max_completion_tokens": 4096,"is_moderated": true}` |
| `perRequestLimits` | [models.PerRequestLimits](../perrequestlimits/index.md) | ✔️ | Per-request token limits | `{"prompt_tokens": 1000,"completion_tokens": 1000}` |
| `supportedParameters` | [models.Parameter](../parameter/index.md)[] | ✔️ | List of supported parameters for this model |  |
| `defaultParameters` | [models.DefaultParameters](../defaultparameters/index.md) | ✔️ | Default parameters for this model | `{"temperature": 0.7,"top_p": 0.9,"top_k": 0,"frequency_penalty": 0,"presence_penalty": 0,"repetition_penalty": 1}` |
| `knowledgeCutoff` | *string* | ➖ | The date up to which the model was trained on data. ISO 8601 date string (YYYY-MM-DD) or null if unknown. | 2024-10-01 |
| `expirationDate` | *string* | ➖ | The date after which the model may be removed. ISO 8601 date string (YYYY-MM-DD) or null if no expiration. | 2025-06-01 |
| `links` | [models.ModelLinks](../modellinks/index.md) | ✔️ | Related API endpoints and resources for this model. | `{"details": "/api/v1/models/openai/gpt-5.4/endpoints"}` |
