---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listresponse"
title: "ListResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.711495+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListResponse - TypeScript SDK

ListResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

List of API keys

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | hash: "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 7 | name: "My Production Key", |
| 8 | label: "Production API Key", |
| 9 | disabled: false, |
| 10 | limit: 100, |
| 11 | limitRemaining: 74.5, |
| 12 | limitReset: "monthly", |
| 13 | includeByokInLimit: false, |
| 14 | usage: 25.5, |
| 15 | usageDaily: 25.5, |
| 16 | usageWeekly: 25.5, |
| 17 | usageMonthly: 25.5, |
| 18 | byokUsage: 17.38, |
| 19 | byokUsageDaily: 17.38, |
| 20 | byokUsageWeekly: 17.38, |
| 21 | byokUsageMonthly: 17.38, |
| 22 | createdAt: "2025-08-24T10:30:00Z", |
| 23 | updatedAt: "2025-08-24T15:45:00Z", |
| 24 | creatorUserId: "user_2dHFtVWx2n56w6HkM0000000000", |
| 25 | }, |
| 26 | ], |
| 27 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | [operations.ListData](../listdata/index.md)[] | ✔️ | List of API keys |
