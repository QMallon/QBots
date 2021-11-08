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

sub = 'Block'
sub2 = 'Targeted Block:'
for line in textRay:
    if sub in line:
        ray2 = line.split()
        print('x y z: ' +ray2[1] + '/' + ray2[2]+ '/' + ray2[3])
        #print(line)
    if sub2 in line:
        ray2 = line.split()
        print('x y z: ' + ray2[8] + '/' + ray2[9] + '/' + ray2[10])
        #print(line)


#print(text)