#!/usr/bin/env python3

from ev3dev2 import *
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MediumMotor, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2

import time
import sys
from ev3dev2.display import Display
from PIL import Image

import cv2 as cv
import numpy as np

lcd = Display()

def avg_4(arr):
    arr = arr[0]
    return [(arr[0][0]+arr[1][0]+arr[2][0]+arr[3][0])/4,(arr[0][1]+arr[1][1]+arr[2][1]+arr[3][1])/4]

## CAMERA INIT STUFF
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)

print("1" + str(time.process_time()), file=sys.stderr)
# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
r,h,c,w = 250,90,400,125  # simply hardcoded the values
global track_window
track_window = (c,r,w,h)
# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

def take_pic():
    global track_window

    print("snap" + str(time.process_time()), file=sys.stderr)
    ret ,frame = cap.read()
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of color in HSV
        zero = np.array([0,100,100])
        lower = np.array([5,255,255])
        upper = np.array([250,100,100])
        biggest = np.array([255,255,255])
        # Threshold the HSV image to get only colors
        mask1 = cv.inRange(hsv, zero, lower)
        mask2 = cv.inRange(hsv, upper, biggest)
        mask = cv.add(mask1, mask2)
        # apply meanshift to get the new location
        ret, track_window = cv.CamShift(mask, track_window, term_crit)
        # Draw it on image
        pts = cv.boxPoints(ret)
        pts = np.int0(pts)

        saved_image = np.zeros((480,640,3), np.uint8)
        img2 = cv.polylines(saved_image,[pts],True, 255,5)

        avg = avg_4([pts])
        img2 = cv.circle(saved_image, avg, 10, 255, -1)

        cv.imwrite("disp.png",saved_image)

        print([pts], file=sys.stderr)
        print(avg_4([pts]), file=sys.stderr)
        print("end snap" + str(time.process_time()), file=sys.stderr)

        return avg[0]

    else:
        return False

## ROBOT INTI STUFF
m = MoveTank(OUTPUT_A, OUTPUT_B)

## MAIN LOOP
while True:
    xpos = take_pic()

    # if xpos == False: #most likeley some error in camera somewhere
    #     print("Some error occoured " + str(time.process_time()), file=sys.stderr)
    #     break
    
    x_ratio = xpos / 640.0 # fraction across screen

    print(str(x_ratio) +", "+ str(xpos) + " @ " + str(time.process_time()), file=sys.stderr)

    # lcd.circle(clear_screen=True, x=x_ratio*178, y=64, radius=10, fill_color='lightgrey')
    
    img = Image.open('disp.png')
    lcd.image.paste(img, (0,0))
    lcd.update()

    # if abs(x_ratio - 1) < 0.2: #can go straight
    #     m.on_for_seconds(SpeedPercent(40), SpeedPercent(40), seconds=0.25,block=False, brake=True)
    # else:
    # if xpos != 0:
    #     if xpos < 320:
    #         m.on_for_seconds(SpeedPercent(20), SpeedPercent(-20), seconds=0.1,block=False, brake=False)
    #     else:
    #         m.on_for_seconds(SpeedPercent(-20), SpeedPercent(20), seconds=0.1,block=False, brake=False)
    
        