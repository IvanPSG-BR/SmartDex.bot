import discord
from discord import app_commands

# Define o comando 'about' que será chamado quando o usuário digitar '!about'
@app_commands.command(name="about", description="Descrição e comandos do bot")
async def about(interact:discord.Interaction):
    # Cria um embed principal com informações sobre o bot
    main_embed = discord.Embed(
        title="Sobre mim",
        description=f"Olá {interact.user.name}, sou um bot criado **por** um pokefan **para** pokefans! Meu intuito é te ajudar em sua jornada, ou em suas batalhas competitivas\nPor que não tenta algum comando?",
        color=discord.Color.dark_blue()
    )
    # Cria um embed para a Pokedex com comandos relacionados
    pokedex_embed = discord.Embed(
        title="📖 Pokedex:",
        description="""`/ability [nome]`: descreve a habilidade;\n
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
    # Cria um embed para busca de pokémons
    search_embed = discord.Embed(
            title="🔍 Busca:",
            description="""`/filter --tipo [tipo] --regiao [regiao]`: busca por filtros;\n
            `/random --tipo [tipo] --regiao [regiao]`: retorna os dados de um pokémon aleatório;\n
            `/weaks [pokemon]`: diz as fraquezas/resistências do pokémon.""",
            color=discord.Color.green()
        )
    # Cria um embed para comandos de Showdown
    showdown_embed = discord.Embed(
            title="⚔️ Showdown:",
            description="""`/analise [situacao]`: analisa a situação de batalha e sugere o que pode acontecer;\n
            `/build [formato]`: monta um time com builds para o formato;\n
            `/counter [pokemon]`: responde com melhores counters;\n
            `/strategy [pokemon] [situacao]`: sugere a estratégia ideal para a situação;\n
            `/team [pokemon] [formato]`: dá dicas para encaixar o Pokémon em um time competitivo;\n
            `/usage [formato]`: pokémon mais usados no formato.""",
            color=discord.Color.red()
        )
    # Cria um embed para jogos oficiais
    ofcgames_embed = discord.Embed(
            title="🕹️ Jogos Oficiais",
            description="""`/itens [nome]`: detalhes sobre o item;\n 
            `/location [nome]`: informações sobre a localização;\n
            `/locations [pokemon]`: lista de onde encontrar o pokémon;\n
            `/version [jogo]`: informações sobe a versão do jogo.""",
            color=discord.Color.gold()
        )
    # Cria um embed para outros comandos
    misc_embed = discord.Embed(
            title="ℹ️ Outros:",
            description="""`/about`: comandos do bot;\n
            `/daily`: pokémon do dia;\n
            `/funfact`: curiosidades sobre Pokémon;\n
            `/music [jogo]`: toca a trilha sonora do jogo;\n
            `/quiz`: quiz de Pokémon.""",
            color=discord.Color.teal()
        )
    
    pikachu_face_img = discord.File("images/pikachu_face.PNG", "pikachu_face.PNG")
    main_embed.set_author(name="BENTE_VII", url="https://github.com/IvanPSG-BR")
    main_embed.set_thumbnail(url="attachment://pikachu_face.PNG")
    main_embed.set_footer(text="\nTunado pela IA DexterAI")
    
    # Cria uma view para os botões de categoria
    view = discord.ui.View()
    categories = {"Pokedex": pokedex_embed,
                  "Busca": search_embed,
                  "Showdown": showdown_embed,
                  "Jogos Oficiais": ofcgames_embed,
                  "Outros": misc_embed}
    
    # Adiciona botões para cada categoria e define suas callbacks
    for k, v in categories.items():
        btn = discord.ui.Button(label=k)
        async def callback(interact:discord.Interaction, emb=v):
            await interact.response.send_message(embed=emb, ephemeral=True)
        btn.callback = callback
        view.add_item(btn)
    
    # Responde ao usuário com a imagem e o embed principal
    await interact.response.send_message(file=pikachu_face_img, embed=main_embed, view=view)
    