import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class VisualizacaoItemPage(BasePage):
    LABEL_CADASTRO_SUCESSO = (By.XPATH, "/html/body/div/p")
    NOME_ITEM = (By.XPATH, "/html/body/div/div[1]/p[1]")
    ALTURA_ITEM = (By.XPATH, "/html/body/div/div[1]/p[2]")
    LARGURA_ITEM = (By.XPATH, "/html/body/div/div[1]/p[3]")
    PESO_ITEM = (By.XPATH, "/html/body/div/div[1]/p[4]")
    BUTTON_DESTROY_ITEM = (By.XPATH, "/html/body/div/div[2]/form/button")

    def visualizar_dados_item(self):
        self.encontrar_elemento(self.NOME_ITEM)
        self.encontrar_elemento(self.ALTURA_ITEM)
        self.encontrar_elemento(self.LARGURA_ITEM)
        self.encontrar_elemento(self.PESO_ITEM)
    
    def buscar_mensagem_cadastro_sucesso(self):
        return self.capturar_texto_elemento(self.LABEL_CADASTRO_SUCESSO)
    
    def excluir_item(self):
        self.clicar_elemento(self.BUTTON_DESTROY_ITEM)
    
    
    