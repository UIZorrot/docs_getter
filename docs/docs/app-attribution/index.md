---
source_url: "https://openrouter.ai/docs/app-attribution"
title: "App Attribution | OpenRouter Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:31.115445+00:00"
---
[Features](../guides/features/presets/index.md)

# App Attribution

Get your app featured in OpenRouter rankings and analytics

App attribution allows developers to associate their API usage with their application, enabling visibility in OpenRouter’s public rankings and detailed analytics. By including simple headers in your requests, your app can appear in our leaderboards and gain insights into your model usage patterns.

## Benefits of App Attribution

When you properly attribute your app usage, you gain access to:

- **Public App Rankings**: Your app appears in OpenRouter’s [public rankings](https://openrouter.ai/rankings) with daily, weekly, and monthly leaderboards
- **Model Apps Tabs**: Your app is featured on individual model pages showing which apps use each model most
- **Detailed Analytics**: Access comprehensive analytics showing your app’s model usage over time, token consumption, and usage patterns
- **Professional Visibility**: Showcase your app to the OpenRouter developer community

## Attribution Headers

OpenRouter tracks app attribution through these optional HTTP headers:

### HTTP-Referer

The `HTTP-Referer` header identifies your app’s URL and is used as the primary identifier for rankings.

### X-OpenRouter-Title

The `X-OpenRouter-Title` header sets or modifies your app’s display name
in rankings and analytics. `X-Title` is still supported for backwards compatibility.

### X-OpenRouter-Categories

The `X-OpenRouter-Categories` header assigns your app to one or more marketplace categories. Pass a comma-separated list of up to 2 categories per request. Categories must be lowercase, hyphen-separated, and each category is limited to 30 characters. Only recognized categories from the list below are accepted; unrecognized ones are silently ignored. Categories are merged with any existing ones (up to 10 total).

#### Category Groups

Categories are organized into groups for the [marketplace](https://openrouter.ai/apps):

**Coding** — Tools for software development:

- `cli-agent` — Terminal-based coding assistants
- `ide-extension` — Editor/IDE integrations
- `cloud-agent` — Cloud-hosted coding agents
- `programming-app` — Programming apps
- `native-app-builder` — Mobile and desktop app builders

**Creative** — Creative apps:

- `creative-writing` — Creative writing tools
- `video-gen` — Video generation apps
- `image-gen` — Image generation apps

**Productivity** — Writing and productivity tools:

- `writing-assistant` — AI-powered writing tools
- `general-chat` — General chat apps
- `personal-agent` — Personal AI agents

**Entertainment** — Entertainment apps:

- `roleplay` — Roleplay apps and other character-based chat apps
- `game` — Gaming and interactive entertainment apps

#### Custom Categories

Only recognized categories from the list above are accepted.
Unrecognized values are silently dropped. If you have a use case
that doesn’t fit the existing categories, reach out to us and
we may add new categories in the future.

##### 

All three headers are optional, but including them
enables all attribution features. Apps using localhost
URLs must include a title to be tracked.

## Implementation Examples

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | defaultHeaders: { |
| 6 | 'HTTP-Referer': 'https://myapp.com', // Your app's URL |
| 7 | 'X-OpenRouter-Title': 'My AI Assistant', // Your app's display name |
| 8 | 'X-OpenRouter-Categories': 'cli-agent,cloud-agent', // Optional categories |
| 9 | }, |
| 10 | }); |
| 11 |  |
| 12 | const completion = await openRouter.chat.send({ |
| 13 | model: 'openai/gpt-5.2', |
| 14 | messages: [ |
| 15 | { |
| 16 | role: 'user', |
| 17 | content: 'Hello, world!', |
| 18 | }, |
| 19 | ], |
| 20 | stream: false, |
| 21 | }); |
| 22 |  |
| 23 | console.log(completion.choices[0].message); |
```

## Where Your App Appears

### App Rankings

Your attributed app will appear in OpenRouter’s main rankings page at [openrouter.ai/rankings](https://openrouter.ai/rankings). The rankings show:

- **Top Apps**: Largest public apps by token usage
- **Time Periods**: Daily, weekly, and monthly views
- **Usage Metrics**: Total token consumption across all models

### Model Apps Tabs

On individual model pages (e.g., [GPT-4o](https://openrouter.ai/models/openai/gpt-4o)), your app will be featured in the “Apps” tab showing:

- **Top Apps**: Apps using that specific model most
- **Weekly Rankings**: Updated weekly based on usage
- **Usage Context**: How your app compares to others using the same model

### Individual App Analytics

Once your app is tracked, you can access detailed analytics at `openrouter.ai/apps?url=<your-app-url>` including:

- **Model Usage Over Time**: Charts showing which models your app uses
- **Token Consumption**: Detailed breakdown of prompt and completion tokens
- **Usage Patterns**: Historical data to understand your app’s AI usage trends

## Best Practices

### URL Requirements

- Use your app’s primary domain (e.g., `https://myapp.com`)
- Avoid using subdomains unless they represent distinct apps
- For localhost development, always include a title header

### Title Guidelines

- Keep titles concise and descriptive
- Use your app’s actual name as users know it
- Avoid generic names like “AI App” or “Chatbot”

### Privacy Considerations

- Only public apps, meaning those that send headers, are included in rankings
- Attribution headers don’t expose sensitive information about your requests

## Related Documentation

- [Quickstart Guide](../quickstart/index.md) - Basic setup with attribution headers
- [API Reference](../api-reference/overview/index.md) - Complete header documentation
- [Usage Accounting](../use-cases/usage-accounting/index.md) - Understanding your API usage
