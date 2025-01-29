from dotenv import load_dotenv
import os, asyncio, uvicorn
import discord
from discord.ext import commands
from src.commands import about_bot
from src.services import dexter_api

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

permits = discord.Intents.default()
permits.message_content = permits.members = True
bot = commands.Bot(command_prefix="pk!", intents=permits)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} Online!")


bot.tree.add_command(
    about_bot.about
)

async def start_api():
    config = uvicorn.Config(dexter_api.app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

async def start_bot():
    await bot.start(TOKEN)

async def main():
    await asyncio.gather(start_api(), start_bot())

if __name__ == "__main__":
    asyncio.run(main())
