---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/category"
title: "Category Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.633907+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

Category - TypeScript SDK

Category type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Filter models by use case category

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Category } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: Category = "programming"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "programming" | "roleplay" | "marketing" | "marketing/seo" | "technology" | "science" | "translation" | "legal" | "finance" | "health" | "trivia" | "academia" | Unrecognized<string> |
```
