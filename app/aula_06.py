'''Exemplo de automação executando e populando um bloco de notas '''

import pyautogui as pg
import pygetwindow as getWindow
import time as delay

delay.sleep(3)
executar = pg.hotkey("win","r")
delay.sleep(3)
comando = pg.typewrite("Notepad")
delay.sleep(3)
pg.press("enter")

delay.sleep(5)
pg.typewrite("Escrevendo o texto via codigo")

delay.sleep(3)

#seleciona a janela ativa para fechar 
encerrar = getWindow.getActiveWindow()
delay.sleep(3)


encerrar.close() # type: ignore
delay.sleep(3)

print("Automação encerrada com sucesso!")




