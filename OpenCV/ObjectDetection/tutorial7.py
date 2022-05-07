from turtle import width
import numpy as np
import cv2

img = cv2.imread('soccer_practice.jpg',0) #we convert to gray scale bc most of algrotihm works with gray scale for ball
template = cv2.imread('shoe.png',0) #we convert to gray scale bc most of algrotihm works with gray scal e for shoe
#template = cv2.imread('ball.png',0) #we convert to gray scale bc most of algrotihm works with gray scale
h, w = template.shape #we have gray scale so we dont need channels so we need just height and width

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] #methods for template matching

#we choice which methos is te best
for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method) #taking our templat image and try to find in your base image have it or not
    # then it return to new image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc

    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('tryit',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    