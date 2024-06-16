from selenium.webdriver.common.by import By
from .base_page import BasePage

class CadastroUsuarioPage(BasePage):
    # Locators
    INPUT_EMAIL = (By.ID, "user_email")
    INPUT_PASSWORD = (By.ID, "user_password")
    INPUT_PASSWORD_CONFIRMATION = (By.ID, "user_password_confirmation")
    BUTTON_SIGNUP = (By.NAME, "commit")

    def preencher_dados_cadastro(self, email, senha):
       self.escrever_campo(self.INPUT_EMAIL, email)
       self.escrever_campo(self.INPUT_PASSWORD, senha)
       self.escrever_campo(self.INPUT_PASSWORD_CONFIRMATION, senha)
    
    def finalizar_cadastro(self):
        self.clicar_elemento(self.BUTTON_SIGNUP)

         