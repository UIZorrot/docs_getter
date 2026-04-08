---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getuseractivityrequest"
title: "GetUserActivityRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.263097+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetUserActivityRequest - TypeScript SDK

GetUserActivityRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetUserActivityRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetUserActivityRequest = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `date` | *string* | ➖ | Filter by a single UTC date in the last 30 days (YYYY-MM-DD format). | 2025-08-24 |
| `apiKeyHash` | *string* | ➖ | Filter by API key hash (SHA-256 hex string, as returned by the keys API). | abc123def456… |
| `userId` | *string* | ➖ | Filter by org member user ID. Only applicable for organization accounts. | user\_abc123 |
