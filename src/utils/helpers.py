import discord
from discord.ext import commands
from discord import app_commands

def create_embed(title:str, desc:str, color:discord.Color, author_name="", author_link="", thumb="", footer="Tunado pela DexterAI"):
    embed = discord.Embed(title=title, description=desc, color=color)
    embed.set_author(name=author_name, url=author_link)
    embed.set_thumbnail(url=thumb)
    embed.set_footer(text=footer)
    
    return embed


async def normalized_text(text:str):
    await text.strip().lower()
