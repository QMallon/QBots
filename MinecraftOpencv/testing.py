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
def mineStaight():
    pydirectinput.leftClick()
    pydirectinput.moveRel(None, -400)
    time.sleep(.5)
    time.sleep(.5)
    pydirectinput.moveRel(None, 400)
    pydirectinput.leftClick()
    pydirectinput.press('w', 2)
    time.sleep(2.0)
def turn180():
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
    pydirectinput.moveRel(300, None)
def checkY(img):
    return(textExtract.)


wincap = WindowCapture('Minecraft 1.17.1 - Singleplayer')
torchcount = 0;
wcount = 0
while True:
    time.sleep(1.0)
    if checkY():


    torchcount +=1
    wcount +=1
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
        for x in range(wcount):
            pydirectinput.press('w', 2)
            time.sleep(.5)

        break


