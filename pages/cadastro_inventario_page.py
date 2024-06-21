from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select

class CadastroInventarioPage(BasePage):
    SELECT_ITEM_INVENTARIO = (By.ID, "inventory_item_id")
    SELECT_DEPOSITO_INVENTARIO = (By.ID, "inventory_deposit_id")
    INPUT_QUANTIDADE_ITEM_INVENTARIO = (By.ID, "inventory_item_count")
    BUTTON_CREATE_INVENTORY = (By.NAME, "commit")
    LABEL_ITEM_EXISTENTE= (By.XPATH, '//*[@id="new_inventory"]/div[2]/div[1]/div')
    LABEL_SUCESSO = (By.XPATH, '/html/body/div/p')
    LINK_SHOW_INVENTORY = (By.XPATH, '//*[@id="inventories"]/table/tbody/tr/td[4]/a')
    BUTTON_DESTROY_INVENTORY = (By.XPATH, '/html/body/div/div[2]/form/button')
    LABEL_MENSAGEM_EXCLUSAO = (By.XPATH, "/html/body/div/p")

    def cadastrar_inventario(self, item, deposito, quantidade):
       self.selecionar_elemento(self.SELECT_ITEM_INVENTARIO, item)
       self.selecionar_elemento(self.SELECT_DEPOSITO_INVENTARIO, deposito)
       self.escrever_campo(self.INPUT_QUANTIDADE_ITEM_INVENTARIO, quantidade)
       self.clicar_elemento(self.BUTTON_CREATE_INVENTORY)
    
    def buscar_mensagem_item_existente(self):
        try:
            return self.capturar_texto_elemento(self.LABEL_SUCESSO)
        except:
            return self.capturar_texto_elemento(self.LABEL_ITEM_EXISTENTE)
    
    def excluir_inventario(self):
        self.clicar_elemento(self.LINK_SHOW_INVENTORY)
        self.clicar_elemento(self.BUTTON_DESTROY_INVENTORY)
    
    def buscar_mensagem_exclusao(self):
        return self.capturar_texto_elemento(self.LABEL_MENSAGEM_EXCLUSAO)
  
    