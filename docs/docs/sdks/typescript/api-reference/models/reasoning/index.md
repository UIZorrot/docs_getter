---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/reasoning"
title: "Reasoning Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.258471+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Reasoning - TypeScript SDK

Reasoning type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Configuration options for reasoning models

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Reasoning } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Reasoning = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `effort` | [models.Effort](../effort/index.md) | ➖ | Constrains effort on reasoning for reasoning models | medium |
| `summary` | [models.ChatReasoningSummaryVerbosityEnum](../chatreasoningsummaryverbosityenum/index.md) | ➖ | N/A | concise |
