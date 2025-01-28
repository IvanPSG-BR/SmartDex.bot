import discord
from discord.ext import commands

@commands.command(name="about")
async def about(ctx:commands.Context):
    pikachu_face_img = discord.File("images/pikachu_face.PNG", "pikachu_face.PNG")
    embed = discord.Embed(
        title="Sobre mim",
        description=f"Olá {ctx.author.display_name}, sou um bot criado **por** um pokefan **para** pokefans! Meu intuito é te ajudar em sua jornada, ou em suas batalhas competitivas\nPor que não tenta algum comando?.",
        color=discord.Color.orange()
    )
    
    embed.add_field(name="📖 Pokedex:",
                    value="""`pk!ability [nome]`: descreve a habilidade;\n
                    `pk!compare [pokemon1] [pokemon2]`: compara 2 pokémon;\n
                    `pk!egg [grupo]`: mostra pokémon pertencentes a esse egg group;\n
                    `pk!evolve [pokemon]`: métodos de evolução do pokémon;\n
                    `pk!pokemon [nome]`: dados gerais do pokémon;\n
                    `pk!move [nome]`: descrição do movimento;\n
                    `pk!moves [pokemon] --tipo [tipo]`: movimentos que o pokémon aprende;\n
                    `pk!nature [nome]`: detalha o efeito da nature;\n
                    `pk!stats [pokemon]`: valores de atributos base do pokémon;\n
                    `pk!typechart [tipo]`: forças/fraquezas do tipo.""",
                    inline=True
                    )
    embed.add_field(name="🔍 Busca:",
                    value="""`pk!weaks [pokemon]`: diz as fraquezas/resistências do pokémon;\n
                    `pk!filter --tipo [tipo] --regiao [regiao]`: busca por filtros.""",
                    inline=True
                    )
    embed.add_field(
                    name="⚔️ Showdown:",
                    value="""`pk!team [pokemon] [formato]`: gera time competitivo;\n
                    `pk!counter [pokemon]`: responde com melhores counters;\n
                    `pk!build [formato]`: ajuda a construir time;\n
                    `pk!strategy [pokemon] [situacao]`: sugere estratégias;\n
                    `pk!usage [formato]`: pokémon mais usados no formato;\n
                    `pk!analise [situacao]`: analisa batalha do Showdown.""",
                    inline=True
                    )
    embed.add_field(
                    name="🕹️ Official Games:",
                    value="""`pk!locations [pokemon]`: lista de onde encontrar o pokémon;\n
                    `pk!location [nome]`: informações sobre a localização;\n
                    `pk!itens [nome]`: detalhes sobre o item;\n 
                    `pk!version [jogo]`: informações sobe a versão do jogo.
                    """
                    )
    embed.add_field(
                    name="ℹ️ Outros:",
                    value="""`pk!about`: comandos do bot;\n
                    `pk!quiz`: quiz de Pokémon;\n
                    `pk!funfact`: curiosidades sobre Pokémon;\n
                    `pk!music [jogo]`: toca a trilha sonora do jogo;\n
                    `pk!daily`: pokémon do dia.""",
                    inline=True
                    )
    
    embed.set_footer(text="\nTunado pela IA DexterAI")
    embed.set_thumbnail(url="attachment://pikachu_face.PNG")
    embed.set_author(name="BENTE_VII", url="https://github.com/IvanPSG-BR")
    
    await ctx.reply(file=pikachu_face_img, embed=embed)
