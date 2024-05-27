#Vidoe Read
import cv2 as cv
from numpy import True_
cap=cv.VideoCapture(0)
opened =cap.isOpened()
#if we want to check height or width,we use get attribute which extract all properties
height=cap.get(cv.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv.CAP_PROP_FPS)
print(height)
print(width)
if(opened):
    while(cap.isOpened()):
        ret,frame =cap.read()
        if(ret==True):
            cv.imshow("My Video",frame)
            if(cv.waitKey(2)==27):
                break
n