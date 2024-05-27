import cv2 as cv
from cv2 import cvtColor
img=cv.imread("images/image.jpg")
img=cv.resize(img,(800,600))
grey_img=cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("1st Image",img)
cv.imshow("Flower",grey_img)

cv.waitKey(0)
cv.destroyAllWindows()