---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listorganizationmembersresponsebody"
title: "ListOrganizationMembersResponseBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.321249+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListOrganizationMembersResponseBody - TypeScript SDK

ListOrganizationMembersResponseBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

List of organization members

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListOrganizationMembersResponseBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListOrganizationMembersResponseBody = { |
| 4 | data: [], |
| 5 | totalCount: 25, |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.ListOrganizationMembersData](../listorganizationmembersdata/index.md)[] | ✔️ | List of organization members |  |
| `totalCount` | *number* | ✔️ | Total number of members in the organization | 25 |
