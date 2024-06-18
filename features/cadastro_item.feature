@item
Feature: Cadastro de item

  Scenario: Cadastrar um item
    Given o usuario logado acesse a tela de cadastro de item
    When o usuario informar nome "Notebook", altura "45", largura "30" e peso "2500" do item e clicar no botao create item
    Then o usuario deve visualizar a mensagem "Item was successfully created." de sucesso no cadastro
