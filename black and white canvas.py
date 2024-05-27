#how to draw line and shapes in Python
import cv2 as cv
import numpy as np 

#draw a Black Canvas
img =np.zeros((600,600))#height,width
#draw a White Canvas
img1 =np.ones((600,600))#height,width
cv.imshow("Black Canvas",img)
cv.imshow("White Canvas",img1)
print("The Size of our canvas1 is:",img.shape)
print("The Size of our canvas2 is:",img1.shape)
cv.waitKey(0)
cv.destroyAllWindows()