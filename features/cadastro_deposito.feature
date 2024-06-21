@deposito
Feature: Cadastro de deposito

  Scenario: Cadastrar um deposito
    Given o usuario logado acesse a tela de cadastro de deposito
    When o usuario informar nome, endereço, cidade,  estado e cep do deposito e clicar no botao create deposit
    Then o usuario deve visualizar a mensagem "Deposit was successfully created." de sucesso no cadastro