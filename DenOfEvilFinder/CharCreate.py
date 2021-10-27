from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def CreateChar(charName):
    print('Starting creation')
    x, y = pyautogui.locateCenterOnScreen('Images\\SinglerPlayer.png', confidence=0.6)
    pyautogui.click(x, y + 10)
    time.sleep(1.0)
    x, y = pyautogui.locateCenterOnScreen('Images\\CreateNewCharacter.png', confidence=0.6)
    pyautogui.click(x, y + 10)
    time.sleep(1.0)
    x, y = pyautogui.locateCenterOnScreen('Images\\Sorceress.png', confidence=0.6)
    pyautogui.click(x, y + 10)
    time.sleep(1.0)
    keyboard.write(charName)
    time.sleep(1.0)
    x, y = pyautogui.locateCenterOnScreen('Images\\OK.png', confidence=0.6)
    pyautogui.click(x, y + 10)
    time.sleep(1.0)

    print('Complete')
    return True


def NewName(charName):
    newname = input('Name taken please enter a new one')
    while newname == charName:
        newname = input('Name taken please enter a new one')
