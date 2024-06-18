from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-bees.herokuapp.com" 

    def acessar_pagina(self, url):
        self.driver.get(self.base_url + url)

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def clicar_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        element = self.encontrar_elemento(locator)
        element.click()

    def escrever_campo(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), "O elemento '{locator}' não foi encontrado na tela"

    def capturar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text
    
    def esperar_elemento_aparecer(self,locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return element
  
    