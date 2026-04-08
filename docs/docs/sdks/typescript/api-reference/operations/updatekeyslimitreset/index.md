---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/updatekeyslimitreset"
title: "UpdateKeysLimitReset Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.062862+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

UpdateKeysLimitReset - TypeScript SDK

UpdateKeysLimitReset type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

New limit reset type for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { UpdateKeysLimitReset } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: UpdateKeysLimitReset = "daily"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "daily" | "weekly" | "monthly" | Unrecognized<string> |
```
