---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createguardrailrequest"
title: "CreateGuardrailRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.170205+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateGuardrailRequest - TypeScript SDK

CreateGuardrailRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateGuardrailRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateGuardrailRequest = { |
| 4 | createGuardrailRequest: { |
| 5 | name: "My New Guardrail", |
| 6 | }, |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `createGuardrailRequest` | [models.CreateGuardrailRequest](../../models/createguardrailrequest/index.md) | ✔️ | N/A | `{"name": "My New Guardrail","description": "A guardrail for limiting API usage","limit_usd": 50,"reset_interval": "monthly","allowed_providers": ["openai","anthropic","deepseek"],"ignored_providers": null,"allowed_models": null,"enforce_zdr": false}` |
