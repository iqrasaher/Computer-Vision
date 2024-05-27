#pip install numpy
#pip install scipy
#pip install scikit-image
#pip install scikit-learn
#pip install pillow
#pip install matplotlib

#Read,Save and Display Image using -->PIL
from PIL import Image
#1.read the Image
img = Image.open("images/cat.jpg")
#if you want to check the widtha and height of image
print(img.width,img.height,img.mode,img.format,type(img))
#2.Image Display
img.show()
#3.Convert RGB iage into GreyScale Image 
#save in same folder of Images
img_grey=img.convert("L")
img_grey.save("images/cat_grey.jpg")
#if you want to open the converted gray image again
Image.open("images/cat_grey.jpg").show()

