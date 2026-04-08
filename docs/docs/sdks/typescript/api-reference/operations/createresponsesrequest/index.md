---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createresponsesrequest"
title: "CreateResponsesRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.823775+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateResponsesRequest - TypeScript SDK

CreateResponsesRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateResponsesRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateResponsesRequest = { |
| 4 | responsesRequest: {}, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `responsesRequest` | [models.ResponsesRequest](../../models/responsesrequest/index.md) | ✔️ | N/A | `{"model": "anthropic/claude-4.5-sonnet-20250929","input": [{"type": "message","content": "Hello, how are you?","role": "user"}` ], “temperature”: 0.7, “top\_p”: 0.9, “tools”: [ `{"type": "function","name": "get_current_weather","description": "Get the current weather in a given location","parameters": {"type": "object","properties": {"location": {"type": "string"}` } } } ] } |
