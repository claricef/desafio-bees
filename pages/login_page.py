from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
   
    INPUT_EMAIL = (By.ID, "user_email")
    INPUT_PASSWORD = (By.ID, "user_password")
    BUTTON_SUBMIT = (By.NAME, "commit")

    def preencher_login_usuario_cadastrado(self, email, senha):
       self.escrever_campo(self.INPUT_EMAIL, email)
       self.escrever_campo(self.INPUT_PASSWORD, senha)
    
    def acessar_sistema(self):
        self.clicar_elemento(self.BUTTON_SUBMIT)
