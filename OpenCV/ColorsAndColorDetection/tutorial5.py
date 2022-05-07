from cv2 import bitwise_and
import numpy as np
import cv2 

cap = cv2.VideoCapture(0) #with 0 you open the default webcam
#cap = cv2.VideoCapture('filename') #you can use video like this 

while True:
    ret, frame = cap.read() #.read return to image with numpyArray(frame) and your camera is working true or not(ret)
    #if ret is false, this meanings we have a issue otherwise everything okey
    width = int(cap.get(3)) #3 for take a width and we convert float to int 
    height = int(cap.get(4)) #4 for tkae a height and we convert float to int 

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #take bgr pixels and then convert to hsv
    lower_blue = np.array([90,50,50]) #lighter blue codde
    upper_blue = np.array([130, 255, 255]) #dark blue code

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #it returns new image which are given color range pixels
    #mask is all created with zeros and ones, whites are showing pixels in the result

    result = cv2.bitwise_and(frame,frame, mask = mask) #if bitwise_and return 1 so if we have blue pixels(because we give range for blue pixels) we keept it 
    
    cv2.imshow('result', result) #show the frame so your camera / open just 1 camera but 4 same image 
    cv2.imshow('mask', mask) #show the frame so your camera / open just 1 camera but 4 same image 

    if cv2.waitKey(1) == ord('x'): #wait one milisecond and then if we press to x (in the keybrod) window is close
        break

cap.release()  #give it to camera for other programs 
cv2.destroyAllWindows()