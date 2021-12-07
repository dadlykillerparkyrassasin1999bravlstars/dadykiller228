import pyautogui
import time
comand   = input('Введите poisk tekst или voxod')
if comand == "poisk":
    pyautogui.moveTo(265 , 740)
    time.sleep(3)
    pyautogui.moveTo(280 , 47)
    time.sleep(3)
    pyautogui.click()
elif comand == "tekst":
        pyautogui.moveTo(1362 , 1)
        pyautogui.click(button = 'right')
        time.sleep(3)
        pyautogui.moveTo(1362 , 220)
        time.sleep(3)
        pyautogui.moveTo(840 , 377)
        time.sleep(3)
        pyautogui.click()
        time.sleep(3)
        pyautogui.press('enter')
elif comand == "voxod":
        pyautogui.moveTo(812 , 51)
        time.sleep(3)
    
