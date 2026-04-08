---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createkeysrequestbody"
title: "CreateKeysRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:13.589669+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateKeysRequestBody - TypeScript SDK

CreateKeysRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateKeysRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateKeysRequestBody = { |
| 4 | name: "My New API Key", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ✔️ | Name for the new API key | My New API Key |
| `limit` | *number* | ➖ | Optional spending limit for the API key in USD | 50 |
| `limitReset` | [operations.CreateKeysLimitReset](../createkeyslimitreset/index.md) | ➖ | Type of limit reset for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday. | monthly |
| `includeByokInLimit` | *boolean* | ➖ | Whether to include BYOK usage in the limit | true |
| `expiresAt` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | ➖ | Optional ISO 8601 UTC timestamp when the API key should expire. Must be UTC, other timezones will be rejected | 2027-12-31T23:59:59Z |
| `creatorUserId` | *string* | ➖ | Optional user ID of the key creator. Only meaningful for organization-owned keys where a specific member is creating the key. | user\_2dHFtVWx2n56w6HkM0000000000 |
