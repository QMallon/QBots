import CharCreate
import Combat
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
while not completed:
    Combat.combat(True)











