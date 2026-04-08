---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/oauth"
title: "OAuth | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:44.905814+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

OAuth - Python SDK

OAuth method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

OAuth authentication endpoints

### Available Operations

- [exchange\_auth\_code\_for\_api\_key](#exchange_auth_code_for_api_key) - Exchange authorization code for API key
- [create\_auth\_code](#create_auth_code) - Create authorization code

## exchange\_auth\_code\_for\_api\_key

Exchange an authorization code from the PKCE flow for a user-controlled API key

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | http_referer="<value>", |
| 6 | x_open_router_title="<value>", |
| 7 | x_open_router_categories="<value>", |
| 8 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 9 | ) as open_router: |
| 10 |  |
| 11 | res = open_router.o_auth.exchange_auth_code_for_api_key(code="auth_code_abc123def456", code_verifier="dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk", code_challenge_method="S256") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `code` | *str* | ✔️ | The authorization code received from the OAuth redirect | auth\_code\_abc123def456 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `code_verifier` | *Optional[str]* | ➖ | The code verifier if code\_challenge was used in the authorization request | dBjftJeZ4CVP-mB92K27uhbUJU1p1r\_wW1gFWFOEjXk |
| `code_challenge_method` | [OptionalNullable[operations.ExchangeAuthCodeForAPIKeyCodeChallengeMethod]](../../../operations/exchangeauthcodeforapikeycodechallengemethod.md/index.md) | ➖ | The method used to generate the code challenge | S256 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ExchangeAuthCodeForAPIKeyResponse](../operations/exchangeauthcodeforapikeyresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## create\_auth\_code

Create an authorization code for the PKCE flow to generate a user-controlled API key

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | http_referer="<value>", |
| 6 | x_open_router_title="<value>", |
| 7 | x_open_router_categories="<value>", |
| 8 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 9 | ) as open_router: |
| 10 |  |
| 11 | res = open_router.o_auth.create_auth_code(callback_url="https://myapp.com/auth/callback", code_challenge="E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM", code_challenge_method="S256", limit=100) |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `callback_url` | *str* | ✔️ | The callback URL to redirect to after authorization. Note, only https URLs on ports 443 and 3000 are allowed. | [https://myapp.com/auth/callback](https://myapp.com/auth/callback) |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `code_challenge` | *Optional[str]* | ➖ | PKCE code challenge for enhanced security | E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM |
| `code_challenge_method` | [Optional[operations.CreateAuthKeysCodeCodeChallengeMethod]](../../../operations/createauthkeyscodecodechallengemethod.md/index.md) | ➖ | The method used to generate the code challenge | S256 |
| `limit` | *Optional[float]* | ➖ | Credit limit for the API key to be created | 100 |
| `expires_at` | [date](https://docs.python.org/3/library/datetime.html) | ➖ | Optional expiration time for the API key to be created | 2027-12-31T23:59:59Z |
| `key_label` | *Optional[str]* | ➖ | Optional custom label for the API key. Defaults to the app name if not provided. | My Custom Key |
| `usage_limit_type` | [Optional[operations.UsageLimitType]](../../../operations/usagelimittype.md/index.md) | ➖ | Optional credit limit reset interval. When set, the credit limit resets on this interval. | monthly |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.CreateAuthKeysCodeResponse](../operations/createauthkeyscoderesponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ConflictResponseError | 409 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
