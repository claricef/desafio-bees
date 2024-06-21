import random
from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cadastro_deposito_page import CadastroDepositoPage
# features/steps/cadastro_item_steps.py

def initialize_pages(context):
    if not hasattr(context, 'pageLogin'):
        context.pageLogin = LoginPage(context.browser)
    if not hasattr(context, 'pageHome'):
        context.pageHome = HomePage(context.browser)
    if not hasattr(context, 'pageCadastroDeposito'):
        context.pageCadastroDeposito = CadastroDepositoPage(context.browser)

@given('o usuario logado acesse a tela de cadastro de deposito')
def step_acessar_pagina_cadastro_deposito_com_usuario_logado(context):
    initialize_pages(context)
    context.pageLogin.acessar_pagina("/users/sign_in")
    context.pageLogin.preencher_login_usuario_cadastrado("namar21086@kernuo.com", "123456")
    context.pageHome.acessar_pagina("/deposits/new")

@when('o usuario informar nome, endereço, cidade,  estado e cep do deposito e clicar no botao create deposit')
def step_cadastrar_deposito(context):
    initialize_pages(context)
    nome = "Deposito" + str(random.randint(1, 1000))
    endereco = "Rua " + str(random.randint(1, 1000))
    cidade = "Barbalha"
    estado = "CE"
    cep = random.randint(1, 100)
    context.pageCadastroDeposito.cadastrar_deposito(nome, endereco, cidade, estado, cep)
