#import library
import cv2 as cv
#create instance of Video Capture
cap=cv.VideoCapture('resources/videoS.mp4')
#Properties of Video
#1.Total number of frames in Video
frames = cap.get(cv.CAP_PROP_FRAME_COUNT)
#2.Frames Per second of Video
fps =cap.get(cv.CAP_PROP_FPS)
#height and width of video
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
#Initialize output writer for Video
fourcc =cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('ReverseVideo.avi',fourcc,fps,(int(width),int(height)))
#we get the index of the last frame of Video File
frame_index = frames-1
#To check either Camera is Open or not.
if(cap.isOpened()):
    #reading till the end of video and we set the current frame position to last frame
    while(frame_index!=0):
        cap.set(cv.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame =cap.read()
        #resize the frame
        frame =cv.resize(frame,(int(width),int(height)))
        #writing the reversed video
        out.write(frame)
        #Decrementing frame index at each step
        frame_index = frame_index-1
        #printing the progress
        if(frame_index%100==0):
            print(frame_index)
out.release()
cap.release()
cv.destroyAllWindows() 