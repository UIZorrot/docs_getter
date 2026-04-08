---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/guardrail"
title: "Guardrail Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.150815+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Guardrail - TypeScript SDK

Guardrail type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Guardrail } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Guardrail = { |
| 4 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 5 | name: "Production Guardrail", |
| 6 | createdAt: "2025-08-24T10:30:00Z", |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `name` | *string* | ✔️ | Name of the guardrail | Production Guardrail |
| `description` | *string* | ➖ | Description of the guardrail | Guardrail for production environment |
| `limitUsd` | *number* | ➖ | Spending limit in USD | 100 |
| `resetInterval` | [models.GuardrailInterval](../guardrailinterval/index.md) | ➖ | Interval at which the limit resets (daily, weekly, monthly) | monthly |
| `allowedProviders` | *string*[] | ➖ | List of allowed provider IDs | [ “openai”, “anthropic”, “google” ] |
| `ignoredProviders` | *string*[] | ➖ | List of provider IDs to exclude from routing | [ “azure” ] |
| `allowedModels` | *string*[] | ➖ | Array of model canonical\_slugs (immutable identifiers) | [ “openai/gpt-5.2-20251211”, “anthropic/claude-4.5-opus-20251124”, “deepseek/deepseek-r1-0528:free” ] |
| `enforceZdr` | *boolean* | ➖ | Whether to enforce zero data retention | false |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the guardrail was created | 2025-08-24T10:30:00Z |
| `updatedAt` | *string* | ➖ | ISO 8601 timestamp of when the guardrail was last updated | 2025-08-24T15:45:00Z |
