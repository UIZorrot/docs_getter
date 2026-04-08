---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getkeyrequest"
title: "GetKeyRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.943667+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetKeyRequest - TypeScript SDK

GetKeyRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetKeyRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetKeyRequest = { |
| 4 | hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `hash` | *string* | ✔️ | The hash identifier of the API key to retrieve | f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 |
