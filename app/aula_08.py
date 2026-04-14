from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

data_frame_lista: list[list[str]] = []

driver.get("https://rpachallengeocr.azurewebsites.net/")

# tabela
tabela = driver.find_element(By.XPATH, '//*[@id="tableSandbox"]')
linhas = tabela.find_elements(By.TAG_NAME, "tr")

for linha_atual in linhas:
    colunas = linha_atual.find_elements(By.TAG_NAME, "td")
    valores = [coluna.text for coluna in colunas]

    if valores:  # evita linha vazia (header)
        print(valores)
        data_frame_lista.append(valores)

# cria dataframe
df = pd.DataFrame(data_frame_lista)

# salva direto
df.to_excel("dadosSite.xlsx", index=False) # type: ignore

input("Finalizado - pressione ENTER para fechar")
driver.quit()