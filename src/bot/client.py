from dotenv import load_dotenv
import discord, os
from discord.ext import commands

load_dotenv()
GUILD = os.getenv("GUILD_ID")

permits = discord.Intents.all()
permits.message_content = permits.members = permits.guilds = True
bot = commands.Bot(command_prefix="pk!", intents=permits)
tests_server = discord.Object(id=int(GUILD))
