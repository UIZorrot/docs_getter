---
source_url: "https://openrouter.ai/docs/api/reference/authentication"
title: "API Authentication | OpenRouter OAuth and API Keys | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:51.053180+00:00"
---
[API Guides](../overview/index.md)

# Authentication

API Authentication

You can cover model costs with OpenRouter API keys.

Our API authenticates requests using Bearer tokens. This allows you to use `curl` or the [OpenAI SDK](https://platform.openai.com/docs/frameworks) directly with OpenRouter.

##### 

API keys on OpenRouter are more powerful than keys used directly for model APIs.

They allow users to set credit limits for apps, and they can be used in [OAuth](../../../guides/overview/auth/oauth/index.md) flows.

## Using an API key

To use an API key, [first create your key](https://openrouter.ai/keys). Give it a name and you can optionally set a credit limit.

If you’re calling the OpenRouter API directly, set the `Authorization` header to a Bearer token with your API key.

If you’re using the OpenAI Typescript SDK, set the `api_base` to `https://openrouter.ai/api/v1` and the `apiKey` to your API key.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | defaultHeaders: { |
| 6 | 'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai. |
| 7 | 'X-OpenRouter-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai. |
| 8 | }, |
| 9 | }); |
| 10 |  |
| 11 | const completion = await openRouter.chat.send({ |
| 12 | model: 'openai/gpt-5.2', |
| 13 | messages: [{ role: 'user', content: 'Say this is a test' }], |
| 14 | stream: false, |
| 15 | }); |
| 16 |  |
| 17 | console.log(completion.choices[0].message); |
```

To stream with Python, [see this example from OpenAI](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb).

## If your key has been exposed

##### 

You must protect your API keys and never commit them to public repositories.

OpenRouter is a GitHub secret scanning partner, and has other methods to detect exposed keys. If we determine that your key has been compromised, you will receive an email notification.

If you receive such a notification or suspect your key has been exposed, immediately visit [your key settings page](https://openrouter.ai/settings/keys) to delete the compromised key and create a new one.

Using environment variables and keeping keys out of your codebase is strongly recommended.
