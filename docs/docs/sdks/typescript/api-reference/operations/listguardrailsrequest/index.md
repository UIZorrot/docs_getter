---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listguardrailsrequest"
title: "ListGuardrailsRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.113486+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListGuardrailsRequest - TypeScript SDK

ListGuardrailsRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListGuardrailsRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListGuardrailsRequest = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *number* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *number* | ➖ | Maximum number of records to return (max 100) | 50 |
