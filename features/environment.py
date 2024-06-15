from selenium import webdriver

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()  # Inicializar o navegador antes de cada cenário

def after_scenario(context, scenario):
    context.browser.quit()  # Fechar o navegador após cada cenário
