from dotenv import load_dotenv
import os, asyncio, uvicorn, logging
from src.commands import about_bot
from src.services import dexter_api
from src.bot import client

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

slash_related = client.bot.tree

@client.bot.event
async def on_ready():
    try:
        await slash_related.sync()
    except Exception as e:
        print(f"Erro ao sincronizar: {e}")
    
    print(f"{client.bot.user} Online!")

slash_related.add_command(about_bot.about)
slash_related.add_command(about_bot.commands_list)

async def start_api():
    config = uvicorn.Config(dexter_api.app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

async def start_bot():
    await client.bot.start(TOKEN)

async def main():
    await asyncio.gather(start_api(), start_bot())

if __name__ == "__main__":
    asyncio.run(main())
    logging.basicConfig(level=logging.INFO)
