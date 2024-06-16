from behave import given, when, then
from pages.cadastro_usuario_page import CadastroUsuarioPage
from pages.home_page import HomePage

@given('o usuario acesse a pagina de cadastro')
def step_acessar_pagina_cadastro(context):
    pageCadastro = CadastroUsuarioPage(context.browser)
    pageCadastro.acessar_pagina("/users/sign_up")
    context.pageCadastro = pageCadastro

@when('o usuario informar o email "{email}" valido, a senha "{senha}", confirmar a senha novamente')
def step_preencher_campos_cadastro(context, email, senha):
    context.pageCadastro.preencher_dados_cadastro(email, senha)

@when('o usuario clicar no botao sign up')
def step_clicar_finalizar_cadastro(context):
    context.pageCadastro.finalizar_cadastro()

@then('o usuario deve visualizar a mensagem "{mensagem}" de boas vindas na pagina inicial')
def step_verificar_mensagem_boas_vindas(context, mensagem):
    pageHome = HomePage(context.browser)
    context.pageHome = pageHome
    texto_capturado = context.pageHome.buscar_mensagem_boas_vindas()
    assert mensagem in texto_capturado, f"Esperado '{mensagem}', mas encontrado '{texto_capturado}'"
