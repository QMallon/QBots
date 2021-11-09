from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pytesseract
from hsvfilter import HsvFilter

# a class that will create our pytesseract and do some of our text recognition needs also includes hsv filter function to clean text before analyzing it
class textExtract:
    pytes = None
    hsvFilter = None

    # constructor defaults to my path and a HSVFilter that I made that removes all noise WORKS WELL When Mining will not work in sunny sky
    def __init__(self, tesPath=r'D:\PROGRAMSHERE\Tools\Tesseract\tesseract.exe', hsvFilter = HsvFilter(0, 0, 210, 179, 255, 255, 0 ,255, 0, 0)):
        self.pytes = pytesseract
        self.pytes.pytesseract.tesseract_cmd= tesPath
        self.hsvFilter = hsvFilter


    # takes in img call filter on it then returns the xyz from the f3 menu of the block we are standing on
    # Not well organize or using any good practices
    def findXYZ(self, imgPath):
        im = None
        if imgPath is string:
            im = np.array(Image.open(imgPath))
            filteredImg = self.apply_hsv_filter(im)
        else:
            filteredImg = self.apply_hsv_filter(imgPath)

        text = self.pytes.image_to_string(filteredImg)
        textRay = text.split('\n')
        for line in textRay:
            x = 0
            #print('Line ' + str(x) + ': ' + line)
            x += 1

        sub = 'Block'
        sub2 = 'Targeted Block:'
        currentBlock = []
        for line in textRay:
            if sub in line:
                ray2 = line.split()
                # x/y/z
                #print('x y z: ' +ray2[1] + '/' + ray2[2]+ '/' + ray2[3])
                if sub2 in line:
                    continue
                else:

                    currentBlock.append(ray2[1].replace(',' , ''))
                    currentBlock.append(ray2[2].replace(',' , ''))
                    currentBlock.append(ray2[3].replace(',', ''))

                #print(line)
            if sub2 in line:
                ray2 = line.split()
                # x/y/z
                #print('x y z: ' + ray2[8] + '/' + ray2[9] + '/' + ray2[10])
                #print(line)

        return currentBlock

    ## barely modified version of LearnToCodeByGamings functions from vision class
    def apply_hsv_filter(self, original_image, hsv_filter=None):
        # convert image to HSV
        hsv = cv.cvtColor(original_image, cv.COLOR_BGR2HSV)

        # if we haven't been given a defined filter, use the filter values from the GUI
        if not hsv_filter:
            hsv_filter = self.hsvFilter

        # add/subtract saturation and value
        h, s, v = cv.split(hsv)
        s = self.shift_channel(s, hsv_filter.sAdd)
        s = self.shift_channel(s, -hsv_filter.sSub)
        v = self.shift_channel(v, hsv_filter.vAdd)
        v = self.shift_channel(v, -hsv_filter.vSub)
        hsv = cv.merge([h, s, v])

        # Set minimum and maximum HSV values to display
        lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
        upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])
        # Apply the thresholds
        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(hsv, hsv, mask=mask)

        # convert back to BGR for imshow() to display it properly
        img = cv.cvtColor(result, cv.COLOR_HSV2BGR)

        return img

        # apply adjustments to an HSV channel
        # https://stackoverflow.com/questions/49697363/shifting-hsv-pixel-values-in-python-using-numpy

    ## barely modified version of LearnToCodeByGamings functions from vision class
    def shift_channel(self, c, amount):
        if amount > 0:
            lim = 255 - amount
            c[c >= lim] = 255
            c[c < lim] += amount
        elif amount < 0:
            amount = -amount
            lim = amount
            c[c <= lim] = 0
            c[c > lim] -= amount
        return c

#print(text)