from dotenv import load_dotenv
import discord, os
from discord.ext import commands
from src.utils.classes import Super_bot

load_dotenv()
GUILD = os.getenv("GUILD_ID")

bot = Super_bot()
tests_server = discord.Object(id=int(GUILD))
