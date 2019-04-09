#!/usr/bin/env python3
from ev3dev2 import *
from time import sleep
import os
from ev3dev2.display import Display
from sys import stderr

print("something", file=stderr)
print('EV3', 'Python rules!')

lcd = Display()

lcd.circle(clear_screen=False, x=89, y=64, radius=61, fill_color='lightgrey')
lcd.circle(False, x=65, y=45, radius=10, fill_color='black')
lcd.circle(False, x=113, y=45, radius=10, fill_color='black')

sleep(10)