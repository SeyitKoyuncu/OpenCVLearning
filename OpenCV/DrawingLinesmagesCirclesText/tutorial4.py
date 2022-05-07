import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))


    #you can change img with frame and frames with img 

    img = cv2.line(frame, (0 , 0), (width,height), (0,250,0), 10) #draw line between starting and end coordinates
    #cv2.line =>> (source image, starting coordinate, ending coordinate, color, thickness)

    frame = cv2.rectangle(frame, (100,100), (200,200), (124,182,231, 5))
    #cv2.rectangle =>> (source image, starting coordinate, end cooridnate, color, thickness)

    img = cv2.circle(img, (300,300), 50, (231,192,10), 5)
    #cv2.circle =>>(source image, center coordinate, radius, color, thickness)

    font = cv2.FONT_HERSHEY_TRIPLEX
    img = cv2.putText(img, 'HELLO WORLD!', (200, height - 100), font, 4, (0,0,0), 10, cv2.LINE_AA)
    #cv2.putText =>> (source image, text, center coordinate, font, font scale, color, line thickness, line type)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()