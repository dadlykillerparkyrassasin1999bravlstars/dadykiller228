import pyautogui
import time
number = input("Введите число от 1 до 8!")
pyautogui.moveTo(510 , 750)
time.sleep(3)
pyautogui.click()
time.sleep(3)
pyautogui.hotkey('ctrl', 'number')
