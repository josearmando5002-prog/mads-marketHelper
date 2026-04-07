MADS Supermercado

Biblioteca Python para gestão e análise de compras feitas por utilizadores em diferentes superfícies comerciais.
O módulo trabalha em memória e disponibiliza funções para:
* registo e listagem de utilizadores, lojas e compras;
* análise de evolução de preços de produtos com gráficos;
* consulta de estatísticas globais avançadas (volume financeiro, tops de vendas);
* exportação seletiva ou integral para JSON.

### Instalação

No PyPI:

```bash
pip install mads-marketHelper
```

### Importação

```python
from mads_grupo2_dev import *
```

Também é possível importar funções específicas:
```python
from mads_grupo2_dev import add_user, add_loja, add_compra, listar_dados
```

### Estrutura de dados (em memória)

O módulo mantém quatro estruturas globais principais:
* `utilizadores` (dict)
* `categoriasLojas` (list) - *Contém: Padaria, Talho, Peixaria, Supermercado*
* `lojas` (dict)
* `compras` (dict)

Isto significa que os dados existem apenas durante a execução do programa. Para persistir a informação, usa a função de exportação.

### Fluxo recomendado

1. Registar lojas com `add_loja`.
2. Registar utilizadores com `add_user`.
3. Registar as transações com `add_compra`.
4. Consultar dados através de `listar_dados`, analisar tendências com `gerar_grafico_evolucao` e verificar os totais com `consultar_estatisticas`.
5. Exportar os dados no fim da sessão com `exportar_para_json`.

---

## API Principal

### Registos

`add_user(nome: str, nif: str, data_nasc: str, sexo: str)`

Regista um utilizador.
* **Parâmetros:**
  * `nome`: texto (apenas letras e espaços).
  * `nif`: texto numérico com exatamente 9 dígitos (deve ser único).
  * `data_nasc`: formato DD-MM-YYYY (não pode ser data futura).
  * `sexo`: 'M', 'F' ou 'O'.
* **Saída:** Imprime lista de erros de validação ou mensagem de sucesso.

`add_loja(nome: str, especialidade: str, localizacao: str)`

Regista uma loja (gera um ID automaticamente).
* **Parâmetros:**
  * `nome`: texto (pode conter números e '&').
  * `especialidade`: deve ser uma das opções em `categoriasLojas` (Padaria, Talho, Peixaria, Supermercado).
  * `localizacao`: texto (apenas letras e hífens).
* **Saída:** Imprime lista de erros ou mensagem de sucesso com o ID da loja.

`add_compra(produto: str, preco: float, id_loja: int, data_compra: str, nif_utilizador: str, tipo_pagam: str = "")`

Regista uma compra associada a um utilizador e a uma loja.
* **Parâmetros:**
  * `produto`: texto (nome do produto comprado).
  * `preco`: valor numérico estritamente superior a 0.
  * `id_loja`: número inteiro (a loja tem de estar registada).
  * `data_compra`: formato DD-MM-YYYY (não pode ser no futuro).
  * `nif_utilizador`: NIF de um utilizador já registado.
  * `tipo_pagam` *(Opcional)*: 'N' (Numerário) ou 'M' (Multibanco).
* **Saída:** Imprime erros de validação ou sucesso indicando o ID da compra gerado.

---

### Listagens

As funções de listagem imprimem os dados no terminal de forma formatada e permitem filtragem dinâmica:

`listar_dados(entidade: str, ordem: str = "asc", filtro_tipo: str = "", filtro_valor: str = "")`

* **Entidades válidas:** "utilizadores", "lojas", "compras".
* **Ordem:** "asc" (crescente) ou "desc" (decrescente).
* **Filtros disponíveis por entidade:**
  * Utilizadores: `sexo`
  * Lojas: `especialidade`
  * Compras: `produto`, `loja`, `pagamento`, `com_pagamento_registado`, `nif`

---

### Estatísticas e Gráficos

`consultar_estatisticas()`

Imprime um painel global com métricas agregadas:
* Totais de utilizadores, lojas e compras registadas.
* Loja com mais transações e produto mais vendido.
* Cliente com mais compras e cliente que mais gastou.
* Volume total transacionado na plataforma.

`gerar_grafico_evolucao(produto: str, data_inicio: str = "", data_fim: str = "")`

Gera e apresenta um gráfico de linha (via Matplotlib) mostrando a evolução do preço de um produto específico.
* Calcula automaticamente a variação de preço (subida, descida ou manutenção).
* Permite limitar o espetro temporal usando `data_inicio` e `data_fim` (DD-MM-YYYY).

---

### Exportação

`exportar_para_json(nome_ficheiro: str = "dados_plataforma.json", entidade: str = "tudo", filtro_tipo: str = "", filtro_valor: str = "")`

Exporta os dados em memória para um ficheiro `.json`.
* **Cenários:**
  * `entidade="tudo"`: Exporta utilizadores, lojas, categorias e compras integralmente.
  * `entidade="compras"`: Permite exportar apenas o dicionário de compras, sendo possível aplicar os mesmos filtros do método de listagem (ex: apenas compras feitas em "multibanco").

---

### Exemplo completo

```python
from mads_grupo2_dev import *

# 1. Registar Utilizadores e Lojas
add_user("João Martins", "123456789", "15-05-1990", "M")
add_loja("Talho Central", "Talho", "Maia")
add_loja("Padaria Pão Quente", "Padaria", "Porto")

# 2. Registar Compras
add_compra("Frango", 3.50, 1, "01-03-2026", "123456789", "N")
add_compra("Frango", 3.80, 1, "10-03-2026", "123456789", "M")
add_compra("Pão de Forma", 1.20, 2, "22-03-2026", "123456789", "N")

# 3. Listar e Analisar
listar_dados("compras", ordem="desc", filtro_tipo="produto", filtro_valor="frango")
consultar_estatisticas()
gerar_grafico_evolucao("Frango")

# 4. Exportar Dados
exportar_para_json("backup_projeto.json")
```
