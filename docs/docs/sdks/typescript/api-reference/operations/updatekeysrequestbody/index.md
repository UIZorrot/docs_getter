---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/updatekeysrequestbody"
title: "UpdateKeysRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.554530+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

UpdateKeysRequestBody - TypeScript SDK

UpdateKeysRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { UpdateKeysRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: UpdateKeysRequestBody = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ➖ | New name for the API key | Updated API Key Name |
| `disabled` | *boolean* | ➖ | Whether to disable the API key | false |
| `limit` | *number* | ➖ | New spending limit for the API key in USD | 75 |
| `limitReset` | [operations.UpdateKeysLimitReset](../updatekeyslimitreset/index.md) | ➖ | New limit reset type for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday. | daily |
| `includeByokInLimit` | *boolean* | ➖ | Whether to include BYOK usage in the limit | true |
