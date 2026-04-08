---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createkeysrequest"
title: "CreateKeysRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.539655+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateKeysRequest - TypeScript SDK

CreateKeysRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateKeysRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateKeysRequest = { |
| 4 | requestBody: { |
| 5 | name: "My New API Key", |
| 6 | }, |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `requestBody` | [operations.CreateKeysRequestBody](../createkeysrequestbody/index.md) | ✔️ | N/A | `{"name": "My New API Key","limit": 50,"limit_reset": "monthly","include_byok_in_limit": true,"expires_at": "2027-12-31T23:59:59Z"}` |
