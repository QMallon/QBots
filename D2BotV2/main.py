import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from Detection import Detection
from Vision import Vision
# from HsvFilter import HsvFilter
# from EdgeFilter import EdgeFilter
from bot import Bot
from bot import BotState

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# WindowCapture.list_window_names(WindowCapture)
# initialize the WindowCapture class
wincap = WindowCapture('Diablo II')
# needle
# vision_monster = Vision('fallenFiltered.png')
vision = Vision(None)
# cascade_monster = cv.CascadeClassifier('cascade/cascade.xml')
detector = Detection('cascade/cascade.xml')

bot = Bot((wincap.offset_x, wincap.offset_y), (wincap.w, wincap.h))
# hsv_filter = HsvFilter(0, 92, 0, 23, 255, 215, 255, 0, 0, 29)
loop_time = time()
# vision_monster.init_control_gui()


# Threads
wincap.start()
detector.start()
bot.start()

while (True):
    if wincap.screenshot is None:
        continue

    # get an updated image of the game
    # screenshot = wincap.get_screenshot()

    #
    detector.update(wincap.screenshot)

    # update the bot with the data it needs right now
    if bot.state == BotState.INITIALIZING:
        # while bot is waiting to start, go ahead and start giving it some targets to work
        # on right away when it does start
        targets = vision.get_click_points(detector.rectangles)
        bot.update_targets(targets)
    elif bot.state == BotState.SEARCHING:
        # when searching for something to click on next, the bot needs to know what the click
        # points are for the current detection results. it also needs an updated screenshot
        # to verify the hover tooltip once it has moved the mouse to that position
        targets = vision.get_click_points(detector.rectangles)
        bot.update_targets(targets)
        bot.update_screenshot(wincap.screenshot)
    elif bot.state == BotState.MOVING:
        # when moving, we need fresh screenshots to determine when we've stopped moving
        bot.update_screenshot(wincap.screenshot)
    elif bot.state == BotState.MINING:
        # nothing is needed while we wait for the mining to finish
        pass

    detection_image = vision.draw_rectangles(wincap.screenshot, detector.rectangles)
    # detection_image = vision.draw_crosshairs(wincap.screenshot, detector.rectangles)
    # display
    cv.imshow('Matches', detection_image)
    # cv.imshow('Feed', wincap.screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        detector.stop()
        wincap.stop()
        bot.stop()
        break
    elif cv.waitKey(1) == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
    elif cv.waitKey(1) == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

print('Done.')
