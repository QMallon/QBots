from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
found = False
located = False
stuckCount = 0
while located != True:
    if(found !=True):
        if pyautogui.locateOnScreen('DenOfEvilMiniMap.png', confidence=0.6) != None:
            print("I can see it")
            found = True
            time.sleep(0.5)
        else:
            print("I am unable to see it")
            found = False
            #   click(400,100)
            #click(100,300)

            time.sleep(1.0)
    else:

        while found == True:

            if pyautogui.locateOnScreen('DenOfEvil2.png', confidence=0.6) != None:
                print("I arrived")
                located = True
                break
                time.sleep(0.5)
            else:
                print("I have not arrived yet")
                location = pyautogui.locateCenterOnScreen('DenOfEvilMiniMap.png', confidence=0.6)

                print(location)
                if location.__str__() == "None":

                    stuckCount += 1
                    if stuckCount>=3:
                        print('I am Stuck')
                        click(400, 100)
                        time.sleep(.5)
                        click(100,300)
                        time.sleep(.5)
                        click(400, 100)
                        time.sleep(.5)
                        click(100, 600)
                       # x, y = pyautogui.locateCenterOnScreen('DenOfEvilMiniMap.png')
                        location = pyautogui.locateCenterOnScreen('DenOfEvilMiniMap.png', confidence=0.6)
                        if location.__str__() == "None":
                            print('I am Stuck')
                            click(400, 100)
                            time.sleep(.5)
                            click(100, 300)
                            time.sleep(.5)
                            click(400, 100)
                            time.sleep(.5)
                            click(100, 600)
                        else:
                            stuckCount = 0



                else:
                    x, y = pyautogui.locateCenterOnScreen('DenOfEvilMiniMap.png', confidence=0.6)
                    pyautogui.click(x, y+10)
                    prevLocation = location


                time.sleep(1.0)
