import cv2
import random

#in opencv we have images with bgr so bgr means blue green and red

"""
[0,0,0]
[blue,green,red]
"""

#when we rotate to image, arrays values also rotated. So you can modify image with just modify to the array.

img = cv2.imread('deneme.png',1)

"""
print(img.shape) #show how many row(height of image), width of image and channels 
#channel is color space of our image

print(img[0])#show the your arrays first row pixels
"""



"""
#### CHANGE SHAPE WITH RANDOM COLOR, SO WITH IT YOU CAN MANUPLATE IMAGE COLOR ### 
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)] # random.randint(low,high) genereates a random number between low and high value. 
"""



copy = img[50:100, 100:150] #copy to this range of row and columns pixels to the cut variable
img[100:150, 50:100] = copy #paste copied pixels range to the image (with my sample image it is not clear chane it my image with other images)




cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()