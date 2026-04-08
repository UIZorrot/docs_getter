---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/operations/getcurrentkeyresponse"
title: "GetCurrentKeyResponse | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:59.876030+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetCurrentKeyResponse - Python SDK

GetCurrentKeyResponse method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

API key details

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.GetCurrentKeyData](../../../../operations/operations/getcurrentkeydata/index.md) | ✔️ | Current API key information | `{"label": "sk-or-v1-au7...890","limit": 100,"usage": 25.5,"usage_daily": 25.5,"usage_weekly": 25.5,"usage_monthly": 25.5,"byok_usage": 17.38,"byok_usage_daily": 17.38,"byok_usage_weekly": 17.38,"byok_usage_monthly": 17.38,"is_free_tier": false,"is_management_key": false,"is_provisioning_key": false,"limit_remaining": 74.5,"limit_reset": "monthly","include_byok_in_limit": false,"expires_at": "2027-12-31T23:59:59Z","creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000","rate_limit": {"requests": 1000,"interval": "1h","note": "This field is deprecated and safe to ignore."}` } |
