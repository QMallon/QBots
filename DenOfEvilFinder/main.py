import CharCreate
import Combat
import ExitTown
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

charCreated = False
completed = False
charName = input('PLEASE ENTER A NAME:')

while not charCreated:
    charCreated = CharCreate.CreateChar(charName)
time.sleep(1.0)
keyboard.press('tab')
time.sleep(1.0)
ExitTown.exittown()













