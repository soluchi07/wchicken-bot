# Discord Quotes Bot 🤖✨

**Technologies:** Python, Discord.py, JSON, dotenv, OOP, Async Programming, Discloud Deployment

A fully-featured Discord bot deployed on **Discloud**, designed to engage server members with dynamic quotes, interactive responses, and real-time message tracking. Built with scalability, maintainability, and asynchronous programming best practices in mind.

## Features

* **Interactive Message Responses:**
  Contextually responds to keywords like `"wagwan"` and `"crazy"` with witty, personalized messages.
* **Random Quote Command:**
  `/get_quote` delivers a random quote stored in a JSON file (quotes.json), demonstrating dynamic data handling.
* **Message Edit Notifications:**
  Tracks and logs edits to messages, notifying users of changes while preserving context.
* **Guild-Specific Command Syncing:**
  Uses Discord’s app commands synced to a specific server for precise command management.

## Technical Highlights

* **Object-Oriented Design:** Custom `Client` class extending `discord.Bot` encapsulates server-specific functionality.
* **Asynchronous Programming:** Efficiently handles real-time Discord events with `async/await`.
* **Environment Variable Management:** Uses `.env` for secure storage of bot tokens and server IDs.
* **JSON Data Handling:** Allows easy expansion of quotes without modifying code.
* **Deployment on Discloud:**

  * Fully hosted on Discloud for 24/7 uptime.
  * Auto-restarts with every crash for reliability.
  * Configured with Python 3.11 for modern, stable runtime.
  * Custom avatar and bot name integrated for branding.

## Discloud Configuration

```ini
# https://docs.discloudbot.com/discloud.config
ID=<your_discloud_id>
MAIN=wchicken-quote.py
NAME=wchickens quotes
AUTORESTART=true
AVATAR=<your_avatar_url>
PYTHON_VERSION=3.11
```

## Usage

1. Clone the repository:

   ```bash
   git clone <repo-url>
   cd discord-quotes-bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add a `.env` file with your bot credentials:

   ```
   BOT_ID=<your_bot_token>
   SERVER_ID=<your_guild_id>
   ```

4. Run locally (optional):

   ```bash
   python wchicken-quote.py
   ```

> **Note:** The bot is fully deployed on **Discloud**, ensuring continuous uptime and seamless Discord integration.