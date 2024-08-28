import pyautogui
import pyscreeze

gu = 'gu.png'
while True:
    pyautogui.locateOnScreen('gu.png')
    if gu == pyautogui.locateOnScreen('gu.png'):
        print('ta na tela')
    else:
        print('nao ta na tela')