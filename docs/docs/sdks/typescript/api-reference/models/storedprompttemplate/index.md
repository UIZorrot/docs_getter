---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/storedprompttemplate"
title: "StoredPromptTemplate Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.332519+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

StoredPromptTemplate - TypeScript SDK

StoredPromptTemplate type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { StoredPromptTemplate } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: StoredPromptTemplate = { |
| 4 | id: "prompt-abc123", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | *string* | ✔️ | N/A |
| `variables` | `Record<string, *models.Variables*>` | ➖ | N/A |
