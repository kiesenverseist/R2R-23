import asyncio
import websockets
import json as json
from time import sleep
import globaldata as gb

def send_data(data):
    message = {
        "type" : "robot update",
        "content" : "test"
    }
    final = json.dumps(message)
    print(final)
    sleep(0.5)
