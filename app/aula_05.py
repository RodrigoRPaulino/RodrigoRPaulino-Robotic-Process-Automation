"""Consultar valor do dolar em site """
import pyautogui as pg
import time as delay

iniciar = pg.position(34,1056)
pg.moveTo(iniciar)
delay.sleep(5)
pg.click()

chrome = pg.typewrite("Google Chrome")
pg.press("enter")
delay.sleep(5) 

visitante = pg.position(x=596, y=838)
pg.moveTo(visitante)
delay.sleep(3)
pg.click()

delay.sleep(3)
pesquisa = pg.typewrite("Dolar")
pg.press("enter")
