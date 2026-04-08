---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/delete-keys"
title: "Delete an API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:25.291377+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](../list/index.md)

# Delete an API key

DELETE

https://openrouter.ai/api/v1/keys/:hash

DELETE

/api/v1/keys/:hash

```
|  |  |
| --- | --- |
| 1 | curl -X DELETE https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "deleted": true |
| 3 | } |
```

Delete an existing API key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

hashstringRequired

The hash identifier of the API key to delete

### Response

API key deleted successfully

deletedtrue

Confirmation that the API key was deleted

### Errors

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error
