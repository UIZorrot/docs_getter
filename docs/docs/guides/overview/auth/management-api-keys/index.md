---
source_url: "https://openrouter.ai/docs/guides/overview/auth/management-api-keys"
title: "Management API Keys | Programmatic Control of OpenRouter API Keys | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:40.051097+00:00"
---
[Overview](../../../../quickstart/index.md)[Authentication](../oauth/index.md)

# Management API Keys

Manage API keys programmatically

OpenRouter provides endpoints to programmatically manage your API keys, enabling key creation and management for applications that need to distribute or rotate keys automatically.

## Creating a Management API Key

To use the key management API, you first need to create a Management API key:

1. Go to the [Management API Keys page](https://openrouter.ai/settings/management-keys)
2. Click “Create New Key”
3. Complete the key creation process

Management keys cannot be used to make API calls to OpenRouter’s completion endpoints - they are exclusively for administrative operations.

## Use Cases

Common scenarios for programmatic key management include:

- **SaaS Applications**: Automatically create unique API keys for each customer instance
- **Key Rotation**: Regularly rotate API keys for security compliance
- **Usage Monitoring**: Track key usage and automatically disable keys that exceed limits (with optional daily/weekly/monthly limit resets)

## Example Usage

All key management endpoints are under `/api/v1/keys` and require a Management API key in the Authorization header.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: 'your-management-key', // Use your Management API key |
| 5 | }); |
| 6 |  |
| 7 | // List the most recent 100 API keys |
| 8 | const keys = await openRouter.apiKeys.list(); |
| 9 |  |
| 10 | // You can paginate using the offset parameter |
| 11 | const keysPage2 = await openRouter.apiKeys.list({ offset: 100 }); |
| 12 |  |
| 13 | // Create a new API key |
| 14 | const newKey = await openRouter.apiKeys.create({ |
| 15 | name: 'Customer Instance Key', |
| 16 | limit: 1000, // Optional credit limit |
| 17 | }); |
| 18 |  |
| 19 | // Get a specific key |
| 20 | const keyHash = '<YOUR_KEY_HASH>'; |
| 21 | const key = await openRouter.apiKeys.get(keyHash); |
| 22 |  |
| 23 | // Update a key |
| 24 | const updatedKey = await openRouter.apiKeys.update(keyHash, { |
| 25 | name: 'Updated Key Name', |
| 26 | disabled: true, // Optional: Disable the key |
| 27 | includeByokInLimit: false, // Optional: control BYOK usage in limit |
| 28 | limitReset: 'daily', // Optional: reset limit every day at midnight UTC |
| 29 | }); |
| 30 |  |
| 31 | // Delete a key |
| 32 | await openRouter.apiKeys.delete(keyHash); |
```

## Response Format

API responses return JSON objects containing key information:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "created_at": "2025-02-19T20:52:27.363244+00:00", |
| 5 | "updated_at": "2025-02-19T21:24:11.708154+00:00", |
| 6 | "hash": "<YOUR_KEY_HASH>", |
| 7 | "label": "sk-or-v1-abc...123", |
| 8 | "name": "Customer Key", |
| 9 | "disabled": false, |
| 10 | "limit": 10, |
| 11 | "limit_remaining": 10, |
| 12 | "limit_reset": null, |
| 13 | "include_byok_in_limit": false, |
| 14 | "usage": 0, |
| 15 | "usage_daily": 0, |
| 16 | "usage_weekly": 0, |
| 17 | "usage_monthly": 0, |
| 18 | "byok_usage": 0, |
| 19 | "byok_usage_daily": 0, |
| 20 | "byok_usage_weekly": 0, |
| 21 | "byok_usage_monthly": 0 |
| 22 | } |
| 23 | ] |
| 24 | } |
```

When creating a new key, the response will include the key string itself. Read more in the [API reference](../../../../api-reference/api-keys/create-api-key/index.md).
