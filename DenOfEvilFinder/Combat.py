from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def combat(inCombat):
    while inCombat:
        inCombat = checkincombat()
        # pyautogui.keyDown('shift')
        # pyautogui.rightClick
        time.sleep(2)
    # pyautogui.keyUp('shift')


def checkincombat():
    enemylist = []
    enemyFound = True
    directory = os.listdir('Images\\Enemies')
    for file in directory:
        if file.endswith('.png'):
            enemylist.append(file)

    while enemyFound:
        count = 0
        for image in enemylist:
            found = pyautogui.locateCenterOnScreen('Images\\Enemies\\'+image, confidence=0.6)
            if found is not None:
                print('found an enemy' + image.title())
                count += 1

        if count == 0:
            print('No Enemies Found')
            enemyFound = False;
