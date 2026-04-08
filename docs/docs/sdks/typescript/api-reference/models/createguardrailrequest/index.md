---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/createguardrailrequest"
title: "CreateGuardrailRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.095852+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

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
| 1 | import { CreateGuardrailRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: CreateGuardrailRequest = { |
| 4 | name: "My New Guardrail", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ✔️ | Name for the new guardrail | My New Guardrail |
| `description` | *string* | ➖ | Description of the guardrail | A guardrail for limiting API usage |
| `limitUsd` | *number* | ➖ | Spending limit in USD | 50 |
| `resetInterval` | [models.GuardrailInterval](../guardrailinterval/index.md) | ➖ | Interval at which the limit resets (daily, weekly, monthly) | monthly |
| `allowedProviders` | *string*[] | ➖ | List of allowed provider IDs | [ “openai”, “anthropic”, “deepseek” ] |
| `ignoredProviders` | *string*[] | ➖ | List of provider IDs to exclude from routing | [ “azure” ] |
| `allowedModels` | *string*[] | ➖ | Array of model identifiers (slug or canonical\_slug accepted) | [ “openai/gpt-5.2”, “anthropic/claude-4.5-opus-20251124”, “deepseek/deepseek-r1-0528:free” ] |
| `enforceZdr` | *boolean* | ➖ | Whether to enforce zero data retention | false |
