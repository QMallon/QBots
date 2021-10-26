import CharCreate
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

charCreated = False
charName = input('PLEASE ENTER A NAME:')

while not charCreated:
    charCreated = CharCreate.CreateChar(charName)











