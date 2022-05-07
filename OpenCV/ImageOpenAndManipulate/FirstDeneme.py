import cv2

img = cv2.imread('deneme.png',1) #take image and with -1,0,1 choice to color of image (-1 for default color / 0 for gray)
img = cv2.resize(img, (400,400)) #resize the image
#img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5) #resize the image with %50 if i give 2 for fx and fy this meaning multiply size with 2
img = cv2.rotate(img , cv2.ROTATE_90_CLOCKWISE) #rotate to image

cv2.imwrite('new_img.jpg',img) #save image to the folder

cv2.imshow('image', img)
cv2.waitKey(0) #this meaning wait infinitly if you write to 5 it wait 5 second
cv2.destroyAllWindows() 