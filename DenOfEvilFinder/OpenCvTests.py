import cv2 as cv
import numpy as np


img = cv.imread('Images\\Enemies\\fallenBodyside.png', cv.IMREAD_UNCHANGED)
searchimg = cv.imread('Images\\cvTestimage.png', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(searchimg, img, cv.TM_CCOEFF_NORMED)
#cv.imshow('Result', result)
#cv.waitKey()

#get best match position
min_val, max_val,min_loc, max_loc = cv.minMaxLoc(result)
print('best Match pos' + str(max_loc))
print('best Match confidence' + str(max_val))
img_w = img.shape[1]
img_h = img.shape[0]


top_left= max_loc
bottom_right = (top_left[0] + img_w, top_left[1] + img_h)
cv.rectangle(searchimg, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

cv.imshow('Result', searchimg)
cv.waitKey()
