import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture

from vision import Vision
from hsvfilter import HsvFilter

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('Minecraft 1.17.1 - Singleplayer')
#wincap.list_window_names()
# initialize the Vision class
vision_limestone = Vision('stone.png')
# initialize the trackbar window
vision_limestone.init_control_gui()

# limestone HSV filter
#hsv_filter = HsvFilter(0, 0, 210, 179, 255, 255, 0, 255, 0, 0)
hsv_filter = HsvFilter(0, 0, 0, 13, 255, 255, 0, 33, 9, 0)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #screenshot =  '1636133666.3996527.jpg'

    # pre-process the image
    processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)

    # do object detection
    rectangles = vision_limestone.find(processed_image, 0.43)

    # draw the detection results onto the original image
    output_image = vision_limestone.draw_rectangles(screenshot, rectangles)



    # display the processed image
    cv.imshow('Processed', processed_image)
    #cv.imshow('Matches', output_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    elif cv.waitKey(1) == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), processed_image)
    elif cv.waitKey(1) == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), processed_image)

print('Done.')