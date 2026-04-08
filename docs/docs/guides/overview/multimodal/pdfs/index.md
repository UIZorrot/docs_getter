---
source_url: "https://openrouter.ai/docs/guides/overview/multimodal/pdfs"
title: "OpenRouter PDF Inputs | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:57.307551+00:00"
---
[Overview](../../../../quickstart/index.md)[Multimodal](../overview/index.md)

# PDF Inputs

How to send PDFs to OpenRouter models

OpenRouter supports PDF processing through the `/api/v1/chat/completions` API. PDFs can be sent as **direct URLs** or **base64-encoded data URLs** in the messages array, via the file content type. This feature works on **any** model on OpenRouter.

**URL support**: Send publicly accessible PDFs directly without downloading or encoding
**Base64 support**: Required for local files or private documents that aren’t publicly accessible

PDFs also work in the chat room for interactive testing.

##### 

When a model supports file input natively, the PDF is passed directly to the
model. When the model does not support file input natively, OpenRouter will
parse the file and pass the parsed results to the requested model.

##### 

You can send both PDFs and other file types in the same request.

## Plugin Configuration

To configure PDF processing, use the `plugins` parameter in your request. OpenRouter provides several PDF processing engines with different capabilities and pricing:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | plugins: [ |
| 3 | { |
| 4 | id: 'file-parser', |
| 5 | pdf: { |
| 6 | engine: 'cloudflare-ai', // or 'mistral-ocr' or 'native' |
| 7 | }, |
| 8 | }, |
| 9 | ], |
| 10 | } |
```

## Pricing

OpenRouter provides several PDF processing engines:

1. `"mistral-ocr"`: Best for scanned documents or
   PDFs with images ($2 per 1,000 pages).
2. `"cloudflare-ai"`: Converts PDFs to markdown
   using Cloudflare Workers AI (Free).
3. `"native"`: Only available for models that
   support file input natively (charged as input tokens).

##### 

The `"pdf-text"` engine is deprecated and automatically redirected to
`"cloudflare-ai"`. Existing requests using `"pdf-text"` will continue to work.

If you don’t explicitly specify an engine, OpenRouter will default first to the model’s native file processing capabilities, and if that’s not available, we will use the `"mistral-ocr"` engine.

## Using PDF URLs

For publicly accessible PDFs, you can send the URL directly without needing to download and encode the file:

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
| 15 | text: 'What are the main points in this document?', |
| 16 | }, |
| 17 | { |
| 18 | type: 'file', |
| 19 | file: { |
| 20 | filename: 'document.pdf', |
| 21 | fileData: 'https://bitcoin.org/bitcoin.pdf', |
| 22 | }, |
| 23 | }, |
| 24 | ], |
| 25 | }, |
| 26 | ], |
| 27 | // Optional: Configure PDF processing engine |
| 28 | plugins: [ |
| 29 | { |
| 30 | id: 'file-parser', |
| 31 | pdf: { |
| 32 | engine: '{{ENGINE}}', |
| 33 | }, |
| 34 | }, |
| 35 | ], |
| 36 | stream: false, |
| 37 | }); |
| 38 |  |
| 39 | console.log(result); |
```

##### 

PDF URLs work with all processing engines. For Mistral OCR, the URL is passed directly to the service. For other engines, OpenRouter fetches the PDF and processes it internally.

## Using Base64 Encoded PDFs

For local PDF files or when you need to send PDF content directly, you can base64 encode the file:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 | import base64 |
| 4 | from pathlib import Path |
| 5 |  |
| 6 | def encode_pdf_to_base64(pdf_path): |
| 7 | with open(pdf_path, "rb") as pdf_file: |
| 8 | return base64.b64encode(pdf_file.read()).decode('utf-8') |
| 9 |  |
| 10 | url = "https://openrouter.ai/api/v1/chat/completions" |
| 11 | headers = { |
| 12 | "Authorization": f"Bearer {API_KEY_REF}", |
| 13 | "Content-Type": "application/json" |
| 14 | } |
| 15 |  |
| 16 | # Read and encode the PDF |
| 17 | pdf_path = "path/to/your/document.pdf" |
| 18 | base64_pdf = encode_pdf_to_base64(pdf_path) |
| 19 | data_url = f"data:application/pdf;base64,{base64_pdf}" |
| 20 |  |
| 21 | messages = [ |
| 22 | { |
| 23 | "role": "user", |
| 24 | "content": [ |
| 25 | { |
| 26 | "type": "text", |
| 27 | "text": "What are the main points in this document?" |
| 28 | }, |
| 29 | { |
| 30 | "type": "file", |
| 31 | "file": { |
| 32 | "filename": "document.pdf", |
| 33 | "file_data": data_url |
| 34 | } |
| 35 | }, |
| 36 | ] |
| 37 | } |
| 38 | ] |
| 39 |  |
| 40 | # Optional: Configure PDF processing engine |
| 41 | # PDF parsing will still work even if the plugin is not explicitly set |
| 42 | plugins = [ |
| 43 | { |
| 44 | "id": "file-parser", |
| 45 | "pdf": { |
| 46 | "engine": "{{ENGINE}}"  # defaults to "{{DEFAULT_PDF_ENGINE}}". See Pricing above |
| 47 | } |
| 48 | } |
| 49 | ] |
| 50 |  |
| 51 | payload = { |
| 52 | "model": "{{MODEL}}", |
| 53 | "messages": messages, |
| 54 | "plugins": plugins |
| 55 | } |
| 56 |  |
| 57 | response = requests.post(url, headers=headers, json=payload) |
| 58 | print(response.json()) |
```

## Skip Parsing Costs

When you send a PDF to the API, the response may include file annotations in the assistant’s message. These annotations contain structured information about the PDF document that was parsed. By sending these annotations back in subsequent requests, you can avoid re-parsing the same PDF document multiple times, which saves both processing time and costs.

Here’s how to reuse file annotations:

```
|  |  |
| --- | --- |
| 1 | import requests |
| 2 | import json |
| 3 | import base64 |
| 4 | from pathlib import Path |
| 5 |  |
| 6 | # First, encode and send the PDF |
| 7 | def encode_pdf_to_base64(pdf_path): |
| 8 | with open(pdf_path, "rb") as pdf_file: |
| 9 | return base64.b64encode(pdf_file.read()).decode('utf-8') |
| 10 |  |
| 11 | url = "https://openrouter.ai/api/v1/chat/completions" |
| 12 | headers = { |
| 13 | "Authorization": f"Bearer {API_KEY_REF}", |
| 14 | "Content-Type": "application/json" |
| 15 | } |
| 16 |  |
| 17 | # Read and encode the PDF |
| 18 | pdf_path = "path/to/your/document.pdf" |
| 19 | base64_pdf = encode_pdf_to_base64(pdf_path) |
| 20 | data_url = f"data:application/pdf;base64,{base64_pdf}" |
| 21 |  |
| 22 | # Initial request with the PDF |
| 23 | messages = [ |
| 24 | { |
| 25 | "role": "user", |
| 26 | "content": [ |
| 27 | { |
| 28 | "type": "text", |
| 29 | "text": "What are the main points in this document?" |
| 30 | }, |
| 31 | { |
| 32 | "type": "file", |
| 33 | "file": { |
| 34 | "filename": "document.pdf", |
| 35 | "file_data": data_url |
| 36 | } |
| 37 | }, |
| 38 | ] |
| 39 | } |
| 40 | ] |
| 41 |  |
| 42 | payload = { |
| 43 | "model": "{{MODEL}}", |
| 44 | "messages": messages |
| 45 | } |
| 46 |  |
| 47 | response = requests.post(url, headers=headers, json=payload) |
| 48 | response_data = response.json() |
| 49 |  |
| 50 | # Store the annotations from the response |
| 51 | file_annotations = None |
| 52 | if response_data.get("choices") and len(response_data["choices"]) > 0: |
| 53 | if "annotations" in response_data["choices"][0]["message"]: |
| 54 | file_annotations = response_data["choices"][0]["message"]["annotations"] |
| 55 |  |
| 56 | # Follow-up request using the annotations (without sending the PDF again) |
| 57 | if file_annotations: |
| 58 | follow_up_messages = [ |
| 59 | { |
| 60 | "role": "user", |
| 61 | "content": [ |
| 62 | { |
| 63 | "type": "text", |
| 64 | "text": "What are the main points in this document?" |
| 65 | }, |
| 66 | { |
| 67 | "type": "file", |
| 68 | "file": { |
| 69 | "filename": "document.pdf", |
| 70 | "file_data": data_url |
| 71 | } |
| 72 | } |
| 73 | ] |
| 74 | }, |
| 75 | { |
| 76 | "role": "assistant", |
| 77 | "content": "The document contains information about...", |
| 78 | "annotations": file_annotations |
| 79 | }, |
| 80 | { |
| 81 | "role": "user", |
| 82 | "content": "Can you elaborate on the second point?" |
| 83 | } |
| 84 | ] |
| 85 |  |
| 86 | follow_up_payload = { |
| 87 | "model": "{{MODEL}}", |
| 88 | "messages": follow_up_messages |
| 89 | } |
| 90 |  |
| 91 | follow_up_response = requests.post(url, headers=headers, json=follow_up_payload) |
| 92 | print(follow_up_response.json()) |
```

##### 

When you include the file annotations from a previous response in your
subsequent requests, OpenRouter will use this pre-parsed information instead
of re-parsing the PDF, which saves processing time and costs. This is
especially beneficial for large documents or when using the `mistral-ocr`
engine which incurs additional costs.

## File Annotations Schema

When OpenRouter parses a PDF, the response includes file annotations in the assistant message. Here is the TypeScript type for the annotation schema:

```
|  |  |
| --- | --- |
| 1 | type FileAnnotation = { |
| 2 | type: 'file'; |
| 3 | file: { |
| 4 | hash: string;           // Unique hash identifying the parsed file |
| 5 | name?: string;          // Original filename (optional) |
| 6 | content: ContentPart[]; // Parsed content from the file |
| 7 | }; |
| 8 | }; |
| 9 |  |
| 10 | type ContentPart = |
| 11 | | { type: 'text'; text: string } |
| 12 | | { type: 'image_url'; image_url: { url: string } }; |
```

The `content` array contains the parsed content from the PDF, which may include text blocks and images (as base64 data URLs). The `hash` field uniquely identifies the parsed file content and is used to skip re-parsing when you include the annotation in subsequent requests.

## Response Format

The API will return a response in the following format:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "gen-1234567890", |
| 3 | "provider": "DeepInfra", |
| 4 | "model": "google/gemma-3-27b-it", |
| 5 | "object": "chat.completion", |
| 6 | "created": 1234567890, |
| 7 | "choices": [ |
| 8 | { |
| 9 | "message": { |
| 10 | "role": "assistant", |
| 11 | "content": "The document discusses...", |
| 12 | "annotations": [ |
| 13 | { |
| 14 | "type": "file", |
| 15 | "file": { |
| 16 | "hash": "abc123...", |
| 17 | "name": "document.pdf", |
| 18 | "content": [ |
| 19 | { "type": "text", "text": "Parsed text content..." }, |
| 20 | { "type": "image_url", "image_url": { "url": "data:image/png;base64,..." } } |
| 21 | ] |
| 22 | } |
| 23 | } |
| 24 | ] |
| 25 | } |
| 26 | } |
| 27 | ], |
| 28 | "usage": { |
| 29 | "prompt_tokens": 1000, |
| 30 | "completion_tokens": 100, |
| 31 | "total_tokens": 1100 |
| 32 | } |
| 33 | } |
```
