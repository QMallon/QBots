from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def followRoad():
    while True:
        # print('Currently in RogueEncampment')
        directory = os.listdir('Images\\Locations\\BloodMoor')
        exits = []
        count = 0
        prevx = 0

        previmage = ''
        located = False
        exitLocated = ''
        print('lookingForRoad')
        for file in directory:
            if file.endswith('.png'):
                exits.append(file)
        for image in exits:
            found = pyautogui.locateCenterOnScreen('Images\\Locations\\BloodMoor\\' + image, grayscale=False,
                                                   confidence=0.5)
            if found is not None:
                print('Road found' + image)
                print(found)
                x, y = found
                if prevx:
                    pyautogui.mouseDown(x, y)
                    time.sleep(3)
                    pyautogui.mouseUp()
                    previmage = image
                else:
                    print('backwards?')

                count += 1
                if count > 4:
                    break

        time.sleep(2)
