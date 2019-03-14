#!/usr/bin/env python3
from ev3dev2 import *
import time
import os
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor

# these lines allow me to access a variety of libraries for sensors, motors etc.

TS = TouchSensor()

US = UltrasonicSensor()

MOVE = MoveTank(OUTPUT_A, OUTPUT_B)

# this is my variable for the simultaneous control of 2 large motors attached to brick outputs A and B

MOVE.on_for_rotation(SpeedPercent(40), SpeedPercent(40), block=True, brake=True, 1)

# this turns the motor 3 rotations and both motors are at 60% speed


while not TS.is_pressed:
    if US.distance_centimetres < 10:
    MOVE.on_for_rotation(SpeedPercent(20), Speed SpeedPercent(-20),block=False, brake=True,1)
    else:
    MOVE.on_for_rotation(SpeedPercent(40), SpeedPercent(40), block=True, brake=True)

# this measures the distance from the sensor to the wall, if this distance is less than 10cm it turns right

if TS.is_pressed:
    off(Brake=True)
    MOVE.on_for_rotation(SpeedPercent(-20), SpeedPercent(-20), block=False, brake=True, 1)
    MOVE.on_for_rotation(SpeedPercent(-20), SpeedPercent(20), block=False, brake=True, 1)
else:
    MOVE.on_for_rotation(SpeedPercent(40), SpeedPercent(40), block=True, brake=True)

# this  the touch sensor is pressed, apply the brakes causing the motors to stop, then it should reverse and turn to the right, otherwise it will just continue on its path
