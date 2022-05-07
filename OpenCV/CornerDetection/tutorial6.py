from cv2 import resize
import numpy as np
import cv2

img = cv2.imread('corner.jpg')
img = cv2.resize(img, (0,0), fx = 0.2, fy = 0.2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #im not sure but i guess we need give gray image to the goodFeaturesToTrack mb because of it we change
#image to the gray image

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#cv2.goodFeaturesToTrack =>> (source image, how much corner you want to detect, quality, minumum euclidean distance)
corners = np.int0(corners) #convert converrs floating numbers to the integer numpy array


for corner in corners:
    x , y = corner.ravel() #ravel take the array elements [[x,y]] =>> [x,y]
    cv2.circle(img, (x,y), 5, (0,0,255), -1)

cv2.imshow('frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()