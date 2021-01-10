import pyautogui
import time
import random

time.sleep(6)
spam_text = "aqui va lo que quieres decir"

for _ in range(50): #amb while true no pararia.
    pyautogui.typewrite(spam_text)
    pyautogui.press('enter')
    time.sleep(1)
