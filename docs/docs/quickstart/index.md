---
source_url: "https://openrouter.ai/docs/quickstart"
title: "OpenRouter Quickstart Guide | Developer Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:25.426802+00:00"
---
[Overview](index.md)

# Quickstart

Get started with OpenRouter

OpenRouter provides a unified API that gives you access to hundreds of AI models through a single endpoint, while automatically handling fallbacks and selecting the most cost-effective options. Get started with just a few lines of code using your preferred SDK or framework.

##### 

```
|  |
| --- |
| Read https://openrouter.ai/skills/create-agent/SKILL.md and follow the instructions to build an agent using OpenRouter. |
```

##### 

Looking for information about free models and rate limits? Please see the [FAQ](../faq/index.md)

In the examples below, the OpenRouter-specific headers are optional. Setting them allows your app to appear on the OpenRouter leaderboards. For detailed information about app attribution, see our [App Attribution guide](../app-attribution/index.md).

## Using the OpenRouter SDK (Beta)

First, install the SDK:

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/sdk |
```

Then use it in your code:

TypeScript SDK

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
| 13 | messages: [ |
| 14 | { |
| 15 | role: 'user', |
| 16 | content: 'What is the meaning of life?', |
| 17 | }, |
| 18 | ], |
| 19 | stream: false, |
| 20 | }); |
| 21 |  |
| 22 | console.log(completion.choices[0].message.content); |
```

## Using the OpenRouter API directly

##### 

You can use the interactive [Request Builder](https://openrouter.ai/request-builder) to generate OpenRouter API requests in the language of your choice.

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 |  |
| 4 | response = requests.post( |
| 5 | url="https://openrouter.ai/api/v1/chat/completions", |
| 6 | headers={ |
| 7 | "Authorization": "Bearer <OPENROUTER_API_KEY>", |
| 8 | "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai. |
| 9 | "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai. |
| 10 | }, |
| 11 | data=json.dumps({ |
| 12 | "model": "openai/gpt-5.2", # Optional |
| 13 | "messages": [ |
| 14 | { |
| 15 | "role": "user", |
| 16 | "content": "What is the meaning of life?" |
| 17 | } |
| 18 | ] |
| 19 | }) |
| 20 | ) |
```

## Using the OpenAI SDK

```
|  |  |
| --- | --- |
| 1 | import OpenAI from 'openai'; |
| 2 |  |
| 3 | const openai = new OpenAI({ |
| 4 | baseURL: 'https://openrouter.ai/api/v1', |
| 5 | apiKey: '<OPENROUTER_API_KEY>', |
| 6 | defaultHeaders: { |
| 7 | 'HTTP-Referer': '<YOUR_SITE_URL>', // Optional. Site URL for rankings on openrouter.ai. |
| 8 | 'X-OpenRouter-Title': '<YOUR_SITE_NAME>', // Optional. Site title for rankings on openrouter.ai. |
| 9 | }, |
| 10 | }); |
| 11 |  |
| 12 | async function main() { |
| 13 | const completion = await openai.chat.completions.create({ |
| 14 | model: 'openai/gpt-5.2', |
| 15 | messages: [ |
| 16 | { |
| 17 | role: 'user', |
| 18 | content: 'What is the meaning of life?', |
| 19 | }, |
| 20 | ], |
| 21 | }); |
| 22 |  |
| 23 | console.log(completion.choices[0].message); |
| 24 | } |
| 25 |  |
| 26 | main(); |
```

The API also supports [streaming](../api/reference/streaming/index.md).

## Using third-party SDKs

For information about using third-party SDKs and frameworks with OpenRouter, please [see our frameworks documentation.](../guides/community/frameworks-and-integrations-overview/index.md)
