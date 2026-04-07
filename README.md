Biblioteca Python para gestão e análise de compras feitas por utilizadores em diferentes superfícies comerciais.
Este módulo opera diretamente em memória e oferece as seguintes funcionalidades:
* registo e listagem de utilizadores, lojas e compras;
* análise de evolução de preços de produtos com gráficos;
* consulta de estatísticas globais avançadas (volume financeiro, tops de vendas);
* exportação seletiva ou integral para JSON.

### Instalação

No PyPI:
```bash
pip install mads-marketHelper
```
*(Nota: A biblioteca `matplotlib` é estritamente necessária para a geração de gráficos).*

### Importação

```python
from mads_grupo2_dev import *
```
Também podes carregar métodos específicos:
```python
from mads_grupo2_dev import add_user, add_loja, add_compra, listar_dados
```

### Estrutura de dados (em memória)

O sistema suporta-se em quatro bases de dados globais. Isto implica que toda a informação é volátil e só existe enquanto o script corre. Para guardares o progresso, recorre à ferramenta de exportação.

* `utilizadores` (dict): Guarda a informação dos clientes.
* `categoriasLojas` (list): Inclui estritamente: *Padaria, Talho, Peixaria, Supermercado*.
* `lojas` (dict): Regista os espaços comerciais.
* `compras` (dict): Armazena o histórico de transações.

### Fluxo recomendado

1. Adicionar os estabelecimentos via `add_loja`.
2. Inscrever os clientes com `add_user`.
3. Gravar as faturas usando `add_compra`.
4. Analisar a informação usando `listar_dados`, estudar o mercado com `gerar_grafico_evolucao` e extrair totais através de `consultar_estatisticas`.
5. Exportar o progresso no final da sessão com `exportar_para_json`.

---

## API Principal

### Registos

#### `add_user(nome, nif, data_nasc, sexo)`
Inscreve um novo cliente no sistema.
* **Parâmetros:**
  * `nome` (**Obrigatório**): string. Apenas letras e espaços permitidos.
  * `nif` (**Obrigatório**): string. Valor numérico de 9 algarismos exatos (tem de ser inédito).
  * `data_nasc` (**Obrigatório**): string. Padrão DD-MM-YYYY (datas no futuro são bloqueadas e a idade calculada tem de ser > 0).
  * `sexo` (**Obrigatório**): string. Restrito a 'M', 'F' ou 'O'.
* **Saída:** Apresenta no ecrã os erros encontrados ou a mensagem de confirmação.

#### `add_loja(nome, especialidade, localizacao)`
Insere um novo estabelecimento comercial (o ID é gerado sequencialmente).
* **Parâmetros:**
  * `nome` (**Obrigatório**): string. Aceita letras, algarismos, espaços e '&'.
  * `especialidade` (**Obrigatório**): string. Obriga a uma das escolhas da lista `categoriasLojas` (formatação automática da capitalização).
  * `localizacao` (**Obrigatório**): string. Só letras, espaços e hífens validados.
* **Nota:** O sistema bloqueia a criação se já existir uma loja com o mesmo nome na mesma localização.
* **Saída:** Mostra o registo de erros ou a confirmação de sucesso com o ID gerado.

#### `add_compra(produto, preco, id_loja, data_compra, nif_utilizador, tipo_pagam="")`
Vincula um artigo a um cliente e a um ponto de venda.
* **Parâmetros:**
  * `produto` (**Obrigatório**): string. Apenas letras, algarismos, espaços e hífens. O sistema guarda o texto em minúsculas (`.lower()`).
  * `preco` (**Obrigatório**): int ou float. Valor numérico estritamente superior a zero.
  * `id_loja` (**Obrigatório**): inteiro. O ID do estabelecimento tem de existir no sistema.
  * `data_compra` (**Obrigatório**): string. Padrão DD-MM-YYYY (sem datas futuras).
  * `nif_utilizador` (**Obrigatório**): string. NIF pertencente a um cliente já inscrito.
  * `tipo_pagam` (*Opcional*): string. 'N' para Numerário ou 'M' para Multibanco (por omissão fica "Não especificado").
* **Saída:** Alerta para eventuais falhas de validação ou emite o comprovativo com o ID da fatura.

---

### Listagens

As ferramentas de listagem mostram a informação na consola de forma estruturada e suportam pesquisas dinâmicas:
`listar_dados(entidade: str, ordem: str = "asc", filtro_tipo: str = "", filtro_valor: str = "")`

* **Parâmetros:**
  * `entidade` (**Obrigatório**): "utilizadores", "lojas" ou "compras".
  * `ordem` (*Opcional*): "asc" (a subir) ou "desc" (a descer).
  * `filtro_tipo` (*Opcional*): Define o campo a pesquisar. Filtros disponíveis:
    * **Utilizadores:** `sexo`
    * **Lojas:** `especialidade`
    * **Compras:** `produto`, `loja`, `pagamento`, `com_pagamento_registado`, `nif`
  * `filtro_valor` (*Opcional*): O valor de pesquisa correspondente ao `filtro_tipo` aplicado.

---

### Estatísticas e Gráficos

#### `consultar_estatisticas()`
Mostra um quadro-resumo com indicadores agregados da plataforma:
* Contagem absoluta de clientes, estabelecimentos e faturas.
* Ponto de venda com mais atividade e o artigo mais popular.
* Cliente com maior frequência e o que movimentou mais capital.
* Dinheiro total transacionado no sistema.

#### `gerar_grafico_evolucao(produto, data_inicio="", data_fim="")`
Cria e exibe um gráfico de linhas (usando o Matplotlib) que espelha o histórico de valores de um artigo. Apura de forma automática a percentagem de inflação, deflação ou manutenção do valor.
* **Parâmetros:**
  * `produto` (**Obrigatório**): string. Nome do artigo a analisar (não pode estar vazio).
  * `data_inicio` (*Opcional*): string. Limite temporal inferior (DD-MM-YYYY).
  * `data_fim` (*Opcional*): string. Limite temporal superior (DD-MM-YYYY e não pode ser anterior à data de início).

---

### Exportação

`exportar_para_json(nome_ficheiro="dados_plataforma.json", entidade="tudo", filtro_tipo="", filtro_valor="")`
Transfere a informação da memória para um documento local em `.json`.

* **Parâmetros:**
  * `nome_ficheiro` (*Opcional*): string. O nome tem de terminar em `.json`. O valor por omissão é `"dados_plataforma.json"`.
  * `entidade` (*Opcional*): `"tudo"` (guarda a totalidade do sistema) ou `"compras"` (extrai estritamente a listagem de faturas).
  * `filtro_tipo` (*Opcional*): Em conjunto com `entidade="compras"`, aplica os mesmos filtros do método de listagem.
  * `filtro_valor` (*Opcional*): O valor de pesquisa para o `filtro_tipo` selecionado.

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
