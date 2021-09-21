import pyautogui
import time
pyautogui.moveTo(160,750)
pyautogui.doubleClick()
pyautogui.moveTo(446,149)
time.sleep(9)
pyautogui.keyDown('win')
pyautogui.press('up')
pyautogui.keyUp('win')
time.sleep(5)
pyautogui.moveTo(150,50)
pyautogui.write('hfpevty kb z?', interval=0.50)
