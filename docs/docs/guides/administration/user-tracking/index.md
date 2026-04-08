---
source_url: "https://openrouter.ai/docs/guides/administration/user-tracking"
title: "User Tracking | Track Your Users with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:31.420490+00:00"
---
[Guides](../activity-export/index.md)[Administration](../activity-export/index.md)

# User Tracking

The OpenRouter API supports **User Tracking** through the optional `user` parameter, allowing you to track your own user IDs and improve your application’s reporting capabilities.

## What is User Tracking?

User tracking enables you to specify an arbitrary string identifier for your end-users in API requests. This optional metadata helps OpenRouter understand your sub-users.

## How It Works

Simply include a `user` parameter in your API requests with any string identifier that represents your end-user. This could be a user ID, email hash, session identifier, or any other stable identifier you use in your application.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [ |
| 4 | {"role": "user", "content": "Hello, how are you?"} |
| 5 | ], |
| 6 | "user": "user_12345" |
| 7 | } |
```

## Implementation Example

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const response = await openRouter.chat.send({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: "What's the weather like today?", |
| 13 | }, |
| 14 | ], |
| 15 | user: 'user_12345', // Your user identifier |
| 16 | stream: false, |
| 17 | }); |
| 18 |  |
| 19 | console.log(response.choices[0].message.content); |
```

## Best Practices

### Choose Stable Identifiers

Use consistent, stable identifiers for the same user across requests:

- **Good**: `user_12345`, `customer_abc123`, `account_xyz789`
- **Avoid**: Random strings that change between requests

### Consider Privacy

When using user identifiers, consider privacy implications:

- Use internal user IDs rather than exposing personal information
- Avoid including personally identifiable information in user identifiers
- Consider using anonymized identifiers for better privacy protection

### Be Consistent

Use the same user identifier format throughout your application:

```
|  |  |
| --- | --- |
| 1 | # Consistent format |
| 2 | user_id = f"app_{internal_user_id}" |
```
