from time import sleep
import random as r
import globaldata as gb

def pic():
    sleep(1)
    gb.detected = not gb.detected
    gb.target_rel_bearing = r.randint(-1, 1)
    print("pic donne'd")
