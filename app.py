import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

permits = discord.Intents.default()
permits.message_content = True
bot = commands.Bot(command_prefix="!", intents=permits)

@bot.event
async def on_ready():
    print(f"Inicializado como {bot.user}")

bot.run(TOKEN)
