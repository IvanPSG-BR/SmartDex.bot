import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

permits = discord.Intents.default()
permits.message_content = permits.members = True
bot = commands.Bot(command_prefix="pk!", intents=permits)

@bot.event
async def on_ready():
    print(f"{bot.user} Online!")

bot.run(TOKEN)
