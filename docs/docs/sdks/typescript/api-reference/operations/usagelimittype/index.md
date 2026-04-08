---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/usagelimittype"
title: "UsageLimitType Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.056306+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

UsageLimitType - TypeScript SDK

UsageLimitType type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Optional credit limit reset interval. When set, the credit limit resets on this interval.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { UsageLimitType } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: UsageLimitType = "monthly"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "daily" | "weekly" | "monthly" | Unrecognized<string> |
```
