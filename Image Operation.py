import cv2 as cv
#image Read
img =cv.imread("images/cat.jpg")
#image Resize
img1 =cv.resize(img,(600,600))
#image Blur
blur_image=cv.blur(img1,(10,10))
#conversion
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Image Flip
flip_image =cv.flip(img1,1)
#image Display
cv.imshow("Image",img1)
cv.imshow("Blur Image",blur_image)
cv.imshow('Grey_Image',gray_img)
cv.imshow("Flip_Image",flip_image)
cv.waitKey(0)
cv.destroyAllWindows()