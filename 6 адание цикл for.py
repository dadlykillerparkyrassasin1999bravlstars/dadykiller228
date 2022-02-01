import pyautogui
import time
n = int(input('Введите количество текстовыхдокумето в хотитесоздать   '))
for step in range(n):
    pyautogui.moveTo(1360, 0)
    pyautogui.click(button = 'right')
    time.sleep(2)
    pyautogui.moveTo(1347, 177)
    time.sleep(2)
    pyautogui.moveTo(1034, 313)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.press('1')
    time.sleep(2)
    pyautogui.click()
    