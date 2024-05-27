#image into Black and White Image
import cv2 as cv
img=cv.imread("resources/image.jpg")
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh,b_w)=cv.threshold(grey,127,255,cv.THRESH_BINARY)

cv.imshow('Original',img)
cv.imshow('Grey',grey)
cv.imshow('Black and White',b_w)
cv.waitKey(0)
cv.destroyAllWindows()