import cv2 as cv
import numpy as np


img = cv.imread('Images\\Enemies\\fallenBodyBack.png', cv.IMREAD_UNCHANGED)
searchimg = cv.imread('Images\\cvtestImage2.png', cv.IMREAD_UNCHANGED)
result = cv.matchTemplate(searchimg, img, cv.TM_SQDIFF_NORMED)
#cv.imshow('Result', result)
#cv.waitKey()

threshold = .39
locations = np.where(result <= threshold)
locations = list(zip(*locations[::-1]))
print(locations)
if locations:
    print('Found needle.')

    img_w = img.shape[1]
    img_h = img.shape[0]
    rectangles = []
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), img_w, img_h]
        rectangles.append(rect)
        rectangles.append(rect)
        # Determine the box positions
       # top_left = loc
        #bottom_right = (top_left[0] + img_w, top_left[1] + img_h)
    rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
        # Draw the box
        #cv.rectangle(searchimg, top_left, bottom_right, line_color, line_type)

    cv.imshow('Matches', searchimg)
    cv.waitKey()
    #cv.imwrite('result.jpg', haystack_img)

else:
    print('Needle not found.')
