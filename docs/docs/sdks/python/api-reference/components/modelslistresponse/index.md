---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/components/modelslistresponse"
title: "ModelsListResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:00.049501+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Components

# 

ModelsListResponse - Python SDK

ModelsListResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

List of available models

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | List[[components.Model](../../../../components/components/model/index.md)] | ✔️ | List of available models | [ `{"id": "openai/gpt-4","canonical_slug": "openai/gpt-4","name": "GPT-4","created": 1692901234,"description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.","pricing": {"prompt": "0.00003","completion": "0.00006","request": "0","image": "0"}`, “context\_length”: 8192, “architecture”: `{"tokenizer": "GPT","instruct_type": "chatml","modality": "text-\u003etext","input_modalities": ["text"],"output_modalities": ["text"]}`, “top\_provider”: `{"context_length": 8192,"max_completion_tokens": 4096,"is_moderated": true}`, “per\_request\_limits”: null, “supported\_parameters”: [ “temperature”, “top\_p”, “max\_tokens” ], “default\_parameters”: null, “knowledge\_cutoff”: null, “expiration\_date”: null, “links”: `{"details": "/api/v1/models/openai/gpt-5.4/endpoints"}` } ] |
