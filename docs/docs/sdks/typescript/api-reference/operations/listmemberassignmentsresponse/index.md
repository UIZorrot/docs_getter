---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listmemberassignmentsresponse"
title: "ListMemberAssignmentsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.990714+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

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
| 1 | import { ListMemberAssignmentsResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListMemberAssignmentsResponse = { |
| 4 | result: { |
| 5 | data: [ |
| 6 | { |
| 7 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 8 | userId: "user_abc123", |
| 9 | organizationId: "org_xyz789", |
| 10 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 11 | assignedBy: "user_abc123", |
| 12 | createdAt: "2025-08-24T10:30:00Z", |
| 13 | }, |
| 14 | ], |
| 15 | totalCount: 1, |
| 16 | }, |
| 17 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `result` | [models.ListMemberAssignmentsResponse](../../models/listmemberassignmentsresponse/index.md) | ✔️ | N/A | `{"data": [{"id": "550e8400-e29b-41d4-a716-446655440000","user_id": "user_abc123","organization_id": "org_xyz789","guardrail_id": "550e8400-e29b-41d4-a716-446655440001","assigned_by": "user_abc123","created_at": "2025-08-24T10:30:00Z"}` ], “total\_count”: `1<br />`} |
