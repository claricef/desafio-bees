import random
from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cadastro_item_page import CadastroItemPage
from pages.visualizacao_item_page import VisualizacaoItemPage

def initialize_pages(context):
    if not hasattr(context, 'pageLogin'):
        context.pageLogin = LoginPage(context.browser)
    if not hasattr(context, 'pageHome'):
        context.pageHome = HomePage(context.browser)
    if not hasattr(context, 'pageCadastroItem'):
        context.pageCadastroItem = CadastroItemPage(context.browser)
    if not hasattr(context, 'pageVisualizacaoItem'):
        context.pageVisualizacaoItem = VisualizacaoItemPage(context.browser)

@given('o usuario logado acesse a tela de cadastro de item')
def step_acessar_pagina_cadastro_item_com_usuario_logado(context):
    initialize_pages(context)
    context.pageLogin.acessar_pagina("/users/sign_in")
    context.pageLogin.preencher_login_usuario_cadastrado("namar21086@kernuo.com", "123456")
    context.pageHome.acessar_pagina("/items/new")

@when('o usuario informar nome, altura, largura e peso do item e clicar no botao create item')
def step_cadastrar_item(context):
    initialize_pages(context)
    nome = "Item" + str(random.randint(1, 1000))
    altura = random.randint(1, 100)
    largura = random.randint(1, 100)
    peso = random.randint(1, 5000)
    context.pageCadastroItem.cadastrar_item(nome, altura, largura, peso)

@then('o usuario deve visualizar a mensagem "{mensagem}" de sucesso no cadastro')
def step_verificar_item_cadastrado(context, mensagem):
    initialize_pages(context)
    texto_capturado = context.pageVisualizacaoItem.buscar_mensagem_cadastro_sucesso()
    assert mensagem in texto_capturado, f"Esperado '{mensagem}', mas encontrado '{texto_capturado}'"
