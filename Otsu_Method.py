import cv2 as cv
import numpy as np
 # read an image 
img = cv.imread('resources/image.jpg',0)
img = cv.resize(img, (320,225))
 # cv.threshold function is used to apply thresholds and save data in th6
otsu_thresh,th6 =cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
 # display the images
cv.imshow('Image Dislay', th6)
cv.waitKey(0)
cv.destroyAllWindows()