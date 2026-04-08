---
source_url: "https://openrouter.ai/docs/guides/overview/multimodal/audio"
title: "OpenRouter Audio | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:57.476757+00:00"
---
[Overview](../../../../quickstart/index.md)[Multimodal](../overview/index.md)

# Audio

How to send and receive audio with OpenRouter models

OpenRouter supports both sending audio files to compatible models and receiving audio responses via the API. This guide covers how to work with audio inputs and outputs.

## Audio Inputs

Send audio files to compatible models for transcription, analysis, and processing. Audio input requests use the `/api/v1/chat/completions` API with the `input_audio` content type. Audio files must be base64-encoded and include the format specification.

**Note**: Audio files must be **base64-encoded** - direct URLs are not supported for audio content.

You can search for models that support audio input by filtering to audio input modality on our [Models page](https://openrouter.ai/models).

### Sending Audio Files

Here’s how to send an audio file for processing:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 | import fs from "fs/promises"; |
| 3 |  |
| 4 | const openRouter = new OpenRouter({ |
| 5 | apiKey: '{{API_KEY_REF}}', |
| 6 | }); |
| 7 |  |
| 8 | async function encodeAudioToBase64(audioPath: string): Promise<string> { |
| 9 | const audioBuffer = await fs.readFile(audioPath); |
| 10 | return audioBuffer.toString("base64"); |
| 11 | } |
| 12 |  |
| 13 | // Read and encode the audio file |
| 14 | const audioPath = "path/to/your/audio.wav"; |
| 15 | const base64Audio = await encodeAudioToBase64(audioPath); |
| 16 |  |
| 17 | const result = await openRouter.chat.send({ |
| 18 | model: "{{MODEL}}", |
| 19 | messages: [ |
| 20 | { |
| 21 | role: "user", |
| 22 | content: [ |
| 23 | { |
| 24 | type: "text", |
| 25 | text: "Please transcribe this audio file.", |
| 26 | }, |
| 27 | { |
| 28 | type: "input_audio", |
| 29 | inputAudio: { |
| 30 | data: base64Audio, |
| 31 | format: "wav", |
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

### Supported Audio Input Formats

Supported audio formats vary by provider. Common formats include:

- `wav` - WAV audio
- `mp3` - MP3 audio
- `aiff` - AIFF audio
- `aac` - AAC audio
- `ogg` - OGG Vorbis audio
- `flac` - FLAC audio
- `m4a` - M4A audio
- `pcm16` - PCM16 audio
- `pcm24` - PCM24 audio

**Note:** Check your model’s documentation to confirm which audio formats it supports. Not all models support all formats.

## Audio Output

OpenRouter supports receiving audio responses from models that have audio output capabilities. To request audio output, include the `modalities` and `audio` parameters in your request.

You can search for models that support audio output by filtering to audio output modality on our [Models page](https://openrouter.ai/models).

### Requesting Audio Output

To receive audio output, set `modalities` to `["text", "audio"]` and provide the `audio` configuration with your desired voice and format:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 | import base64 |
| 4 |  |
| 5 | url = "https://openrouter.ai/api/v1/chat/completions" |
| 6 | headers = { |
| 7 | "Authorization": f"Bearer {API_KEY_REF}", |
| 8 | "Content-Type": "application/json" |
| 9 | } |
| 10 |  |
| 11 | payload = { |
| 12 | "model": "{{MODEL}}", |
| 13 | "messages": [ |
| 14 | { |
| 15 | "role": "user", |
| 16 | "content": "Say hello in a friendly tone." |
| 17 | } |
| 18 | ], |
| 19 | "modalities": ["text", "audio"], |
| 20 | "audio": { |
| 21 | "voice": "alloy", |
| 22 | "format": "wav" |
| 23 | }, |
| 24 | "stream": True |
| 25 | } |
| 26 |  |
| 27 | # Audio output requires streaming — the response is delivered as SSE chunks |
| 28 | response = requests.post(url, headers=headers, json=payload, stream=True) |
| 29 |  |
| 30 | audio_data_chunks = [] |
| 31 | transcript_chunks = [] |
| 32 |  |
| 33 | for line in response.iter_lines(): |
| 34 | if not line: |
| 35 | continue |
| 36 | decoded = line.decode("utf-8") |
| 37 | if not decoded.startswith("data: "): |
| 38 | continue |
| 39 | data = decoded[len("data: "):] |
| 40 | if data.strip() == "[DONE]": |
| 41 | break |
| 42 | chunk = json.loads(data) |
| 43 | delta = chunk["choices"][0].get("delta", {}) |
| 44 | audio = delta.get("audio", {}) |
| 45 | if audio.get("data"): |
| 46 | audio_data_chunks.append(audio["data"]) |
| 47 | if audio.get("transcript"): |
| 48 | transcript_chunks.append(audio["transcript"]) |
| 49 |  |
| 50 | transcript = "".join(transcript_chunks) |
| 51 | print(f"Transcript: {transcript}") |
| 52 |  |
| 53 | # Combine and decode the base64 audio chunks, then save |
| 54 | full_audio_b64 = "".join(audio_data_chunks) |
| 55 | audio_bytes = base64.b64decode(full_audio_b64) |
| 56 | with open("output.wav", "wb") as f: |
| 57 | f.write(audio_bytes) |
```

### Streaming Chunk Format

Audio output requires streaming (`stream: true`). Audio data and transcript are delivered incrementally via the `delta.audio` field in each chunk:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "choices": [ |
| 3 | { |
| 4 | "delta": { |
| 5 | "audio": { |
| 6 | "data": "<base64-encoded audio chunk>", |
| 7 | "transcript": "Hello" |
| 8 | } |
| 9 | } |
| 10 | } |
| 11 | ] |
| 12 | } |
```

### Audio Configuration Options

The `audio` parameter accepts the following options:

| Option | Description |
| --- | --- |
| `voice` | The voice to use for audio generation (e.g., `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`). Available voices vary by model. |
| `format` | The audio format for the output (e.g., `wav`, `mp3`, `flac`, `opus`, `pcm16`). Available formats vary by model. |
