
# Tutorial de Integração de Dados para a IA de Pokémon

Este tutorial irá guiá-lo por todo o processo de unificação, integração e geração automática de perguntas e respostas a partir de diferentes fontes de dados. O objetivo é preparar um conjunto de dados unificado para ser usado na criação de uma IA que responda a comandos de Discord relacionados ao Pokémon Showdown.

## 1. Unificar a Estrutura dos Dados

### Problema
Seus arquivos vêm em formatos muito diferentes (JSON, CSV com diferentes delimitadores, texto com pipes, etc.).

### Solução
Escolha um formato “padrão” para representar cada registro, por exemplo, JSON com campos fixos. Isso irá garantir que todas as fontes de dados possam ser integradas de maneira eficiente.

Exemplo de esquema de dados para cada Pokémon ou situação:

```json
{
  "arquivo": "",       // Nome do arquivo ou formato
  "pokemon": "",       // Nome do Pokémon
  "lead": {},          // Dados extraídos do arquivo leads
  "metagame": {},      // Dados extraídos do arquivo metagame
  "moveset": {},       // Dados extraídos do arquivo moveset
  "usage": {}          // Dados extraídos do arquivo usage
}
```

Crie scripts para cada tipo de arquivo para normalizar os dados e convertê-los para essa estrutura. Aqui estão algumas sugestões:
- Para o **JSON de leads**: extraia os campos relevantes e limpe os dados.
- Para os arquivos **CSV** (metagame e usage): use bibliotecas como `pandas` para ler os dados e ajustar as colunas.
- Para os arquivos de **moveset**: identifique delimitadores e extraia os dados necessários.

### Dica
Comece com um arquivo de cada vez, como o arquivo de *leads*, e normalize os dados para um formato unificado. Depois, faça o mesmo para os outros arquivos.

---

## 2. Integrar os Dados

### Problema
Como juntar os dados de diferentes fontes?

### Solução
Identifique chaves comuns, como o nome do Pokémon ou o nome do arquivo (por exemplo, `gen1ou-2024-12...`), para unir as informações. 

Se você ainda não tem experiência com bancos de dados, use o **pandas** para fazer a integração entre os dados. Exemplo:

```python
import pandas as pd

# Supondo que você tenha DataFrames para leads e usage:
df_leads = pd.read_json('leads_normalizado.json')  # Exemplo
df_usage = pd.read_csv('usage_normalizado.csv')

# Se ambos tiverem uma coluna "Pokemon" já limpa:
df_integrado = pd.merge(df_leads, df_usage, on="Pokemon", how="outer")
```

Após a integração, exporte o resultado para um arquivo único (JSON ou CSV).

### Dica
Se você estiver confortável com planilhas e não deseja usar um banco de dados completo, o **pandas** pode servir como uma solução simples para o seu caso.

---

## 3. Gerar Automaticamente Exemplos de Perguntas e Respostas

### Problema
Criar manualmente centenas de exemplos de perguntas e respostas pode ser inviável.

### Solução
Crie templates para cada comando (por exemplo, `pk!usage [formato]`, `pk!counter [pokemon]`, etc.) e use os dados integrados para gerar perguntas e respostas automaticamente.

Exemplo de template para o comando `pk!usage [formato]`:

- **Instruction**:  
  `"Liste os pokémon mais usados no formato {formato}."`
  
- **Input**:  
  Se o registro integrado contém o campo `"usage"` e também o nome do formato (por exemplo, a partir do nome do arquivo), você pode montar um input como:
  ```txt
  Formato: gen1ou-2024-12
  Dados de usage:
  - Pokémon: Tauros, Usage: 79.63%
  - Pokémon: Snorlax, Usage: 74.10%
  ```
  
- **Output**:  
  O output esperado pode ser uma resposta como:  
  `"Os pokémon mais usados são Tauros, Snorlax, Chansey, ..."`.

Automatize a geração de exemplos com um script Python:

```python
def gerar_exemplo_usage(formato, df_usage):
    # Filtra os dados pelo formato
    df_filtrado = df_usage[df_usage['File'].str.contains(formato)]
    # Ordena pelo uso
    df_filtrado = df_filtrado.sort_values(by="Usage %", ascending=False)
    top_pokemon = df_filtrado.head(5)['Pokemon'].tolist()

    instruction = f"Liste os pokémon mais usados no formato {formato}."
    input_text = f"Dados de usage para {formato}: {df_filtrado.to_dict(orient='records')}"
    output = f"Os pokémon mais usados são: {', '.join(top_pokemon)}."
    return {"instruction": instruction, "input": input_text, "output": output}
```

Repita este processo para os outros comandos, como `pk!analise`, `pk!build`, `pk!counter`, `pk!strategy` e `pk!team`. Use as informações integradas para gerar as respostas.

### Dica
Comece com apenas um template e veja se os resultados fazem sentido. A partir disso, ajuste as regras de extração de informações e gere exemplos para os outros comandos.

---

## Conclusão

Resumindo, você deve seguir estes passos:

1. **Unificar os arquivos para um formato padrão** usando scripts.
2. **Integrar os dados** com ferramentas como `pandas`, utilizando chaves comuns.
3. **Gerar perguntas e respostas automaticamente** criando templates para cada comando e utilizando os dados integrados.

Com essa abordagem, você poderá automatizar grande parte do processo e gerar rapidamente o dataset para treinar a IA.

Se precisar de ajuda em qualquer etapa, estou à disposição!

