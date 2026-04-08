---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createkeysdata"
title: "CreateKeysData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:13.844836+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateKeysData - TypeScript SDK

CreateKeysData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

The created API key information

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateKeysData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateKeysData = { |
| 4 | hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 5 | name: "My Production Key", |
| 6 | label: "sk-or-v1-0e6...1c96", |
| 7 | disabled: false, |
| 8 | limit: 100, |
| 9 | limitRemaining: 74.5, |
| 10 | limitReset: "monthly", |
| 11 | includeByokInLimit: false, |
| 12 | usage: 25.5, |
| 13 | usageDaily: 25.5, |
| 14 | usageWeekly: 25.5, |
| 15 | usageMonthly: 25.5, |
| 16 | byokUsage: 17.38, |
| 17 | byokUsageDaily: 17.38, |
| 18 | byokUsageWeekly: 17.38, |
| 19 | byokUsageMonthly: 17.38, |
| 20 | createdAt: "2025-08-24T10:30:00Z", |
| 21 | updatedAt: "2025-08-24T15:45:00Z", |
| 22 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 23 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `hash` | *string* | ✔️ | Unique hash identifier for the API key | f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 |
| `name` | *string* | ✔️ | Name of the API key | My Production Key |
| `label` | *string* | ✔️ | Human-readable label for the API key | sk-or-v1-0e6…1c96 |
| `disabled` | *boolean* | ✔️ | Whether the API key is disabled | false |
| `limit` | *number* | ✔️ | Spending limit for the API key in USD | 100 |
| `limitRemaining` | *number* | ✔️ | Remaining spending limit in USD | 74.5 |
| `limitReset` | *string* | ✔️ | Type of limit reset for the API key | monthly |
| `includeByokInLimit` | *boolean* | ✔️ | Whether to include external BYOK usage in the credit limit | false |
| `usage` | *number* | ✔️ | Total OpenRouter credit usage (in USD) for the API key | 25.5 |
| `usageDaily` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC day | 25.5 |
| `usageWeekly` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC week (Monday-Sunday) | 25.5 |
| `usageMonthly` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC month | 25.5 |
| `byokUsage` | *number* | ✔️ | Total external BYOK usage (in USD) for the API key | 17.38 |
| `byokUsageDaily` | *number* | ✔️ | External BYOK usage (in USD) for the current UTC day | 17.38 |
| `byokUsageWeekly` | *number* | ✔️ | External BYOK usage (in USD) for the current UTC week (Monday-Sunday) | 17.38 |
| `byokUsageMonthly` | *number* | ✔️ | External BYOK usage (in USD) for current UTC month | 17.38 |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the API key was created | 2025-08-24T10:30:00Z |
| `updatedAt` | *string* | ✔️ | ISO 8601 timestamp of when the API key was last updated | 2025-08-24T15:45:00Z |
| `expiresAt` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | ➖ | ISO 8601 UTC timestamp when the API key expires, or null if no expiration | 2027-12-31T23:59:59Z |
| `creatorUserId` | *string* | ✔️ | The user ID of the key creator. For organization-owned keys, this is the member who created the key. For individual users, this is the user’s own ID. | user\_2dHFtVWx2n56w6HkM0000000000 |
