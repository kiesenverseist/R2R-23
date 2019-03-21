#!/usr/bin/env python3
from ev3dev2 import *
import time
import os
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.led import Leds

leds = Leds()
leds.set_color('LEFT', 'YELLOW')
leds.set_color('RIGHT', 'YELLOW')

# these lines allow me to access a variety of libraries for sensors, motors etc.

# TS = TouchSensor(INPUT_1)

#US = UltrasonicSensor()

lm = LargeMotor(OUTPUT_A)

rm = LargeMotor(OUTPUT_B)

# this is my variable for the simultaneous control of 2 large motors attached to brick outputs A and B

lm.on_for_rotations(speed = 40, rotations = 20, brake = True, block = False)
rm.on_for_rotations(speed = 40, rotations = 20, brake = True, block = False)

# while True:
#     if TS.is_pressed:
#         lm.on_for_seconds(speed = 40, seconds = 0.1, brake = True, block = False)
#         rm.on_for_seconds(speed = 40, seconds = 0.1, brake = True, block = False)
#    else:
#        m.on_for_rotation(SpeedPercent(40), SpeedPercent(40), block=True, brake=True)

# this measures the distance from the sensor to the wall, if this distance is less than 10cm it turns right

#if TS.is_pressed:
#   off(Brake=True)
#  m.on_for_rotation(SpeedPercent(-20), SpeedPercent(-20), block=False, brake=True, 1)
# m.on_for_rotation(SpeedPercent(-20), SpeedPercent(20), block=False, brake=True, 1)
#else:
#    m.on_for_rotation(SpeedPercent(40), SpeedPercent(40), block=True, brake=True)

# this  the touch sensor is pressed, apply the brakes causing the motors to stop, then it should reverse and turn to the right, otherwise it will just continue on its path
