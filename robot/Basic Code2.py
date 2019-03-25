#!/usr/bin/env python3
from ev3dev2 import *
import time
import os
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MediumMotor, OUTPUT_C
# from ev3dev2.sensor import INPUT_1
# from ev3dev2.sensor import INPUT_2
# from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor

# these lines allow me to access a variety of libraries for sensors, motors etc.
print("starting")
# ts = TouchSensor(INPUT_1)

# us = UltrasonicSensor(INPUT_2)

m = MoveTank(OUTPUT_A, OUTPUT_B)

a = MediumMotor(OUTPUT_C)

while True:
    a.on_for_degrees(-100,2000, block = True)
    # a.wait_until_not_moving()
    a.on_for_degrees(100, 2000, block = True)
    # a.wait_until_not_moving()

m.on_for_degrees(100, 100, 90, block = False, brake = True)

print("done")
# this is my variable for the simultaneous control of 2 large motors attached to brick outputs A and B

#while not TS.is_pressed:
    #if US.distance_centimetres < 10:
        #m.on_for_seconds(SpeedPercent(20), SpeedPercent(-20), seconds=1,block=False, brake=True)
    #else:
        #m.on_for_seconds(SpeedPercent(40), SpeedPercent(40), seconds=1 block=True, brake=True)

# this measures the distance from the sensor to the wall, if this distance is less than 10cm it turns right
#while True:
#    if ts.is_pressed:
#        m.on_for_seconds(SpeedPercent(-20), SpeedPercent(-20), seconds=1, block=False, brake=True)
#        m.on_for_seconds(SpeedPercent(-20), SpeedPercent(20), seconds=1, block=False, brake=True)
#    else:
#        m.on_for_seconds(SpeedPercent(40), SpeedPercent(40), seconds=1, block=True, brake=True)

# this  the touch sensor is pressed, apply the brakes causing the motors to stop, then it should reverse and turn to the right, otherwise it will just continue on its path
