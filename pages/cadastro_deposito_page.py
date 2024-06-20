from selenium.webdriver.common.by import By
from .base_page import BasePage

class CadastroDepositoPage(BasePage):
    INPUT_NOME_DEPOSITO = (By.ID, "deposit_name")
    INPUT_ENDERECO_DEPOSITO = (By.ID, "deposit_address")
    INPUT_CIDADE_DEPOSITO = (By.ID, "deposit_city")
    INPUT_ESTADO_DEPOSITO = (By.ID, "deposit_state")
    INPUT_CEP_DEPOSITO = (By.ID, "deposit_zipcode")
    BUTTON_CREATE_DEPOSITY = (By.NAME, "commit")

    def cadastrar_deposito(self, nome, endereco, cidade, estado, cep):
       self.escrever_campo(self.INPUT_NOME_DEPOSITO, nome)
       self.escrever_campo(self.INPUT_ENDERECO_DEPOSITO, endereco)
       self.escrever_campo(self.INPUT_CIDADE_DEPOSITO, cidade)
       self.escrever_campo(self.INPUT_ESTADO_DEPOSITO, estado)
       self.escrever_campo(self.INPUT_CEP_DEPOSITO, cep)
       self.clicar_elemento(self.BUTTON_CREATE_DEPOSITY)