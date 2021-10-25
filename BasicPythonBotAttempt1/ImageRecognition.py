#This script locates the image stickman.png in the region we give it and tell you if it can see it
#FROM KIANBROSE
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('DenOfEvil2.png', confidence=0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)