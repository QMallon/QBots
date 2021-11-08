import cv2 as cv
import keyboard
import numpy as np
import os
import time

import pyautogui
import pydirectinput
from windowcapture import WindowCapture
from Detection import Detection
from Vision import Vision
# from HsvFilter import HsvFilter
# from EdgeFilter import EdgeFilter
from bot import Bot
from bot import BotState

def turn180():
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
torchcount = 0;
while True:
    time.sleep(1.0)
    #pydirectinput.mouseDown()
    pydirectinput.leftClick()
    pydirectinput.moveRel(None, -400)
    time.sleep(.5)
    #pydirectinput.mouseUp()
    #pydirectinput.keyDown('w')
    time.sleep(.5)
    #pydirectinput.keyUp('w')
    #pydirectinput.mouseUp()
    pydirectinput.moveRel(None, 400)
    pydirectinput.leftClick()
    pydirectinput.press('w', 2)
    time.sleep(2.0)
    torchcount +=1
    if torchcount>=3:
        pydirectinput.moveRel(600, None)
        pydirectinput.rightClick()
        pydirectinput.moveRel(-600, None)
        torchcount = 0

    #pydirectinput.moveRel(100, None)
    #pydirectinput.mouseDown()
    #pydirectinput.keyUp('w')


    if keyboard.is_pressed('u'):
        pydirectinput.mouseUp()
        turn180()

        break


