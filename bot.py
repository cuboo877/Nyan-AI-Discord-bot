import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
from utils.config_loader import ConfigLoader

load_dotenv()
#--------------
ConfigLoader.load()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
token = os.getenv('discord-token')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

async def load_extensions():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            module_name = f"cogs.{filename[:-3]}"
            try:
                await bot.load_extension(module_name)
                print(f"✅ Loaded extension: {module_name}")
            except Exception as e:
                print(f"❌ Failed to load {module_name}: {e}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

asyncio.run(main())