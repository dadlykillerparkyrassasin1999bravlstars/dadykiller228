import pyautogui
import time
pyautogui.moveTo(476 , 742)
time.sleep(3)
pyautogui.hotkey('ctrl', 'a')
time.sleep(3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)
pyautogui.moveTo(1157 , 14)
pyautogui.click()
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.hotkey('enter')
