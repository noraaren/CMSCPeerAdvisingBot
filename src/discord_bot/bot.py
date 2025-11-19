import os
import sys
from pathlib import Path

# Add parent directory to path so we can import from services
sys.path.insert(0, str(Path(__file__).parent.parent))

import discord
from services import googleCalendarService, googleAuth
from commands import last_two_weeks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    print(" successfully connected")

@client.event
async def on_message(message: discord.Message):
    # don't reply to yourself
    if message.author == client.user:
        return

    if message.content.strip().lower() == "!last2weeks":
        await last_two_weeks.last_two_weeks(message)

client.run(TOKEN)

