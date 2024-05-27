import cv2 as cv
import numpy as np
img = cv.imread("images/cat.jpg")
font=cv.FONT_ITALIC
#puttext(img,text,start_coor,font,font-size,color,thickness,linetype(line format))
img=cv.putText(img,'Hello World',(60,150),font,4,(220,0,213),5,cv.LINE_AA)
img=cv.resize(img,(500,500))
cv.imshow("images",img)
cv.waitKey(0)
cv.destroyAllWindows()