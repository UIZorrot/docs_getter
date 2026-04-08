---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/components/updateguardrailresponse"
title: "UpdateGuardrailResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:00.539611+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Components

# 

UpdateGuardrailResponse - Python SDK

UpdateGuardrailResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [components.Guardrail](../../../../components/components/guardrail/index.md) | ✔️ | N/A | `{"id": "550e8400-e29b-41d4-a716-446655440000","name": "Production Guardrail","description": "Guardrail for production environment","limit_usd": 100,"reset_interval": "monthly","allowed_providers": ["openai","anthropic","google"],"ignored_providers": null,"allowed_models": null,"enforce_zdr": false,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z"}` |
