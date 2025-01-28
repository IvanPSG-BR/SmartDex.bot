# Tutorial SmartDex.bot

## Estrutura do Projeto
A estrutura recomendada para organizar o projeto é:

```
SmartDex.bot/
├── src/
│   ├── commands/
│   │   ├── pokedex.py      # Comandos relacionados à Pokédex
│   │   ├── showdown.py     # Comandos relacionados ao Pokémon Showdown
│   │   ├── ai.py           # Comandos que usam IA
│   │   └── misc.py         # Comandos diversos
├── .env                     # Variáveis de ambiente
├── .gitignore
└── app.py                  # Arquivo principal
```

## Organização dos Comandos

### 1. Comandos Básicos da Pokédex
- `!pokemon [nome]`: Informações básicas do Pokémon (stats, tipos, habilidades, etc)
- `!moves [pokemon] [--tipo tipo]`: Lista movimentos do Pokémon
- `!compare [pokemon1] [pokemon2]`: Compara dois Pokémon
- `!evolucao [pokemon]`: Mostra linha evolutiva

### 2. Comandos de Busca Avançada
- `!buscar --tipo [tipo] --regiao [regiao]`: Busca por características
- `!fraquezas [pokemon]`: Análise de fraquezas/resistências

### 3. Comandos Showdown
- `!team [pokemon] [formato]`: Gera time competitivo
- `!counter [pokemon]`: Lista melhores counters
- `!meta [formato]`: Análise do meta atual
- `!build [formato]`: Ajuda a construir time

### 4. Comandos com IA
- `!estrategia [pokemon] [situacao]`: Sugere estratégias
- `!analise [situacao]`: Analisa batalha do Showdown
- `!predict [pokemon] [movimento]`: Prevê próximos movimentos

### 5. Recursos Divertidos
- `!quiz`: Quiz de Pokémon
- `!daily`: Pokémon do dia
- `!random [--tipo tipo]`: Time aleatório

## Como Configurar Parâmetros nos Comandos

### 1. Parâmetro Simples
```python
@bot.command()
async def pokemon(ctx, nome):
    await ctx.send(f"Procurando {nome}...")
```

### 2. Múltiplos Parâmetros
```python
@bot.command()
async def compare(ctx, pokemon1, pokemon2):
    await ctx.send(f"Comparando {pokemon1} com {pokemon2}...")
```

### 3. Parâmetros Opcionais
```python
@bot.command()
async def moves(ctx, pokemon, tipo=None):
    if tipo:
        await ctx.send(f"Mostrando movimentos do tipo {tipo} do {pokemon}")
    else:
        await ctx.send(f"Mostrando todos os movimentos do {pokemon}")
```

### 4. Parâmetros com Flags
```python
@bot.command()
async def buscar(ctx, *, args):
    # Convertendo argumentos em dicionário
    params = {}
    current_key = None
    
    for arg in args.split():
        if arg.startswith('--'):
            current_key = arg[2:]
            params[current_key] = None
        elif current_key:
            params[current_key] = arg
            current_key = None
    
    await ctx.send(f"Buscando com parâmetros: {params}")
```

### 5. Resto do Texto como Um Parâmetro
```python
@bot.command()
async def estrategia(ctx, pokemon, *, situacao):
    await ctx.send(f"Analisando estratégia para {pokemon} na situação: {situacao}")
```

## Dicas de Organização
1. Mantenha o `app.py` simples, apenas com configurações básicas do bot
2. Coloque comandos em arquivos separados baseado em sua função:
   - `pokedex.py`: Comandos da Pokédex
   - `showdown.py`: Comandos do Showdown
   - `ai.py`: Comandos que usam IA
   - `misc.py`: Comandos diversos
3. Use funções auxiliares em arquivos separados quando precisar reutilizar código
4. Mantenha cada arquivo focado em uma responsabilidade específica

## Exemplo de app.py Básico
```python
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

permits = discord.Intents.default()
permits.message_content = permits.members = True
bot = commands.Bot(command_prefix="pk!", intents=permits)

@bot.event
async def on_ready():
    print(f"{bot.user} Online!")

bot.run(TOKEN)
```

# Tutorial: Treinando o Llama para o SmartDex

## Visão Geral
O SmartDex é um bot do Discord que usa o Llama 3.1 8b para fornecer análises competitivas de Pokémon. O bot é dividido em duas partes principais:
- Parte Pokédex: Dados estáticos da PokéAPI
- Parte Showdown: Análises competitivas usando Llama treinado com dados do Smogon

## Estrutura dos Dados de Treinamento

### 1. Coleta de Dados
Fontes principais:
- Análises do Smogon
- Dados do Pokémon Showdown
- Estatísticas de uso
- Replays de batalhas

### 2. Organização dos Dados
Os dados estão divididos em 4 categorias principais:

1. **Análises de Pokémon**
   - Sets competitivos
   - Movesets
   - EVs e Natures
   - Counters e checks

2. **Construção de Times**
   - Cores defensivos
   - Estilos de time
   - Sinergias
   - Weather teams

3. **Análise de Batalhas**
   - Situações comuns
   - Double switches
   - Late game
   - Matchups específicos

4. **Dicas de Meta**
   - Tiers do Showdown
   - Items importantes
   - Status moves
   - Speed control

### 3. Formato dos Dados
Cada entrada no dataset segue o formato:
```
{
    "instruction": "Pergunta ou comando do usuário",
    "input": "Contexto adicional (opcional)",
    "output": "Resposta detalhada baseada nos dados do Smogon"
}
```

## Processo de Fine-tuning

### 1. Preparação
- Converter dados para formato JSONL
- Dividir em treino/validação
- Definir parâmetros de treinamento

### 2. Treinamento
- Usar batches pequenos
- Monitorar overfitting
- Avaliar respostas periodicamente

### 3. Avaliação
Testar o modelo com:
- Perguntas sobre Pokémon específicos
- Análises de situações de batalha
- Dicas de construção de time
- Questões sobre o meta

## Próximos Passos

1. **Expansão do Dataset**
   - Adicionar mais exemplos
   - Cobrir mais situações
   - Incluir outros formatos

2. **Melhorias no Modelo**
   - Ajustar parâmetros
   - Testar diferentes prompts
   - Otimizar respostas

3. **Integração com o Bot**
   - Implementar chamadas ao modelo
   - Criar sistema de cache
   - Otimizar tempo de resposta

## Notas Importantes
- Manter consistência nas respostas
- Evitar informações incorretas
- Focar em dados competitivos relevantes
- Atualizar conforme o meta muda
