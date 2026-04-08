---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/reasoningconfig"
title: "ReasoningConfig Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.199342+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ReasoningConfig - TypeScript SDK

ReasoningConfig type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Configuration for reasoning mode in the response

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ReasoningConfig } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ReasoningConfig = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `effort` | [models.ReasoningEffort](../reasoningeffort/index.md) | ➖ | N/A | medium |
| `summary` | [models.ReasoningSummaryVerbosity](../reasoningsummaryverbosity/index.md) | ➖ | N/A | auto |
| `maxTokens` | *number* | ➖ | N/A |  |
| `enabled` | *boolean* | ➖ | N/A |  |
