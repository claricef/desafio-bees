@inventario
Feature: Cadastro de inventário

  Scenario: Cadastrar no inventario um item unico em um deposito  
    Given o usuario esteja logado
    when o usuario cadastrar o item e o deposito para criar o inventario
    and o usuario selecionar um item cadastrado, selecionar um deposito cadastrado, informar a quantidade e clicar no botao create inventory
    Then o usuario deve visualizar a mensagem "Inventory was successfully created." 

   Scenario: Verificar mensagem ao cadastrar item duplicado em um mesmo deposito
     Given o usuario esteja logado
     When o usuario selecionar um item cadastrado, selecionar um deposito cadastrado, informar a quantidade e clicar no botao create inventory
     Then o usuario deve visualizar a mensagem "Item has already been taken"
    
    Scenario: Excluir um inventario
      Given o usuario esteja logado
      When o usuario selecionar o inventario, clicar na ação Show this inventory e após no botão Destroy this inventory
      Then o usuario deve visualizar a mensagem "Inventory was successfully destroyed." de sucesso na exclusão