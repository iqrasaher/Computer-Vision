#Splitting Videos into Frames
import cv2 as cv
cap = cv.VideoCapture('resources/Video.avi')
frameNo = 0
while(True):
    ret, frame =cap.read()
    if ret:
        cv.imwrite(f"resources/frames/frame_{frameNo}.jpg",frame)
    else:
        break
    frameNo = frameNo+2
cap.release()

    