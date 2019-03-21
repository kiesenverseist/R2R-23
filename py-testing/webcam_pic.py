import numpy as np
import cv2 as cv
import time as t 

cap = cv.VideoCapture(1)
exited = False

def start():
    while True:
        if exited:
            return

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Convert BGR to HSV
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            # define range of color in HSV
            lower = np.array([30,50,50])
            upper = np.array([70,255,255])
            # Threshold the HSV image to get only colors
            mask = cv.inRange(hsv, lower, upper)
            #mask = cv.fastNlMeansDenoising(mask, None, 10, 7, 21)
            # Bitwise-AND mask and original image
            res = cv.bitwise_and(frame,frame, mask= mask)

            cv.imshow('frame',frame)
            cv.imshow('mask',mask)
            cv.imshow('res',res)

            if cv.waitKey(1) & 0xFF == ord('q'):
                exit()

def exit():
    cap.release()
    cv.destroyAllWindows()
    exited = True