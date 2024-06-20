@deposito
Feature: Cadastro de deposito

  Scenario: Cadastrar um deposito
    Given o usuario logado acesse a tela de cadastro de deposito
    When o usuario informar nome "Deposito", endereço "Rua 15", cidade "Barbalha",  estado "CE" e cep "1234" do deposito e clicar no botao create deposit
    Then o usuario deve visualizar a mensagem "Deposit was successfully created." de sucesso no cadastro