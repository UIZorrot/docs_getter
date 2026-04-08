---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/memberassignment"
title: "MemberAssignment Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.165842+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

MemberAssignment - TypeScript SDK

MemberAssignment type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { MemberAssignment } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: MemberAssignment = { |
| 4 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 5 | userId: "user_abc123", |
| 6 | organizationId: "org_xyz789", |
| 7 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 8 | assignedBy: "user_abc123", |
| 9 | createdAt: "2025-08-24T10:30:00Z", |
| 10 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the assignment | 550e8400-e29b-41d4-a716-446655440000 |
| `userId` | *string* | ✔️ | Clerk user ID of the assigned member | user\_abc123 |
| `organizationId` | *string* | ✔️ | Organization ID | org\_xyz789 |
| `guardrailId` | *string* | ✔️ | ID of the guardrail | 550e8400-e29b-41d4-a716-446655440001 |
| `assignedBy` | *string* | ✔️ | User ID of who made the assignment | user\_abc123 |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the assignment was created | 2025-08-24T10:30:00Z |
