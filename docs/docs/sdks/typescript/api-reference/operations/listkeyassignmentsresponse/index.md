---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listkeyassignmentsresponse"
title: "ListKeyAssignmentsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.464419+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListKeyAssignmentsResponse - TypeScript SDK

ListKeyAssignmentsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListKeyAssignmentsResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListKeyAssignmentsResponse = { |
| 4 | result: { |
| 5 | data: [ |
| 6 | { |
| 7 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 8 | keyHash: |
| 9 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 10 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 11 | keyName: "Production Key", |
| 12 | keyLabel: "prod-key", |
| 13 | assignedBy: "user_abc123", |
| 14 | createdAt: "2025-08-24T10:30:00Z", |
| 15 | }, |
| 16 | ], |
| 17 | totalCount: 1, |
| 18 | }, |
| 19 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `result` | [models.ListKeyAssignmentsResponse](../../models/listkeyassignmentsresponse/index.md) | ✔️ | N/A | `{"data": [{"id": "550e8400-e29b-41d4-a716-446655440000","key_hash": "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93","guardrail_id": "550e8400-e29b-41d4-a716-446655440001","key_name": "Production Key","key_label": "prod-key","assigned_by": "user_abc123","created_at": "2025-08-24T10:30:00Z"}` ], “total\_count”: `1<br />`} |
