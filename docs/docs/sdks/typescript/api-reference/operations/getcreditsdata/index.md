---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getcreditsdata"
title: "GetCreditsData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.792358+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetCreditsData - TypeScript SDK

GetCreditsData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetCreditsData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetCreditsData = { |
| 4 | totalCredits: 100.5, |
| 5 | totalUsage: 25.75, |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `totalCredits` | *number* | ✔️ | Total credits purchased | 100.5 |
| `totalUsage` | *number* | ✔️ | Total credits used | 25.75 |
