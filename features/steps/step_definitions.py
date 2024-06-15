from behave import given, when, then
from selenium.webdriver.common.by import By

@given('que o usuário acessa o navegador')
def step_usuario_acessa_navegador(context):
    pass
    
@when('o usuário navega pela url do sistema')
def step_usuario_acessa_url_sistema(context):
    context.browser.get('https://test-bees.herokuapp.com/')

@then('o usuário deve ser redirecionado para a página de login')
def step_usuario_redirecionado_pagina_login(context):
    h2_element = context.browser.find_element(By.TAG_NAME, 'h2')
    assert 'Login' in h2_element.text, f"Esperado 'Login', mas encontrado '{h2_element.text}'"