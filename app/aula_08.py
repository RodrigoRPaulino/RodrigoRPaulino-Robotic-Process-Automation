'''
Intalação do selenium e biblioteca do pandas para extração de dados de tabela usando o openpyxl
'''

from selenium import webdriver   
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://rpachallengeocr.azurewebsites.net/")

# tabela
tabela = driver.find_element(By.XPATH,'//*[@id="tableSandbox"]') 
linhas =  tabela.find_elements(By.TAG_NAME,"tr") 
coluna = tabela.find_elements(By.TAG_NAME,"td") 

linha = 1
#para
for linha_atual in linhas:
    print(linha_atual.text)
    linha = linha + 1



