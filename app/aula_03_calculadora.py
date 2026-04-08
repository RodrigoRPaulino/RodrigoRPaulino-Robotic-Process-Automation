import pyautogui as pg
import time 

#move por coordenada
iniciar = pg.position(34,1056)
pg.moveTo(iniciar)

time.sleep(5)
pg.click()

time.sleep(2)
calc = pg.typewrite("Calculadora")

time.sleep(2)
calc = pg.position(110,336)
pg.click(calc)
#serve para pegar a posição  por coordenada
#print(pg.position())