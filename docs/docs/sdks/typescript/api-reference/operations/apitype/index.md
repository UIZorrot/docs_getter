---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/apitype"
title: "ApiType Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.212530+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ApiType - TypeScript SDK

ApiType type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Type of API used for the generation

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ApiType } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ApiType = "rerank"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "completions" | "embeddings" | "rerank" | "video" | Unrecognized<string> |
```
