import cv2 as cv
cap=cv.VideoCapture(0)
opened= cap.isOpened()
if(opened):
    while(cap.isOpened()):
        ret,frame=cap.read()
        if(ret==True):
            cv.imshow('MyVideo',frame)
            if(cv.waitKey(2)==27):
                break
#cv.waitKey(0)
cv.destroyAllWindows()