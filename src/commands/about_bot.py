import discord
from discord import app_commands
from src.utils import helpers, classes
from src.bot.client import bot
from time import sleep
first_command = True

choice_options = ["pokedex", "search", "showdown", "official_games", "miscellaneous"]

pokedex_embed = helpers.create_embed(
    title="📖 Pokedex:",
    desc="""`/ability [nome]`: descreve a habilidade;\n
    `/compare [pokemon1] [pokemon2]`: compara 2 pokémon;\n
    `/egg [grupo]`: mostra pokémon pertencentes a esse egg group;\n
    `/evolve [pokemon]`: métodos de evolução do pokémon;\n
    `/move [nome]`: descrição do movimento;\n
    `/moves [pokemon] --tipo [tipo]`: movimentos que o pokémon aprende;\n
    `/nature [nome]`: detalha o efeito da nature;\n
    `/pokemon [nome]`: dados gerais do pokémon;\n
    `/stats [pokemon]`: valores de atributos base do pokémon;\n
    `/typechart [tipo]`: forças/fraquezas do tipo.""",
    color=discord.Color.orange()
)
search_embed = helpers.create_embed(
        title="🔍 Busca:",
        desc="""`/filter --tipo [tipo] --regiao [regiao]`: busca por filtros;\n
        `/random --tipo [tipo] --regiao [regiao]`: retorna os dados de um pokémon aleatório;\n
        `/weaks [pokemon]`: diz as fraquezas/resistências do pokémon.""",
        color=discord.Color.green()
    )
showdown_embed = helpers.create_embed(
        title="⚔️ Showdown:",
        desc="""`/analise [situacao]`: analisa a situação de batalha e sugere o que pode acontecer;\n
        `/build [formato]`: monta um time com builds para o formato;\n
        `/counter [pokemon]`: responde com melhores counters;\n
        `/strategy [pokemon] [situacao]`: sugere a estratégia ideal para a situação;\n
        `/team [pokemon] [formato]`: dá dicas para encaixar o Pokémon em um time competitivo;\n
        `/usage [formato]`: pokémon mais usados no formato.""",
        color=discord.Color.red()
    )
ofcgames_embed = helpers.create_embed(
        title="🕹️ Jogos Oficiais",
        desc="""`/itens [nome]`: detalhes sobre o item;\n 
        `/location [nome]`: informações sobre a localização;\n
        `/locations [pokemon]`: lista de onde encontrar o pokémon;\n
        `/version [jogo]`: informações sobe a versão do jogo.""",
        color=discord.Color.gold()
    )
misc_embed = helpers.create_embed(
        title="ℹ️ Outros:",
        desc="""`/about`: comandos do bot;\n
        `/daily`: pokémon do dia;\n
        `/funfact`: curiosidades sobre Pokémon;\n
        `/music [jogo]`: toca a trilha sonora do jogo;\n
        `/quiz`: quiz de Pokémon.""",
        color=discord.Color.teal()
    )

categories = {"Pokedex": pokedex_embed, "Busca": search_embed, "Showdown": showdown_embed, "Jogos Oficiais": ofcgames_embed, "Outros": misc_embed}

async def about(interact:discord.Interaction):
    main_embed = helpers.create_embed(
            title="Sobre mim",
            desc=f"Olá {interact.user.name}, prazer em te conhecer! sou a {bot.user.name}, uma PokeAssistente criada **por** um fã **para** fãs! Meu objetivo é te ajudar em sua jornada, ou em suas batalhas competitivas\n\nPor que não tenta algum comando?",
            color=discord.Color.dark_blue(),
            author_name="BENTE_VII",
            author_link="https://github.com/IvanPSG-BR",
            thumb="attachment://pikachu_face.PNG",
        )
    
    view = classes.Persistent_view(categories)
    pikachu_face_img = discord.File("media/pikachu_face.PNG", "pikachu_face.PNG")
    about_smartdex_audio = discord.File("media/about_smartdex.mp3", "Sobre mim.mp3")
    
    try:   
        await interact.followup.send(embed=main_embed, files=[pikachu_face_img, about_smartdex_audio], view=view)
    except Exception as e:
        print(f"Erro no retorno da interação do Painel \"Sobre\": {e}")

@app_commands.command(name="commands_list", description="Exibe comandos do bot")
@app_commands.describe(commands_category="Categoria dos Comandos")
@app_commands.choices(commands_category=[
    app_commands.Choice(name=option, value=choice_options.index(option)) for option in choice_options
])
async def commands_list(interact:discord.Interaction, commands_category:app_commands.Choice[int]):
    global first_command
    cvalue_list = list(categories.values())
    
    try:
        for option in choice_options:
            if commands_category.value == choice_options.index(option):
                if first_command:
                    await interact.response.defer(thinking=True)
                    first_command = False
                    sleep(1.5)
                    await interact.followup.send(embed=cvalue_list[choice_options.index(option)], ephemeral=True)
                else:
                    await interact.response.send_message(embed=cvalue_list[choice_options.index(option)], ephemeral=True)
                
                break

    except Exception as e:
        print(f"Erro no retorno da interação do comando commands_list: {e}")
        