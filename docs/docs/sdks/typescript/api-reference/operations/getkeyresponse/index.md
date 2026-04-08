---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getkeyresponse"
title: "GetKeyResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.992710+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetKeyResponse - TypeScript SDK

GetKeyResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

API key details

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetKeyResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetKeyResponse = { |
| 4 | data: { |
| 5 | hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 6 | name: "My Production Key", |
| 7 | label: "Production API Key", |
| 8 | disabled: false, |
| 9 | limit: 100, |
| 10 | limitRemaining: 74.5, |
| 11 | limitReset: "monthly", |
| 12 | includeByokInLimit: false, |
| 13 | usage: 25.5, |
| 14 | usageDaily: 25.5, |
| 15 | usageWeekly: 25.5, |
| 16 | usageMonthly: 25.5, |
| 17 | byokUsage: 17.38, |
| 18 | byokUsageDaily: 17.38, |
| 19 | byokUsageWeekly: 17.38, |
| 20 | byokUsageMonthly: 17.38, |
| 21 | createdAt: "2025-08-24T10:30:00Z", |
| 22 | updatedAt: "2025-08-24T15:45:00Z", |
| 23 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 24 | }, |
| 25 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.GetKeyData](../getkeydata/index.md) | ✔️ | The API key information | `{"hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943","name": "My Production Key","label": "sk-or-v1-0e6...1c96","disabled": false,"limit": 100,"limit_remaining": 74.5,"limit_reset": "monthly","include_byok_in_limit": false,"usage": 25.5,"usage_daily": 25.5,"usage_weekly": 25.5,"usage_monthly": 25.5,"byok_usage": 17.38,"byok_usage_daily": 17.38,"byok_usage_weekly": 17.38,"byok_usage_monthly": 17.38,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z","expires_at": "2027-12-31T23:59:59Z","creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000"}` |
