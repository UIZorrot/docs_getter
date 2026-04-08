---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getcurrentkeyresponse"
title: "GetCurrentKeyResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.107932+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetCurrentKeyResponse - TypeScript SDK

GetCurrentKeyResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

API key details

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetCurrentKeyResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetCurrentKeyResponse = { |
| 4 | data: { |
| 5 | label: "sk-or-v1-au7...890", |
| 6 | limit: 100, |
| 7 | usage: 25.5, |
| 8 | usageDaily: 25.5, |
| 9 | usageWeekly: 25.5, |
| 10 | usageMonthly: 25.5, |
| 11 | byokUsage: 17.38, |
| 12 | byokUsageDaily: 17.38, |
| 13 | byokUsageWeekly: 17.38, |
| 14 | byokUsageMonthly: 17.38, |
| 15 | isFreeTier: false, |
| 16 | isManagementKey: false, |
| 17 | isProvisioningKey: false, |
| 18 | limitRemaining: 74.5, |
| 19 | limitReset: "monthly", |
| 20 | includeByokInLimit: false, |
| 21 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 22 | rateLimit: { |
| 23 | requests: 1000, |
| 24 | interval: "1h", |
| 25 | note: "This field is deprecated and safe to ignore.", |
| 26 | }, |
| 27 | }, |
| 28 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.GetCurrentKeyData](../getcurrentkeydata/index.md) | ✔️ | Current API key information | `{"label": "sk-or-v1-au7...890","limit": 100,"usage": 25.5,"usage_daily": 25.5,"usage_weekly": 25.5,"usage_monthly": 25.5,"byok_usage": 17.38,"byok_usage_daily": 17.38,"byok_usage_weekly": 17.38,"byok_usage_monthly": 17.38,"is_free_tier": false,"is_management_key": false,"is_provisioning_key": false,"limit_remaining": 74.5,"limit_reset": "monthly","include_byok_in_limit": false,"expires_at": "2027-12-31T23:59:59Z","creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000","rate_limit": {"requests": 1000,"interval": "1h","note": "This field is deprecated and safe to ignore."}` } |
