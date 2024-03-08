#pip install pyautogui
import pyautogui

anchura, altura = pyautogui.size()

pyautogui.moveTo(anchura/2,altura/2)

pyautogui.click()

pyautogui.typewrite("Hola que tal como estais", interval=0.1)
