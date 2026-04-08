---
source_url: "https://openrouter.ai/docs/guides/overview/multimodal/images"
title: "OpenRouter Image Inputs | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:56.864452+00:00"
---
[Overview](../../../../quickstart/index.md)[Multimodal](../overview/index.md)

# Image Inputs

How to send images to OpenRouter models

Requests with images, to multimodel models, are available via the `/api/v1/chat/completions` API with a multi-part `messages` parameter. The `image_url` can either be a URL or a base64-encoded image. Note that multiple images can be sent in separate content array entries. The number of images you can send in a single request varies per provider and per model. Due to how the content is parsed, we recommend sending the text prompt first, then the images. If the images must come first, we recommend putting it in the system prompt.

OpenRouter supports both **direct URLs** and **base64-encoded data** for images:

- **URLs**: More efficient for publicly accessible images as they don’t require local encoding
- **Base64**: Required for local files or private images that aren’t publicly accessible

### Using Image URLs

Here’s how to send an image using a URL:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const result = await openRouter.chat.send({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: [ |
| 13 | { |
| 14 | type: 'text', |
| 15 | text: "What's in this image?", |
| 16 | }, |
| 17 | { |
| 18 | type: 'image_url', |
| 19 | imageUrl: { |
| 20 | url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg', |
| 21 | }, |
| 22 | }, |
| 23 | ], |
| 24 | }, |
| 25 | ], |
| 26 | stream: false, |
| 27 | }); |
| 28 |  |
| 29 | console.log(result); |
```

### Using Base64 Encoded Images

For locally stored images, you can send them using base64 encoding. Here’s how to do it:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 | import * as fs from 'fs'; |
| 3 |  |
| 4 | const openRouter = new OpenRouter({ |
| 5 | apiKey: '{{API_KEY_REF}}', |
| 6 | }); |
| 7 |  |
| 8 | async function encodeImageToBase64(imagePath: string): Promise<string> { |
| 9 | const imageBuffer = await fs.promises.readFile(imagePath); |
| 10 | const base64Image = imageBuffer.toString('base64'); |
| 11 | return `data:image/jpeg;base64,${base64Image}`; |
| 12 | } |
| 13 |  |
| 14 | // Read and encode the image |
| 15 | const imagePath = 'path/to/your/image.jpg'; |
| 16 | const base64Image = await encodeImageToBase64(imagePath); |
| 17 |  |
| 18 | const result = await openRouter.chat.send({ |
| 19 | model: '{{MODEL}}', |
| 20 | messages: [ |
| 21 | { |
| 22 | role: 'user', |
| 23 | content: [ |
| 24 | { |
| 25 | type: 'text', |
| 26 | text: "What's in this image?", |
| 27 | }, |
| 28 | { |
| 29 | type: 'image_url', |
| 30 | imageUrl: { |
| 31 | url: base64Image, |
| 32 | }, |
| 33 | }, |
| 34 | ], |
| 35 | }, |
| 36 | ], |
| 37 | stream: false, |
| 38 | }); |
| 39 |  |
| 40 | console.log(result); |
```

Supported image content types are:

- `image/png`
- `image/jpeg`
- `image/webp`
- `image/gif`
