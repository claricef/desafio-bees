Feature: Cadastro de usuário

  Scenario: Cadastrar usuário com dados válidos
    Given o usuario acesse a pagina de cadastro
    When o usuario informar o email "namar21086@kernuo.com" valido e a senha "123456" com no minimo 6 caracteres
    and o usuario clicar no botao sign up
    Then o usuario deve visualizar a mensagem "Welcome to your storage" de boas vindas na pagina inicial

