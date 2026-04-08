---
source_url: "https://openrouter.ai/docs/api/api-reference/o-auth/exchange-auth-code-for-api-key"
title: "Exchange authorization code for API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:28.009047+00:00"
---
[API Reference](../../responses/create-responses/index.md)[OAuth](index.md)

# Exchange authorization code for API key

POST

https://openrouter.ai/api/v1/auth/keys

POST

/api/v1/auth/keys

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/auth/keys \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "code": "auth_code_abc123def456", |
| 6 | "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk", |
| 7 | "code_challenge_method": "S256" |
| 8 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "key": "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", |
| 3 | "user_id": "user_2yOPcMpKoQhcd4bVgSMlELRaIah" |
| 4 | } |
```

Exchange an authorization code from the PKCE flow for a user-controlled API key

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

codestringRequired

The authorization code received from the OAuth redirect

code\_verifierstringOptional

The code verifier if code\_challenge was used in the authorization request

code\_challenge\_methodenum or nullOptional

The method used to generate the code challenge

Allowed values:

### Response

Successfully exchanged code for an API key

keystring

The API key to use for OpenRouter requests

user\_idstring or null

User ID associated with the API key

### Errors

400

Bad Request Error

403

Forbidden Error

500

Internal Server Error
