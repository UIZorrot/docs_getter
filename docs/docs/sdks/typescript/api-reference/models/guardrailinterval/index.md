---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/guardrailinterval"
title: "GuardrailInterval Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.622377+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

GuardrailInterval - TypeScript SDK

GuardrailInterval type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Interval at which the limit resets (daily, weekly, monthly)

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GuardrailInterval } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: GuardrailInterval = "monthly"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "daily" | "weekly" | "monthly" | Unrecognized<string> |
```
