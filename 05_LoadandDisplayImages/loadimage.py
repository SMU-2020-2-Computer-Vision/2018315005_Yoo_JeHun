import cv2
import os

cwd = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread('messi5.jpg')

ROI = img[286:332, 338:390]

cv2.imshow('Ball', ROI)
cv2.waitkey(0)

cv2.destroyAllWindows()