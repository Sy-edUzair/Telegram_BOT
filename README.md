# Telegram_BOT
This Telegram bot uses the DialoGPT model from Hugging Face's Transformers library to provide conversational responses. It handles both private chats and group chats, responding to commands and messages as appropriate.
![image](https://github.com/Sy-edUzair/Telegram_BOT/assets/115092632/e18d64a2-b9fa-4b5b-bf33-b8570cbb9098)

## Features

- **Commands Supported**:
  - `/start`: Initiates a conversation with the bot.
  - `/help`: Provides guidance on using the bot.

- **Messaging**:
  - Handles messages in private chats directly.
  - In group chats, responds only when mentioned (`@Python1233bot`).

- **Error Handling**:
  - Logs errors encountered during bot operation.

## Requirements

- Python 3.6+
- `telegram`, `transformers` libraries
- DialoGPT model (`microsoft/DialoGPT-medium`)

## Setup

1. Install dependencies:
   ```bash
   pip install python-telegram-bot torch tranformers
2. Obtain a Telegram bot token from BotFather and replace TOKEN in main.py with your token.

3. Optionally, if behind a proxy, set PROXY_URL accordingly in main.py.

4. Run the bot:
   ```bash
   python bot.py

## Usage
1. Start a chat with the bot using /start.
2. Use /help for instructions on using the bot.
3. In private chats, the bot responds directly to messages.
4. In group chats, mention @Python1233bot followed by your message to get a response.

## Notes
1. The bot is configured to run with a polling mechanism (app.run_polling).
2. Ensure proper handling of context.error in case of any issues.

This project is licensed under the MIT License


https://github.com/Sy-edUzair
