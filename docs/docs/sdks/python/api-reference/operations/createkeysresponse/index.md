---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/operations/createkeysresponse"
title: "CreateKeysResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:59.649914+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateKeysResponse - Python SDK

CreateKeysResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

API key created successfully

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.CreateKeysData](../../../../operations/operations/createkeysdata/index.md) | ✔️ | The created API key information | `{"hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943","name": "My Production Key","label": "sk-or-v1-0e6...1c96","disabled": false,"limit": 100,"limit_remaining": 74.5,"limit_reset": "monthly","include_byok_in_limit": false,"usage": 25.5,"usage_daily": 25.5,"usage_weekly": 25.5,"usage_monthly": 25.5,"byok_usage": 17.38,"byok_usage_daily": 17.38,"byok_usage_weekly": 17.38,"byok_usage_monthly": 17.38,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z","expires_at": "2027-12-31T23:59:59Z","creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000"}` |
| `key` | *str* | ✔️ | The actual API key string (only shown once) | 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 |
