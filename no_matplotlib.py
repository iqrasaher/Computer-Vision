import matplotlib.image as mpimg
import matplotlib.pylab as plt
#use imread function of matplotlib
img=mpimg.imread("images/text.jpg")
print(img.shape,img.dtype,type(img))
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("on")
plt.show()
#Change Intensity Value
#if value is less than 0.5, then Black otherwise no change
img1 = img
img1[img1 < 0.5] = 0
plt.imshow(img1)
plt.axis("off")
#you can save image using savefig
plt.savefig("images/text_dark.jpg")
plt.close()
img = mpimg.imread("images/text_dark.jpg")
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.show()

