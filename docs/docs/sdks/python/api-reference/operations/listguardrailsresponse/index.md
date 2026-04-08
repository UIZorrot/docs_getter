---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/operations/listguardrailsresponse"
title: "ListGuardrailsResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:00.197882+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListGuardrailsResponse - Python SDK

ListGuardrailsResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `result` | [components.ListGuardrailsResponse](../../../../operations/components/listguardrailsresponse/index.md) | ✔️ | N/A | `{"data": [{"id": "550e8400-e29b-41d4-a716-446655440000","name": "Production Guardrail","description": "Guardrail for production environment","limit_usd": 100,"reset_interval": "monthly","allowed_providers": ["openai","anthropic","google"],"ignored_providers": null,"allowed_models": null,"enforce_zdr": false,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z"}` ], “total\_count”: `1<br />`} |
