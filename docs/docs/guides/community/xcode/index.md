---
source_url: "https://openrouter.ai/docs/guides/community/xcode"
title: "Xcode Integration | OpenRouter Apple Intelligence Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:55.641598+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Xcode

Using OpenRouter with Apple Intelligence in Xcode

## Using Xcode with Apple Intelligence

[Apple Intelligence](https://developer.apple.com/apple-intelligence) in Xcode 26 provides built-in AI assistance for coding. By integrating OpenRouter, you can access hundreds of AI models directly in your Xcode development environment, going far beyond the default ChatGPT integration.

This integration allows you to use models from Anthropic, Google, Meta, and many other providers without leaving your development environment.

### Prerequisites

##### 

Apple Intelligence on Xcode is currently in Beta and requires:

- **macOS Tahoe 26.0 Beta** or later
- **[Xcode 26 beta 4](https://developer.apple.com/download/applications)** or later

### Setup Instructions

#### Step 1: Access Intelligence Settings

Navigate to **Settings > Intelligence > Add a Model Provider** in your macOS system preferences.

![Xcode Intelligence Settings](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/c46062c0d9931133ed02f265eaaee49b2ee1ca6cf7880ae77bafa26ecea5eab7/content/pages/community/xcode-setup-1.png)

#### Step 2: Configure OpenRouter Provider

In the “Add a Model Provider” dialog, enter the following details:

- **URL**: `https://openrouter.ai/api`
  - **Important**: Do not add `/v1` at the end of the endpoint like you typically would for direct API calls
- **API Key Header**: `Authorization`
- **API Key**: `Bearer YOUR_API_KEY_HERE` (replace `YOUR_API_KEY_HERE` with your OpenRouter API key that starts with `sk-or-v1-`)
- **Description**: `OpenRouter` (or any name you prefer)

Click **Add** to save the configuration.

![OpenRouter Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/592b32c826b6c61f74a2df4b9a82bf193658ecd9a13ecc35d1463d843f161d82/content/pages/community/xcode-setup-2.png)

#### Step 3: Browse Available Models

Once configured, click on **OpenRouter** to see all available models. Since OpenRouter offers hundreds of models, you should bookmark your favorite models for quick access. Bookmarked models will appear at the top of the list, making them easily accessible from within the pane whenever you need them.

![Available Models](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/d836c8a6857842197c7d36eb31d32511ed5c51e0dec68005684f709125e90743/content/pages/community/xcode-setup-3.png)

You’ll have access to models from various providers including:

- Anthropic Claude models
- Google Gemini models
- Meta Llama models
- OpenAI GPT models
- And hundreds more

![Extended Model List](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/bcb38487165ff3b19e52cbe51446a0fbf9bbf6b38a417207c3e5f96b68d19230/content/pages/community/xcode-setup-4.png)

#### Step 4: Start Using AI in Xcode

Head back to the chat interface (icon at the top) and start chatting with your selected models directly in Xcode.

![Xcode Chat Interface](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3087cf6c2b0d3830c356b83cd6097d0ac15bce25a439341066c794e50abe9bc9/content/pages/community/xcode-setup-5.png)

### Using Apple Intelligence Features

Once configured, you can use Apple Intelligence features in Xcode with OpenRouter models:

- **Code Completion**: Get intelligent code suggestions
- **Code Explanation**: Ask questions about your code
- **Refactoring Assistance**: Get help improving your code structure
- **Documentation Generation**: Generate comments and documentation

![Apple Intelligence Interface](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/660a4e6b369fd9cf148744b5a41f8a8970a9432121b8033c8cb2085128ba7dd4/content/pages/community/xcode-setup-6.png)

*Image credit: [Apple Developer Documentation](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)*

### Learn More

- **Apple Intelligence Documentation**: [Writing Code with Intelligence in Xcode](https://developer.apple.com/documentation/Xcode/writing-code-with-intelligence-in-xcode)
- **OpenRouter Quick Start**: [Getting Started with OpenRouter](../../../quickstart/index.md)
- **Available Models**: [Browse OpenRouter Models](https://openrouter.ai/models)
