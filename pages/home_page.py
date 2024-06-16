from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
   
    LABEL_WELCOME = (By.XPATH, "/html/body/div/h1")

    def buscar_mensagem_boas_vindas(self):
        return self.capturar_texto_elemento(self.LABEL_WELCOME)
