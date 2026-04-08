---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/updateguardrailrequest"
title: "UpdateGuardrailRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.772214+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

UpdateGuardrailRequest - TypeScript SDK

UpdateGuardrailRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { UpdateGuardrailRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: UpdateGuardrailRequest = { |
| 4 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 5 | updateGuardrailRequest: {}, |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `id` | *string* | ✔️ | The unique identifier of the guardrail to update | 550e8400-e29b-41d4-a716-446655440000 |
| `updateGuardrailRequest` | [models.UpdateGuardrailRequest](../../models/updateguardrailrequest/index.md) | ✔️ | N/A | `{"name": "Updated Guardrail Name","description": "Updated description","limit_usd": 75,"reset_interval": "weekly"}` |
