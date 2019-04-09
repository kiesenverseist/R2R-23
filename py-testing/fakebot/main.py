import fakemove as move
import fakecam as cm
import net
import threading as threading
import time
import globaldata as gb

last_time = time.time()
i = 0

dat = "something"
while True:
    if time.time() - last_time > 3:
        last_time = time.time()
        th = threading.Thread(target=cm.pic, name="cam")
        th.start()
    
    i += 1
    if i>= 10:
        i = 0
        th = threading.Thread(target=net.send_data, args=(dat,), name="net")
        th.start()
    
    move.move()
    

    