import random
from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cadastro_inventario_page import CadastroInventarioPage
from pages.cadastro_item_page import CadastroItemPage
from pages.cadastro_deposito_page import CadastroDepositoPage
# features/steps/cadastro_item_steps.py

def initialize_pages(context):
    if not hasattr(context, 'pageLogin'):
        context.pageLogin = LoginPage(context.browser)
    if not hasattr(context, 'pageHome'):
        context.pageHome = HomePage(context.browser)
    if not hasattr(context, 'pageCadastroInventario'):
        context.pageCadastroInventario = CadastroInventarioPage(context.browser)
    if not hasattr(context, 'pageCadastroItem'):
        context.pageCadastroItem = CadastroItemPage(context.browser)
    if not hasattr(context, 'pageCadastroDeposito'):
        context.pageCadastroDeposito = CadastroDepositoPage(context.browser)

# contador = 0
@given('o usuario esteja logado')
def step_acessar_pagina_cadastro_inventario_com_usuario_logado(context):
    initialize_pages(context)
    context.pageLogin.acessar_pagina("/users/sign_in")
    context.pageLogin.preencher_login_usuario_cadastrado("namar21086@kernuo.com", "123456")
   
@when('o usuario cadastrar o item e o deposito para criar o inventario')
def step_cadastrar_item_e_depositvo(context):
    initialize_pages(context)
    nomeItem = "Item 1" 
    altura = random.randint(1, 100)
    largura = random.randint(1, 100)
    peso = random.randint(1, 5000)
    context.pageHome.acessar_pagina("/items/new")
    context.pageCadastroItem.cadastrar_item(nomeItem, altura, largura, peso)
    nomeDeposito = 'Deposito 1'
    endereco = 'Teste'
    cidade = 'Teste'
    estado = 'TE' 
    cep = '123'
    context.pageHome.acessar_pagina("/deposits/new")
    context.pageCadastroDeposito.cadastrar_deposito(nomeDeposito, endereco, cidade, estado, cep)

@when('o usuario selecionar um item cadastrado, selecionar um deposito cadastrado, informar a quantidade e clicar no botao create inventory')
def step_cadastrar_inventario(context):
    initialize_pages(context)
    context.pageHome.acessar_pagina("/inventories/new")
    context.pageCadastroInventario.cadastrar_inventario('Item 1', 'Deposito 1', '10')

@when('o usuario selecionar o inventario, clicar na ação Show this inventory e após no botão Destroy this inventory')
def step_excluir_inventario_cadastrado(context):
    initialize_pages(context)
    context.pageHome.acessar_pagina("/inventories")
    context.pageCadastroInventario.excluir_inventario()

@then('o usuario deve visualizar a mensagem "{mensagem}"')
def step_visualizar_mensagem(context, mensagem):
    texto_capturado = context.pageCadastroInventario.buscar_mensagem_item_existente()
    assert mensagem in texto_capturado, f"Esperado '{mensagem}', mas encontrado '{texto_capturado}'"

@then('o usuario deve visualizar a mensagem "{mensagem}" de sucesso na exclusão')
def step_visualizar_mensagem_exclusao(context, mensagem):
    pass
