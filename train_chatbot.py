import pyautogui as pg
import time 


print ("Hola, gracias por llamarme")
time.sleep(1)
print ("A quien se lo desea mandar? ")
persona= input( )
time.sleep(1)
print ("Que mensaje desea mandar? ")
mensaje= input( )
time.sleep(2)
print ("Iniciando tarea... Porfavor no toques nada")

pg.hotkey("winleft")
pg.typewrite("WhatsApp",0.2)
pg.press("Enter")
time.sleep(3)
pg.typewrite( persona)
time.sleep(2)
pg.press("down")
pg.press("enter")
time.sleep(4)
pg.typewrite( mensaje)
pg.press("enter")

