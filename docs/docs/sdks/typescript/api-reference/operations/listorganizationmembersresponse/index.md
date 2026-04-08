---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listorganizationmembersresponse"
title: "ListOrganizationMembersResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.231251+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListOrganizationMembersResponse - TypeScript SDK

ListOrganizationMembersResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListOrganizationMembersResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListOrganizationMembersResponse = { |
| 4 | result: { |
| 5 | data: [], |
| 6 | totalCount: 25, |
| 7 | }, |
| 8 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `result` | [operations.ListOrganizationMembersResponseBody](../listorganizationmembersresponsebody/index.md) | ✔️ | N/A |
