from behave import given, when, then
from pages.login_page import LoginPage
from pages.home_page import HomePage

@given('o usuario acesse a pagina de login')
def step_acessar_pagina_login(context):
    pageLogin = LoginPage(context.browser)
    pageLogin.acessar_pagina("/users/sign_in")
    context.pageLogin = pageLogin

@when('o usuario informar o email "{email}" cadastrado e sua senha "{senha}"')
def step_preencher_campos_login(context, email, senha):
    context.pageLogin.preencher_login_usuario_cadastrado(email, senha)

@when('o usuario clicar no botao submit')
def step_clicar_acessar_sistema(context):
    context.pageLogin.acessar_sistema()

@then('o usuario deve visualizar a mensagem "{mensagem}" na pagina inicial')
def step_verificar_mensagem_login_sucesso(context, mensagem):
    pageHome = HomePage(context.browser)
    context.pageHome = pageHome
    texto_capturado = context.pageHome.buscar_mensagem_login_sucesso()
    assert mensagem in texto_capturado, f"Esperado '{mensagem}', mas encontrado '{texto_capturado}'"
