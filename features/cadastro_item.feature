@item
Feature: Cadastro de item

  Scenario: Cadastrar um item
    Given o usuario logado acesse a tela de cadastro de item
    When o usuario informar nome, altura, largura e peso do item e clicar no botao create item
    Then o usuario deve visualizar a mensagem "Item was successfully created." de sucesso no cadastro
