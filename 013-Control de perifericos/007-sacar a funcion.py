import pyautogui

def irclick(x,y):
    pyautogui.sleep(1)
    pyautogui.moveTo(x,y)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(1)

def escribir(texto):
    pyautogui.sleep(1)
    pyautogui.typewrite(texto, interval=0.1)
    pyautogui.sleep(1)


irclick(472,194)
irclick(502,522)
irclick(821,393)
escribir("esto es un texto")


