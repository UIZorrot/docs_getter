---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getcreditsresponse"
title: "GetCreditsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.728567+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetCreditsResponse - TypeScript SDK

GetCreditsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Total credits purchased and used

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetCreditsResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetCreditsResponse = { |
| 4 | data: { |
| 5 | totalCredits: 100.5, |
| 6 | totalUsage: 25.75, |
| 7 | }, |
| 8 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.GetCreditsData](../getcreditsdata/index.md) | ✔️ | N/A | `{"total_credits": 100.5,"total_usage": 25.75}` |
