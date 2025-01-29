# Criando uma API para um Modelo de IA e Integrando com um Bot do Discord

Este guia explica como criar uma API para um modelo de IA treinado no formato **.gguf** e usá-lo em um bot do Discord.

## 1. Instalar Dependências
Primeiro, instale as bibliotecas necessárias para criar a API:

```bash
pip install fastapi uvicorn discord.py llama-cpp-python requests
```

## 2. Estrutura do Projeto
Organize seu projeto da seguinte forma:

```
/meu-projeto/
│
├── bot_discord.py         # Código do bot do Discord
├── api.py                 # API que acessa o modelo de IA
└── modelo_ia.py           # Código que carrega e usa o modelo de IA
```

## 3. Criar a API (api.py)
Crie um servidor FastAPI para expor o modelo de IA:

```python
# api.py
from fastapi import FastAPI
from modelo_ia import carregar_modelo, gerar_resposta

app = FastAPI()

# Carregar o modelo
modelo = carregar_modelo("caminho/para/seu/modelo.gguf")

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

@app.post("/gerar_resposta/")
def obter_resposta(prompt: str):
    resposta = gerar_resposta(modelo, prompt)
    return {"resposta": resposta}
```

## 4. Criar Funções do Modelo (modelo_ia.py)

```python
# modelo_ia.py
from llama_cpp import Llama

def carregar_modelo(modelo_path: str):
    return Llama(model_path=modelo_path, n_threads=6, n_ctx=1536)

def gerar_resposta(modelo, prompt: str) -> str:
    resposta = modelo(prompt)
    return resposta
```

## 5. Rodar a API
Para iniciar a API, execute:

```bash
uvicorn api:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## 6. Criar o Bot do Discord (bot_discord.py)

```python
# bot_discord.py
import discord
import requests

TOKEN = "seu_token_aqui"
API_URL = "http://127.0.0.1:8000/gerar_resposta/"

client = discord.Client()

@client.event
async def on_ready():
    print(f'Bot {client.user} está online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!gerar'):
        prompt = message.content[len('!gerar '):]
        response = requests.post(API_URL, json={"prompt": prompt})
        data = response.json()

        await message.channel.send(data['resposta'])

client.run(TOKEN)
```

## 7. Testar o Bot
1. **Inicie a API**: `uvicorn api:app --reload`
2. **Inicie o bot do Discord**: `python bot_discord.py`
3. No Discord, envie: `!gerar Olá, IA!`
4. O bot responderá com o texto gerado pelo modelo de IA.

## 8. Considerações
- Para rodar o bot 24/7, use serviços como **AWS, Google Cloud ou Replit**.
- Para segurança, implemente autenticação na API.
- Para escalabilidade, considere usar **Docker**.

Esse setup cria uma API funcional para interagir com seu modelo de IA e um bot do Discord integrado. 🚀
