#!/usr/bin/env python3
from ev3dev2 import *
import time
import os
import sys
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_3
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.led import Leds

# these lines allow me to access a variety of libraries for motors, sensors etc.

gy = GyroSensor(INPUT_3)

m = MoveTank(OUTPUT_A, OUTPUT_B)

led = Leds()

# these are my variables for the control of motors, sensors and leds

led.set_color("RIGHT", "AMBER")
led.set_color("LEFT", "AMBER")

# this sets the led colour to amber once the execution reaches this stage in the code indicating the robot is ready to start

time.sleep(10)

init_angle = gy.angle

while True:
    angle = gy.angle

    # print(str(angle), file=sys.stderr)

    if angle > init_angle + 3:
        m.on_for_seconds(SpeedPercent(40), SpeedPercent(20), seconds=0.2, block=False, brake=True)
    elif angle < init_angle - 3:
        m.on_for_seconds(SpeedPercent(20), SpeedPercent(40), seconds=0.2, block=False, brake=True)
    else:
        m.on_for_seconds(SpeedPercent(40), SpeedPercent(40), seconds=0.5, block=True, brake=True)