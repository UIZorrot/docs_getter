---
source_url: "https://openrouter.ai/docs/api/api-reference/organization/list-organization-members"
title: "List organization members | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.787291+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Organization](index.md)

# List organization members

GET

https://openrouter.ai/api/v1/organization/members

GET

/api/v1/organization/members

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/organization/members \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "user_2dHFtVWx2n56w6HkM0000000000", |
| 5 | "first_name": "Jane", |
| 6 | "last_name": "Doe", |
| 7 | "email": "jane.doe@example.com", |
| 8 | "role": "org:admin" |
| 9 | } |
| 10 | ], |
| 11 | "total_count": 25 |
| 12 | } |
```

List all members of the organization associated with the authenticated management key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

offsetintegerOptional`>=0`

Number of records to skip for pagination

limitintegerOptional`1-100`

Maximum number of records to return (max 100)

### Response

List of organization members

datalist of objects

List of organization members

total\_countinteger

Total number of members in the organization

### Errors

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
