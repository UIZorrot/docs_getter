---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/listmemberassignmentsresponse"
title: "ListMemberAssignmentsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.446059+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ListMemberAssignmentsResponse - TypeScript SDK

ListMemberAssignmentsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListMemberAssignmentsResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ListMemberAssignmentsResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 7 | userId: "user_abc123", |
| 8 | organizationId: "org_xyz789", |
| 9 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 10 | assignedBy: "user_abc123", |
| 11 | createdAt: "2025-08-24T10:30:00Z", |
| 12 | }, |
| 13 | ], |
| 14 | totalCount: 1, |
| 15 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.MemberAssignment](../memberassignment/index.md)[] | ✔️ | List of member assignments |  |
| `totalCount` | *number* | ✔️ | Total number of member assignments | 10 |
