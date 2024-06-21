# Desafio BEES

- Para executar os testes desse projeto é necessário ter o Python instalado e o driver do Selenium adequado para o seu browser

## Instalação

### Clone o repositório:

  `git clone https://github.com/claricef/desafio-bees.git`
  
  `cd desafio-bees`

### Instale as dependências necessárias:

  `pip install -r requirements.txt`

Para executar os testes foram adicionadas tags as features para permitir selecionar qual delas executar sem necessidade de executar todas, dentro do arquivo .feature na primeira linha existe a tag é definida da seguinte forma @nomeTag

### Exemplo de como executar testes por tag:

  `behave -t @deposito`

### Para executar todos:

  `behave`

## Estrutura dos Arquivos

### features/nome_arquivo.feature:
  - Arquivo que define os cenários de teste em Gherkin.

### features/steps/nome_arquivo.py:
 - Arquivo que contém a implementação dos passos definidos nos cenários de teste.

### features/pages/nome_pagina.py:
  - Arquivo que encapsula a interação com a página do sistema sob teste.
  - O arquivo base_page.py é uma classe base para todas as páginas. Contém métodos comuns para interação com elementos da página, como clicar, escrever e capturar texto de elementos.
py.

### features/steps/environment.py:
  - Arquivo que define as configurações do ambiente de teste. Este arquivo é útil para configurar e limpar o estado do teste antes e depois de cada execução de cenário, garantindo que o ambiente esteja pronto para cada teste.

### ./requirements.txt:
  - Arquivo que contém as dependências necessárias para executar o projeto


