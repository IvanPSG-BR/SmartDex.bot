import discord
from src.bot.client import bot
from src.commands import about_bot

last_msg_author_id = -1

async def command_sended(interaction:discord.Interaction):
    global last_msg_author_id
    
    try:
        if interaction.type == discord.InteractionType.application_command:
            if interaction.user.id != last_msg_author_id and about_bot.first_command:
                last_msg_author_id = interaction.user.id
                about_bot.first_command = False
                print("Painel \"Sobre\" enviado ao usuário!")
                await about_bot.about(interaction)
            else:
                print("Requisitos para enviar o painel \"Sobre\" não foram cumpridos")
        else:
            print("Interação não foi um slash command")
    except Exception as e:
        print(f"Erro ao enviar painel \"Sobre\": {e}")
