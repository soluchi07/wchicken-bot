import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import json
import random

# Load environment variables from .env file
load_dotenv()
bot_id = os.getenv('BOT_ID')
server_id = (os.getenv('SERVER_ID'))

if server_id is None or bot_id is None:
    raise ValueError("SERVER_ID environment variable is missing")

server_id = int(server_id)

print("Files in current directory:", os.listdir())
with open('quotes.json', 'r') as file:
    quotes = json.load(file)



# discord.client
class Client(commands.Bot):
    def __init__(self, server_id: int, **kwargs):
        super().__init__(**kwargs)
        self.server_id = server_id

    async def on_ready(self):
        print(f'logged on as {self.user}')
        
        try:
            guild = discord.Object(id=self.server_id)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'oop i guess it failed. look:\n{e}')

    async def on_message(self, message):
        if message.author == self.user:
            return
        print(f"Received message: {message.content} from {message.author} (ID: {message.id})")
        
        if 'wagwan' in message.content.lower():
            await message.channel.send(f'wagwan {message.author.mention}!')

        if "crazy" in message.content.lower():
            await message.channel.send(f'{message.author.mention}...Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. The rats make me crazy')

        if message.content.lower() == 'who' or message.content.lower() == 'who?':
            await message.channel.send('...asked')

        await self.process_commands(message)
    
    async def on_message_edit(self, before, after):
        print(f'{before.content} is now {after.content}')
        await before.channel.send(f'Hey I saw that! {before.author.mention} sent "{before.content}" and changed it to "{after.content}"')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True         # Required for message events
client = Client(command_prefix='!', server_id=server_id, intents=intents)

GUILD_ID = discord.Object(id=server_id)

@client.tree.command(name='get_quote',description='drops a random quote probably', guild=GUILD_ID) #name must be lowercase
async def getQuote(interaction: discord.Interaction):
    quote = quotes[random.randint(0, len(quotes))]
    await interaction.response.send_message(f'{quote["user"]} once said:\n{quote["quote"]}')


# client = Client(intents=intents)
client.run(bot_id)


