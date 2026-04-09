import pyautogui as pg
import time as delay
import pygetwindow as getWindow

opcao = pg.confirm('Selecione a opção desejada', buttons = ['Excel','Word','Notepad']) # type: ignore

if opcao == "Excel":
    pg.hotkey("win","r")
    delay.sleep(2)

    pg.typewrite("Excel")
    delay.sleep(3)

    pg.press("enter")
    delay.sleep(3)

    pg.position(227,207)
    pg.press("enter")

    #seleciona a janela ativa para fechar 
    encerrar = getWindow.getActiveWindow()
    delay.sleep(3)

    encerrar.close() # type: ignore
    delay.sleep(3)


    print("Executando Excel")

elif opcao == "Word":
    pg.hotkey("win","r")
    delay.sleep(2)

    pg.typewrite("winword")    
    delay.sleep(3)

    pg.press("enter")
    delay.sleep(3)

    pg.position(415,411)
    pg.press("enter")

    #seleciona a janela ativa para fechar 
    encerrar = getWindow.getActiveWindow()
    delay.sleep(3)

    encerrar.close() # type: ignore
    delay.sleep(3)

    print("Executando Word")

else:
    pg.hotkey("win","r")
    delay.sleep(2)

    pg.typewrite("Notepad")    
    delay.sleep(3)

    pg.press("enter")
    delay.sleep(10)

    pg.press("enter")

    #seleciona a janela ativa para fechar 
    encerrar = getWindow.getActiveWindow()
    delay.sleep(3)

    encerrar.close() # type: ignore
    delay.sleep(3)
   
    print("Executando Notepad")
