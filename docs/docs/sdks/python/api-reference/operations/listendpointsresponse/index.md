---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/operations/listendpointsresponse"
title: "ListEndpointsResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:01.153192+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListEndpointsResponse - Python SDK

ListEndpointsResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

Returns a list of endpoints

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [components.ListEndpointsResponse](../../../../operations/components/listendpointsresponse/index.md) | ✔️ | List of available endpoints for a model | `{"id": "openai/gpt-4","name": "GPT-4","created": 1692901234,"description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy.","architecture": {"tokenizer": "GPT","instruct_type": "chatml","modality": "text-\u003etext","input_modalities": ["text"],"output_modalities": ["text"]}`, “endpoints”: [ `{"name": "OpenAI: GPT-4","model_name": "GPT-4","context_length": 8192,"pricing": {"prompt": "0.00003","completion": "0.00006","request": "0","image": "0"}`, “provider\_name”: “OpenAI”, “tag”: “openai”, “quantization”: “fp16”, “max\_completion\_tokens”: 4096, “max\_prompt\_tokens”: 8192, “supported\_parameters”: [ “temperature”, “top\_p”, “max\_tokens”, “frequency\_penalty”, “presence\_penalty” ], “status”: “default”, “uptime\_last\_30m”: 99.5, “uptime\_last\_5m”: 100, “uptime\_last\_1d”: 99.8, “supports\_implicit\_caching”: true, “latency\_last\_30m”: `{"p50": 0.25,"p75": 0.35,"p90": 0.48,"p99": 0.85}`, “throughput\_last\_30m”: `{"p50": 45.2,"p75": 38.5,"p90": 28.3,"p99": 15.1}` } ] } |
