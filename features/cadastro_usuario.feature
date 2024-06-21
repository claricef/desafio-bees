@usuario
Feature: Cadastro de usuário

  Scenario: Cadastrar usuário com dados válidos
    Given o usuario acesse a pagina de cadastro
    When o usuario informar o email, a senha, confirmar a senha novamente
    and o usuario clicar no botao sign up
    Then o usuario deve visualizar a mensagem "Welcome to your storage" de boas vindas na pagina inicial

