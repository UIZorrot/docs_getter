---
source_url: "https://openrouter.ai/docs/guides/community/openai-sdk"
title: "OpenAI SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:53.162749+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# OpenAI SDK

Using OpenRouter with OpenAI SDK

## Using the OpenAI SDK

- Using `pip install openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples-python/blob/main/src/openai_test.py).
- Using `npm i openai`: [github](https://github.com/OpenRouterTeam/openrouter-examples/tree/main/typescript).

  ##### 

  You can also use
  [Grit](https://app.grit.io/studio) to
  automatically migrate your code. Simply run `npx @getgrit/launcher openrouter`.

```
|  |  |
| --- | --- |
| 1 | import OpenAI from "openai" |
| 2 |  |
| 3 | const openai = new OpenAI({ |
| 4 | baseURL: "https://openrouter.ai/api/v1", |
| 5 | apiKey: "${API_KEY_REF}", |
| 6 | defaultHeaders: { |
| 7 | ${getHeaderLines().join('\n        ')} |
| 8 | }, |
| 9 | }) |
| 10 |  |
| 11 | async function main() { |
| 12 | const completion = await openai.chat.completions.create({ |
| 13 | model: "${Model.GPT_4_Omni}", |
| 14 | messages: [ |
| 15 | { role: "user", content: "Say this is a test" } |
| 16 | ], |
| 17 | }) |
| 18 |  |
| 19 | console.log(completion.choices[0].message) |
| 20 | } |
| 21 | main(); |
```
