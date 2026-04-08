---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/role"
title: "Role Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:20.715828+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

Role - TypeScript SDK

Role type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Role of the member in the organization

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Role } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: Role = "org:member"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "org:admin" | "org:member" | Unrecognized<string> |
```
