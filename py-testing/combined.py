import test_drawing as td
import webcam_pic as wp 
from threading import Thread
from time import sleep

Thread(target=wp.start).start()

i = 0

while True:
    i += 1
    td.step(i)
    sleep(0.01)
    if i > 10000: i = 0

td.exit()
wp.exit()
quit()