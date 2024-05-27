#import library
import cv2 as cv
#create instance of Video Capture
cap=cv.VideoCapture(0)
#To check either Camera is Open or not.
opened =cap.isOpened()
'''if camera is Opened then we use while Loop till cap isopened.
then we click Image from Camera'''
#ret return Boolean
#vidoe is always a set of frames

'''Continuous Looping:it will show contiuous
frames till user press
press a key check after 2 miliseconds,
Escpe Character Value is 27,the, it will break the loop'''
if(opened):
    while(cap.isOpened()):
        ret,frame =cap.read()
        if(ret==True):
            cv.imshow("My Video",frame)
            if(cv.waitKey(2)==27):
                break



    

    