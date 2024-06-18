from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome()

def after_all(context):
    context.browser.quit()

def before_scenario(context, scenario):
    # Limpar cookies ou redefinir estado se necessário
    context.browser.delete_all_cookies()

def after_scenario(context, scenario):
    # Limpar após cada cenário se necessário
    pass