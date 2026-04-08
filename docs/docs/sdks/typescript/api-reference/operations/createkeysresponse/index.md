---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createkeysresponse"
title: "CreateKeysResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.597792+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateKeysResponse - TypeScript SDK

CreateKeysResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

API key created successfully

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateKeysResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateKeysResponse = { |
| 4 | data: { |
| 5 | hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 6 | name: "My New API Key", |
| 7 | label: "My New API Key", |
| 8 | disabled: false, |
| 9 | limit: 50, |
| 10 | limitRemaining: 50, |
| 11 | limitReset: "monthly", |
| 12 | includeByokInLimit: true, |
| 13 | usage: 0, |
| 14 | usageDaily: 0, |
| 15 | usageWeekly: 0, |
| 16 | usageMonthly: 0, |
| 17 | byokUsage: 0, |
| 18 | byokUsageDaily: 0, |
| 19 | byokUsageWeekly: 0, |
| 20 | byokUsageMonthly: 0, |
| 21 | createdAt: "2025-08-24T10:30:00Z", |
| 22 | updatedAt: null, |
| 23 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 24 | }, |
| 25 | key: |
| 26 | "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", |
| 27 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.CreateKeysData](../createkeysdata/index.md) | ✔️ | The created API key information | `{"hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943","name": "My Production Key","label": "sk-or-v1-0e6...1c96","disabled": false,"limit": 100,"limit_remaining": 74.5,"limit_reset": "monthly","include_byok_in_limit": false,"usage": 25.5,"usage_daily": 25.5,"usage_weekly": 25.5,"usage_monthly": 25.5,"byok_usage": 17.38,"byok_usage_daily": 17.38,"byok_usage_weekly": 17.38,"byok_usage_monthly": 17.38,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z","expires_at": "2027-12-31T23:59:59Z","creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000"}` |
| `key` | *string* | ✔️ | The actual API key string (only shown once) | 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 |
