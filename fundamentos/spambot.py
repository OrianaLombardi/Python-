import pyautogui
import webbrowser as web 
from time import sleep

web.open("https://web.whatsapp.com/send?phone=+5491123560685")
sleep(10)
#nombre_Archivo=('C:\Users\Usuario\Desktop\cursos\phyton\fundamentos\ori.txt')


with open("Orki.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        