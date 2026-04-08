---
source_url: "https://openrouter.ai/docs/api/api-reference/o-auth/create-auth-keys-code"
title: "Create authorization code | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.624841+00:00"
---
[API Reference](../../responses/create-responses/index.md)[OAuth](../exchange-auth-code-for-api-key/index.md)

# Create authorization code

POST

https://openrouter.ai/api/v1/auth/keys/code

POST

/api/v1/auth/keys/code

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/auth/keys/code \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "callback_url": "https://myapp.com/auth/callback", |
| 6 | "code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM", |
| 7 | "code_challenge_method": "S256", |
| 8 | "limit": 100 |
| 9 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "auth_code_xyz789", |
| 4 | "app_id": 12345, |
| 5 | "created_at": "2025-08-24T10:30:00Z" |
| 6 | } |
| 7 | } |
```

Create an authorization code for the PKCE flow to generate a user-controlled API key

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

callback\_urlstringRequired`format: "uri"`

The callback URL to redirect to after authorization. Note, only https URLs on ports 443 and 3000 are allowed.

code\_challengestringOptional

PKCE code challenge for enhanced security

code\_challenge\_methodenumOptional

The method used to generate the code challenge

Allowed values:

limitdoubleOptional

Credit limit for the API key to be created

expires\_atdatetime or nullOptional

Optional expiration time for the API key to be created

key\_labelstringOptional`<=100 characters`

Optional custom label for the API key. Defaults to the app name if not provided.

usage\_limit\_typeenumOptional

Optional credit limit reset interval. When set, the credit limit resets on this interval.

Allowed values:

### Response

Successfully created authorization code

dataobject

Auth code data

### Errors

400

Bad Request Error

401

Unauthorized Error

409

Conflict Error

500

Internal Server Error
