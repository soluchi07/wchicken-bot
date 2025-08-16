# Discord Quotes Bot 🤖

**Technologies:** Python, Discord.py, JSON, dotenv, OOP, Async Programming

A fully-featured Discord bot built to engage server members with fun interactions, dynamic quotes, and responsive commands. Designed with modularity, scalability, and maintainability in mind—demonstrating proficiency in Python, asynchronous programming, and API integration.

## Features

* **Interactive Message Responses:**
  Responds contextually to keywords such as `"wagwan"` and `"crazy"`, enhancing user engagement with personalized messages.
* **Quote Command:**
  `/get_quote` returns a random inspirational or humorous quote stored in a JSON file (quotes.json), showcasing dynamic data handling.
* **Message Edit Tracking:**
  Monitors and logs edited messages, sending notifications that preserve conversational context.
* **Custom Command Syncing:**
  Uses Discord’s app commands with guild-specific syncing, demonstrating advanced bot management and API interaction.

## Technical Highlights

* Implemented **Object-Oriented Design** with a custom `Client` class to extend `discord.Bot`, encapsulating server-specific functionality.
* Utilized **asynchronous programming** with `async/await` to handle real-time events efficiently.
* Integrated **environment variable management** via `.env` for secure handling of API tokens and server IDs.
* Managed external data with **JSON parsing**, enabling easy expansion of quotes and messages without changing code.
* Applied **error handling** and logging for robust runtime performance and debugging.

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

3. Configure environment variables in a `.env` file:

   ```
   BOT_ID=<your_bot_token>
   SERVER_ID=<your_guild_id>
   ```

4. Run the bot:

   ```bash
   python wchicken-quote.py
   ```