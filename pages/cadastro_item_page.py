from selenium.webdriver.common.by import By
from .base_page import BasePage

class CadastroItemPage(BasePage):
    INPUT_NOME_ITEM = (By.ID, "item_name")
    INPUT_ALTURA_ITEM = (By.ID, "item_height")
    INPUT_LARGURA_ITEM = (By.ID, "item_width")
    INPUT_PESO_ITEM = (By.ID, "item_weight")
    BUTTON_CREATE_ITEM = (By.NAME, "commit")

    def cadastrar_item(self, nome, altura, largura, peso):
       self.escrever_campo(self.INPUT_NOME_ITEM, nome)
       self.escrever_campo(self.INPUT_ALTURA_ITEM, altura)
       self.escrever_campo(self.INPUT_LARGURA_ITEM, largura)
       self.escrever_campo(self.INPUT_PESO_ITEM, peso)
       self.clicar_elemento(self.BUTTON_CREATE_ITEM)