from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while pyautogui.locateCenterOnScreen('Images\\Locations\\bloodmoorMap.png', confidence=.6) is None:
    print('Currently in RogueEncampment')
    directory = os.listdir('Images\\Locations\\RogueEncampment')
    exits = []
    located = False
    exitLocated = ''
    for file in directory:
        if file.endswith('.png'):
            exits.append(file)
    for image in exits:
        found = pyautogui.locateCenterOnScreen('Images\\Locations\\RogueEncampment\\' + image, confidence=.6)
        if found is not None:
            print('Exit found' + image)
            x, y = found
            pyautogui.moveTo(x + 10, y + 10)
            time.sleep(.5)
            pyautogui.mouseDown(x + 10, y + 10)
            time.sleep(1)
            pyautogui.mouseUp()
            exitLocated = image
            break
        time.sleep(.5)
        click(100, 600)
        time.sleep(.5)
        click(400, 100)

    time.sleep(2)
    while located is False:
        xoffset = 0
        yoffset = 0
        found = pyautogui.locateCenterOnScreen('Images\\Locations\\RogueEncampment\\' + image, confidence=.6)
        if found is not None:
            x, y = found
            pyautogui.moveTo(x, y)
            time.sleep(.5)
            pyautogui.mouseDown(x, y)
            time.sleep(2)
            pyautogui.mouseUp()
        else:
            if image.__contains__('North'):
                click(400, 100)
                time.sleep(.5)
                click(100, 300)
                time.sleep(.5)
                xoffset = -10
                yoffset = -10
            if image.__contains__('South'):
                time.sleep(.5)
                click(400, 600)
                time.sleep(.5)
                click(400, 100)
                xoffset = 10
                yoffset = 10
                if pyautogui.locateCenterOnScreen('Images\\Locations\\RogueEncampment\\exitSouthBridgeEbd.png', confidence=.5) is not None:
                    image = 'exitSouthBridgeEbd.png'

            time.sleep(2)
        if pyautogui.locateCenterOnScreen('Images\\Locations\\bloodmoorMap.png', confidence=.5) is not None:
            located = True

print('FoundBloodMoor')