---
source_url: "https://openrouter.ai/docs/guides/overview/multimodal/image-generation"
title: "OpenRouter Image Generation | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:51.004198+00:00"
---
[Overview](../../../../quickstart/index.md)[Multimodal](../overview/index.md)

# Image Generation

How to generate images with OpenRouter models

OpenRouter supports image generation through models that have `"image"` in their `output_modalities`. These models can create images from text prompts when you specify the appropriate modalities in your request.

## Model Discovery

You can find image generation models in several ways:

### Via the API

Use the `output_modalities` query parameter on the [Models API](../../../../api-reference/models/get-models/index.md) to programmatically discover image generation models:

```
|  |  |
| --- | --- |
| $ | # List only image generation models |
| $ | curl "https://openrouter.ai/api/v1/models?output_modalities=image" |
| $ |  |
| $ | # List models that support both text and image output |
| $ | curl "https://openrouter.ai/api/v1/models?output_modalities=text,image" |
```

See [Models - Query Parameters](../../models/index.md) for the full list of supported modality values.

### On the Models Page

Visit the [Models page](https://openrouter.ai/models) and filter by output modalities to find models capable of image generation. Look for models that list `"image"` in their output modalities.

### In the Chatroom

When using the [Chatroom](https://openrouter.ai/chat), click the **Image** button to automatically filter and select models with image generation capabilities. If no image-capable model is active, you’ll be prompted to add one.

## API Usage

To generate images, send a request to the `/api/v1/chat/completions` endpoint with the `modalities` parameter. The value depends on the model’s capabilities:

- **Models that output both text and images** (e.g., Gemini): Use `modalities: ["image", "text"]`
- **Models that only output images** (e.g., Sourceful, Flux): Use `modalities: ["image"]`

### Basic Image Generation

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
| 12 | content: 'Generate a beautiful sunset over mountains', |
| 13 | }, |
| 14 | ], |
| 15 | modalities: ['image', 'text'], |
| 16 | stream: false, |
| 17 | }); |
| 18 |  |
| 19 | // The generated image will be in the assistant message |
| 20 | if (result.choices) { |
| 21 | const message = result.choices[0].message; |
| 22 | if (message.images) { |
| 23 | message.images.forEach((image, index) => { |
| 24 | const imageUrl = image.imageUrl.url; // Base64 data URL |
| 25 | console.log(`Generated image ${index + 1}: ${imageUrl.substring(0, 50)}...`); |
| 26 | }); |
| 27 | } |
| 28 | } |
```

### Image Configuration Options

Some image generation models support additional configuration through the `image_config` parameter.

#### Aspect Ratio

Set `image_config.aspect_ratio` to request specific aspect ratios for generated images.

**Supported aspect ratios:**

- `1:1` → 1024×1024 (default)
- `2:3` → 832×1248
- `3:2` → 1248×832
- `3:4` → 864×1184
- `4:3` → 1184×864
- `4:5` → 896×1152
- `5:4` → 1152×896
- `9:16` → 768×1344
- `16:9` → 1344×768
- `21:9` → 1536×672

**Extended aspect ratios** (supported by [`google/gemini-3.1-flash-image-preview`](https://openrouter.ai/models/google/gemini-3.1-flash-image-preview) only):

- `1:4` → Tall, narrow format ideal for scrolling carousels and vertical UI elements
- `4:1` → Wide, short format for hero banners and horizontal layouts
- `1:8` → Extra-tall format for notification headers and narrow vertical spaces
- `8:1` → Extra-wide format for wide-format banners and panoramic layouts

#### Image Size

Set `image_config.image_size` to control the resolution of generated images.

**Supported sizes:**

- `1K` → Standard resolution (default)
- `2K` → Higher resolution
- `4K` → Highest resolution
- `0.5K` → Lower resolution, optimized for efficiency (supported by [`google/gemini-3.1-flash-image-preview`](https://openrouter.ai/models/google/gemini-3.1-flash-image-preview) only)

You can combine both `aspect_ratio` and `image_size` in the same request:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 |  |
| 4 | url = "https://openrouter.ai/api/v1/chat/completions" |
| 5 | headers = { |
| 6 | "Authorization": f"Bearer {API_KEY_REF}", |
| 7 | "Content-Type": "application/json" |
| 8 | } |
| 9 |  |
| 10 | payload = { |
| 11 | "model": "{{MODEL}}", |
| 12 | "messages": [ |
| 13 | { |
| 14 | "role": "user", |
| 15 | "content": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme" |
| 16 | } |
| 17 | ], |
| 18 | "modalities": ["image", "text"], |
| 19 | "image_config": { |
| 20 | "aspect_ratio": "16:9", |
| 21 | "image_size": "4K" |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | response = requests.post(url, headers=headers, json=payload) |
| 26 | result = response.json() |
| 27 |  |
| 28 | if result.get("choices"): |
| 29 | message = result["choices"][0]["message"] |
| 30 | if message.get("images"): |
| 31 | for image in message["images"]: |
| 32 | image_url = image["image_url"]["url"] |
| 33 | print(f"Generated image: {image_url[:50]}...") |
```

#### Font Inputs (Sourceful only)

Use `image_config.font_inputs` to render custom text with specific fonts in generated images. The text you want to render must also be included in your prompt for best results. This parameter is only supported by Sourceful models (`sourceful/riverflow-v2-fast` and `sourceful/riverflow-v2-pro`).

Each font input is an object with:

- `font_url` (required): URL to the font file
- `text` (required): Text to render with the font

**Limits:**

- Maximum 2 font inputs per request
- Additional cost: $0.03 per font input

**Example:**

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "image_config": { |
| 3 | "font_inputs": [ |
| 4 | { |
| 5 | "font_url": "https://example.com/fonts/custom-font.ttf", |
| 6 | "text": "Hello World" |
| 7 | } |
| 8 | ] |
| 9 | } |
| 10 | } |
```

**Tips for best results:**

- Include the text in your prompt along with details about font name, color, size, and position
- The `text` parameter should match exactly what’s in your prompt - avoid extra wording or quotation marks
- Use line breaks or double spaces to separate headlines and sub-headers when using the same font
- Works best with short, clear headlines and sub-headlines

#### Super Resolution References (Sourceful only)

Use `image_config.super_resolution_references` to enhance low-quality elements in your input image using high-quality reference images. The output image will match the size of your input image, so use larger input images for better results. This parameter is only supported by Sourceful models (`sourceful/riverflow-v2-fast` and `sourceful/riverflow-v2-pro`) when using image-to-image generation (i.e., when input images are provided in `messages`).

**Limits:**

- Maximum 4 reference URLs per request
- Only works with image-to-image requests (ignored when there are no images in `messages`)
- Additional cost: $0.20 per reference

**Example:**

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "image_config": { |
| 3 | "super_resolution_references": [ |
| 4 | "https://example.com/reference1.jpg", |
| 5 | "https://example.com/reference2.jpg" |
| 6 | ] |
| 7 | } |
| 8 | } |
```

**Tips for best results:**

- Supply an input image where the elements to enhance are present but low quality
- Use larger input images for better output quality (output matches input size)
- Use high-quality reference images that show what you want the enhanced elements to look like

### Streaming Image Generation

Image generation also works with streaming responses:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 |  |
| 4 | url = "https://openrouter.ai/api/v1/chat/completions" |
| 5 | headers = { |
| 6 | "Authorization": f"Bearer {API_KEY_REF}", |
| 7 | "Content-Type": "application/json" |
| 8 | } |
| 9 |  |
| 10 | payload = { |
| 11 | "model": "{{MODEL}}", |
| 12 | "messages": [ |
| 13 | { |
| 14 | "role": "user", |
| 15 | "content": "Create an image of a futuristic city" |
| 16 | } |
| 17 | ], |
| 18 | "modalities": ["image", "text"], |
| 19 | "stream": True |
| 20 | } |
| 21 |  |
| 22 | response = requests.post(url, headers=headers, json=payload, stream=True) |
| 23 |  |
| 24 | for line in response.iter_lines(): |
| 25 | if line: |
| 26 | line = line.decode('utf-8') |
| 27 | if line.startswith('data: '): |
| 28 | data = line[6:] |
| 29 | if data != '[DONE]': |
| 30 | try: |
| 31 | chunk = json.loads(data) |
| 32 | if chunk.get("choices"): |
| 33 | delta = chunk["choices"][0].get("delta", {}) |
| 34 | if delta.get("images"): |
| 35 | for image in delta["images"]: |
| 36 | print(f"Generated image: {image['image_url']['url'][:50]}...") |
| 37 | except json.JSONDecodeError: |
| 38 | continue |
```

## Response Format

When generating images, the assistant message includes an `images` field containing the generated images:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "choices": [ |
| 3 | { |
| 4 | "message": { |
| 5 | "role": "assistant", |
| 6 | "content": "I've generated a beautiful sunset image for you.", |
| 7 | "images": [ |
| 8 | { |
| 9 | "type": "image_url", |
| 10 | "image_url": { |
| 11 | "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA..." |
| 12 | } |
| 13 | } |
| 14 | ] |
| 15 | } |
| 16 | } |
| 17 | ] |
| 18 | } |
```

### Image Format

- **Format**: Images are returned as base64-encoded data URLs
- **Types**: Typically PNG format (`data:image/png;base64,`)
- **Multiple Images**: Some models can generate multiple images in a single response
- **Size**: Image dimensions vary by model capabilities

## Model Compatibility

Not all models support image generation. To use this feature:

1. **Check Output Modalities**: Ensure the model has `"image"` in its `output_modalities`
2. **Set Modalities Parameter**: Use `["image", "text"]` for models that output both, or `["image"]` for image-only models
3. **Use Compatible Models**: Examples include:
   - `google/gemini-3.1-flash-image-preview` (supports extended aspect ratios and 0.5K resolution)
   - `google/gemini-2.5-flash-image`
   - `black-forest-labs/flux.2-pro`
   - `black-forest-labs/flux.2-flex`
   - `sourceful/riverflow-v2-standard-preview`
   - Other models with image generation capabilities

## Best Practices

- **Clear Prompts**: Provide detailed descriptions for better image quality
- **Model Selection**: Choose models specifically designed for image generation
- **Error Handling**: Check for the `images` field in responses before processing
- **Rate Limits**: Image generation may have different rate limits than text generation
- **Storage**: Consider how you’ll handle and store the base64 image data

## Troubleshooting

**No images in response?**

- Verify the model supports image generation (`output_modalities` includes `"image"`)
- Ensure you’ve set the `modalities` parameter correctly: `["image", "text"]` for models that output both, or `["image"]` for image-only models
- Check that your prompt is requesting image generation

**Model not found?**

- Use the [Models page](https://openrouter.ai/models) to find available image generation models
- Filter by output modalities to see compatible models
