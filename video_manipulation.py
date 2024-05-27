#pip install opencv-contrib-python 
import cv2 as cv
cap=cv.VideoCapture(0)
cap.set(10,100)#10 is the key to set Brightness
cap.set(3,640)#3 is the key of width
cap.set(4,480)#4 is the key of height
opened= cap.isOpened()
#fourcc
#fourcc =cv.VideoWriter_fourcc(*'MJPG')
#fourcc =cv.VideoWriter_fourcc(*'VP80')/fourcc =cv.VideoWriter_fourcc(*'avc1')/fourcc =cv.VideoWriter_fourcc(*'H264')
fourcc =cv.VideoWriter_fourcc(*'XVID')
width=cap.get(cv.CAP_PROP_FRAME_WIDTH)
height =cap.get(cv.CAP_PROP_FRAME_HEIGHT)
fps =cap.get(cv.CAP_PROP_FPS)
#Video Writer mkv,avi,mp4
#out = cv.VideoWriter('iqra.avi',fourcc,fps,(int(height),int(width)))
out = cv.VideoWriter('iqraSaher.avi',fourcc,fps,(int(width),int(height)))
print(height)
#print("Frames are {}".format(fps))
if(opened):
    while(cap.isOpened()):
        ret,frame=cap.read()
        if(ret==True):
            cv.imshow('MyVideo',frame)
            out.write(frame)
            if(cv.waitKey(2)==27):
                break
out.release()
cap.release()
cv.destroyAllWindows()