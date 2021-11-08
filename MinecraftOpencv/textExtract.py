from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd= r'D:\PROGRAMSHERE\Tools\Tesseract\tesseract.exe'
im = np.array(Image.open('testImage2.jpg'))
text = pytesseract.image_to_string(im)
textRay = text.split('\n')
for line in textRay:
    x = 0
    print('Line ' + str(x) + ': ' + line)
    x += 1


#print(text)