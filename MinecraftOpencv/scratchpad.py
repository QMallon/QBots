import cv2 as cv
import keyboard
import numpy as np
import os
import time
from textExtract import textExtract

textGetter = textExtract()
for line in textGetter.findXYZ('testImage2.jpg'):
    print(line)
