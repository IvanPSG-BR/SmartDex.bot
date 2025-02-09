import discord
from discord import app_commands
from ..utils import helpers

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

@app_commands.command(name="about", description="Apresentação do bot")
async def about(interact:discord.Interaction):
    main_embed = helpers.create_embed(
            title="Sobre mim",
            desc=f"Olá {interact.user.name}, sou um bot criado **por** um pokefan **para** pokefans! Meu intuito é te ajudar em sua jornada, ou em suas batalhas competitivas\nPor que não tenta algum comando?",
            color=discord.Color.dark_blue(),
            author_name="BENTE_VII",
            author_link="https://github.com/IvanPSG-BR",
            thumb="attachment://pikachu_face.PNG",
        )
    
    view = discord.ui.View()
    pikachu_face_img = discord.File("images/pikachu_face.PNG", "pikachu_face.PNG")
    for name, embed in categories.items():
        btn = discord.ui.Button(label=name)
        async def callback(interact:discord.Interaction, emb=embed):
            await interact.response.send_message(embed=emb, ephemeral=True)
        btn.callback = callback
        view.add_item(btn)
    
    try:   
        await interact.response.send_message(file=pikachu_face_img, embed=main_embed, view=view)
    except Exception as e:
        print(f"Erro no retorno da interação: {e}")



@app_commands.command(name="commands_list", description="Exibe comandos do bot")
@app_commands.describe(commands_category="Categoria dos Comandos")
@app_commands.choices(commands_category=[
    app_commands.Choice(name=option, value=choice_options.index(option)) for option in choice_options
])
async def commands_list(interact:discord.Interaction, commands_category:app_commands.Choice[int]):
    response_msg = None
    cvalue_list = list(categories.values())
    
    try:
        for option in choice_options:
            if commands_category.value == choice_options.index(option):
                response_msg = interact.response.send_message(embed=cvalue_list[choice_options.index(option)], ephemeral=True)
                break
                
        await response_msg

    except Exception as e:
        print(f"Erro no retorno da interação: {e}")
        