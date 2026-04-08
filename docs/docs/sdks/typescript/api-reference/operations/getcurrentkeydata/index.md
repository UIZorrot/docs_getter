---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getcurrentkeydata"
title: "GetCurrentKeyData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.377228+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetCurrentKeyData - TypeScript SDK

GetCurrentKeyData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Current API key information

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetCurrentKeyData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetCurrentKeyData = { |
| 4 | label: "sk-or-v1-au7...890", |
| 5 | limit: 100, |
| 6 | usage: 25.5, |
| 7 | usageDaily: 25.5, |
| 8 | usageWeekly: 25.5, |
| 9 | usageMonthly: 25.5, |
| 10 | byokUsage: 17.38, |
| 11 | byokUsageDaily: 17.38, |
| 12 | byokUsageWeekly: 17.38, |
| 13 | byokUsageMonthly: 17.38, |
| 14 | isFreeTier: false, |
| 15 | isManagementKey: false, |
| 16 | isProvisioningKey: false, |
| 17 | limitRemaining: 74.5, |
| 18 | limitReset: "monthly", |
| 19 | includeByokInLimit: false, |
| 20 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 21 | rateLimit: { |
| 22 | requests: 1000, |
| 23 | interval: "1h", |
| 24 | note: "This field is deprecated and safe to ignore.", |
| 25 | }, |
| 26 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `label` | *string* | ✔️ | Human-readable label for the API key | sk-or-v1-0e6…1c96 |
| `limit` | *number* | ✔️ | Spending limit for the API key in USD | 100 |
| `usage` | *number* | ✔️ | Total OpenRouter credit usage (in USD) for the API key | 25.5 |
| `usageDaily` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC day | 25.5 |
| `usageWeekly` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC week (Monday-Sunday) | 25.5 |
| `usageMonthly` | *number* | ✔️ | OpenRouter credit usage (in USD) for the current UTC month | 25.5 |
| `byokUsage` | *number* | ✔️ | Total external BYOK usage (in USD) for the API key | 17.38 |
| `byokUsageDaily` | *number* | ✔️ | External BYOK usage (in USD) for the current UTC day | 17.38 |
| `byokUsageWeekly` | *number* | ✔️ | External BYOK usage (in USD) for the current UTC week (Monday-Sunday) | 17.38 |
| `byokUsageMonthly` | *number* | ✔️ | External BYOK usage (in USD) for current UTC month | 17.38 |
| `isFreeTier` | *boolean* | ✔️ | Whether this is a free tier API key | false |
| `isManagementKey` | *boolean* | ✔️ | Whether this is a management key | false |
| ~~`isProvisioningKey`~~ | *boolean* | ✔️ | : warning: \*\* DEPRECATED \*\*: This will be removed in a future release, please migrate away from it as soon as possible.  Whether this is a management key | false |
| `limitRemaining` | *number* | ✔️ | Remaining spending limit in USD | 74.5 |
| `limitReset` | *string* | ✔️ | Type of limit reset for the API key | monthly |
| `includeByokInLimit` | *boolean* | ✔️ | Whether to include external BYOK usage in the credit limit | false |
| `expiresAt` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | ➖ | ISO 8601 UTC timestamp when the API key expires, or null if no expiration | 2027-12-31T23:59:59Z |
| `creatorUserId` | *string* | ✔️ | The user ID of the key creator. For organization-owned keys, this is the member who created the key. For individual users, this is the user’s own ID. | user\_2dHFtVWx2n56w6HkM0000000000 |
| ~~`rateLimit`~~ | [operations.RateLimit](../ratelimit/index.md) | ✔️ | : warning: \*\* DEPRECATED \*\*: This will be removed in a future release, please migrate away from it as soon as possible.  Legacy rate limit information about a key. Will always return -1. | `{"requests": 1000,"interval": "1h","note": "This field is deprecated and safe to ignore."}` |
