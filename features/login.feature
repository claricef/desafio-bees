Feature: Relizar login no sistema

  Scenario: Login no sistema com usuário válido
    Given o usuario acesse a pagina de login
    When o usuario informar o email "namar21086@kernuo.com" cadastrado e sua senha "123456"
    and o usuario clicar no botao submit
    Then o usuario deve visualizar a mensagem "Signed in successfully." na pagina inicial
