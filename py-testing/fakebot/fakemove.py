from time import sleep
import globaldata as gb
import time

def move():
    sleep(0.1)
    print(gb.pos, gb.bearing, gb.target_rel_bearing, gb.detected, time.time())