---
source_url: "https://openrouter.ai/docs/guides/overview/multimodal/videos"
title: "OpenRouter Video Inputs | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:58.484286+00:00"
---
[Overview](../../../../quickstart/index.md)[Multimodal](../overview/index.md)

# Video Inputs

How to send video files to OpenRouter models

OpenRouter supports sending video files to compatible models via the API. This guide will show you how to work with video using our API.

OpenRouter supports both **direct URLs** and **base64-encoded data URLs** for videos:

- **URLs**: Efficient for publicly accessible videos as they don’t require local encoding
- **Base64 Data URLs**: Required for local files or private videos that aren’t publicly accessible

##### 

**Important:** Video URL support varies by provider. OpenRouter only sends video URLs to providers that explicitly support them. For example, Google Gemini on AI Studio only supports YouTube links (not Vertex AI).

##### 

**API Only:** Video inputs are currently only supported via the API. Video uploads are not available in the OpenRouter chatroom interface at this time.

## Video Inputs

Requests with video files to compatible models are available via the `/api/v1/chat/completions` API with the `video_url` content type. The `url` can either be a URL or a base64-encoded data URL. Note that only models with video processing capabilities will handle these requests.

You can search for models that support video by filtering to video input modality on our [Models page](https://openrouter.ai/models).

### Using Video URLs

Here’s how to send a video using a URL. Note that for Google Gemini on AI Studio, only YouTube links are supported:

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
| 8 | model: "{{MODEL}}", |
| 9 | messages: [ |
| 10 | { |
| 11 | role: "user", |
| 12 | content: [ |
| 13 | { |
| 14 | type: "text", |
| 15 | text: "Please describe what's happening in this video.", |
| 16 | }, |
| 17 | { |
| 18 | type: "video_url", |
| 19 | videoUrl: { |
| 20 | url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ", |
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

### Using Base64 Encoded Videos

For locally stored videos, you can send them using base64 encoding as data URLs:

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
| 8 | async function encodeVideoToBase64(videoPath: string): Promise<string> { |
| 9 | const videoBuffer = await fs.promises.readFile(videoPath); |
| 10 | const base64Video = videoBuffer.toString('base64'); |
| 11 | return `data:video/mp4;base64,${base64Video}`; |
| 12 | } |
| 13 |  |
| 14 | // Read and encode the video |
| 15 | const videoPath = 'path/to/your/video.mp4'; |
| 16 | const base64Video = await encodeVideoToBase64(videoPath); |
| 17 |  |
| 18 | const result = await openRouter.chat.send({ |
| 19 | model: '{{MODEL}}', |
| 20 | messages: [ |
| 21 | { |
| 22 | role: 'user', |
| 23 | content: [ |
| 24 | { |
| 25 | type: 'text', |
| 26 | text: "What's in this video?", |
| 27 | }, |
| 28 | { |
| 29 | type: 'video_url', |
| 30 | videoUrl: { |
| 31 | url: base64Video, |
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

## Supported Video Formats

OpenRouter supports the following video formats:

- `video/mp4`
- `video/mpeg`
- `video/mov`
- `video/webm`

## Common Use Cases

Video inputs enable a wide range of applications:

- **Video Summarization**: Generate text summaries of video content
- **Object and Activity Recognition**: Identify objects, people, and actions in videos
- **Scene Understanding**: Describe settings, environments, and contexts
- **Sports Analysis**: Analyze gameplay, movements, and tactics
- **Surveillance**: Monitor and analyze security footage
- **Educational Content**: Analyze instructional videos and provide insights

## Best Practices

### File Size Considerations

Video files can be large, which affects both upload time and processing costs:

- **Compress videos** when possible to reduce file size without significant quality loss
- **Trim videos** to include only relevant segments
- **Consider resolution**: Lower resolutions (e.g., 720p vs 4K) reduce file size while maintaining usability for most analysis tasks
- **Frame rate**: Lower frame rates can reduce file size for videos where high temporal resolution isn’t critical

### Optimal Video Length

Different models may have different limits on video duration:

- Check model-specific documentation for maximum video length
- For long videos, consider splitting into shorter segments
- Focus on key moments rather than sending entire long-form content

### Quality vs. Size Trade-offs

Balance video quality with practical considerations:

- **High quality** (1080p+, high bitrate): Best for detailed visual analysis, object detection, text recognition
- **Medium quality** (720p, moderate bitrate): Suitable for most general analysis tasks
- **Lower quality** (480p, lower bitrate): Acceptable for basic scene understanding and action recognition

## Provider-Specific Video URL Support

Video URL support varies significantly by provider:

- **Google Gemini (AI Studio)**: Only supports YouTube links (e.g., `https://www.youtube.com/watch?v=...`)
- **Google Gemini (Vertex AI)**: Does not support video URLs - use base64-encoded data URLs instead
- **Other providers**: Check model-specific documentation for video URL support

## Troubleshooting

**Video not processing?**

- Verify the model supports video input (check `input_modalities` includes `"video"`)
- If using a video URL, confirm the provider supports video URLs (see Provider-Specific Video URL Support above)
- For Gemini on AI Studio, ensure you’re using a YouTube link, not a direct video file URL
- If the video URL isn’t working, try using a base64-encoded data URL instead
- Check that the video format is supported
- Verify the video file isn’t corrupted

**Large file errors?**

- Compress the video to reduce file size
- Reduce video resolution or frame rate
- Trim the video to a shorter duration
- Check model-specific file size limits
- Consider using a video URL (if supported by the provider) instead of base64 encoding for large files

**Poor analysis results?**

- Ensure video quality is sufficient for the task
- Provide clear, specific prompts about what to analyze
- Consider if the video duration is appropriate for the model
- Check if the video content is clearly visible and well-lit
