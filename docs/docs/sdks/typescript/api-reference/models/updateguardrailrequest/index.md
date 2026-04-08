---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/updateguardrailrequest"
title: "UpdateGuardrailRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.400973+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

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
| 1 | import { UpdateGuardrailRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: UpdateGuardrailRequest = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ➖ | New name for the guardrail | Updated Guardrail Name |
| `description` | *string* | ➖ | New description for the guardrail | Updated description |
| `limitUsd` | *number* | ➖ | New spending limit in USD | 75 |
| `resetInterval` | [models.GuardrailInterval](../guardrailinterval/index.md) | ➖ | Interval at which the limit resets (daily, weekly, monthly) | monthly |
| `allowedProviders` | *string*[] | ➖ | New list of allowed provider IDs | [ “openai”, “anthropic”, “deepseek” ] |
| `ignoredProviders` | *string*[] | ➖ | List of provider IDs to exclude from routing | [ “azure” ] |
| `allowedModels` | *string*[] | ➖ | Array of model identifiers (slug or canonical\_slug accepted) | [ “openai/gpt-5.2” ] |
| `enforceZdr` | *boolean* | ➖ | Whether to enforce zero data retention | true |
