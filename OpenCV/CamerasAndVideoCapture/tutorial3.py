import numpy as np
import cv2 

cap = cv2.VideoCapture(0) #with 0 you open the default webcam
#cap = cv2.VideoCapture('filename') #you can use video like this 

while True:
    ret, frame = cap.read() #.read return to image with numpyArray(frame) and your camera is working true or not(ret)
    #if ret is false, this meanings we have a issue otherwise everything okey
    width = int(cap.get(3)) #3 for take a width and we convert float to int 
    height = int(cap.get(4)) #4 for tkae a height and we convert float to int 


    image = np.zeros(frame.shape, np.uint8)  #give a image shapes all 0 so this image fully black

    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5, fy = 0.5) #resize camera for copying with 4 times

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #paste top and left and paste to the image value 
    image[height//2:, :width//2] = smaller_frame #paste bottom and left and paste to the image value 
    image[:height//2, width//2:] = smaller_frame #paste top and right and paste to the image value 
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #paste bottom and right and paste to the image value 

    #cv2.imshow('frame', frame) #show the frame so your camera / open just 1 camera 1 image
    cv2.imshow('frame', image) #show the frame so your camera / open just 1 camera but 4 same image 

    if cv2.waitKey(1) == ord('x'): #wait one milisecond and then if we press to x (in the keybrod) window is close
        break

cap.release()  #give it to camera for other programs 
cv2.destroyAllWindows()