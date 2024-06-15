Feature: Acessar o sistema

  Scenario: Usuário acessa a página de login
    Given que o usuário acessa o navegador
    When o usuário navega pela url do sistema
    Then o usuário deve ser redirecionado para a página de login