#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import json

async def hello(websocket, path):
    print("connection attempted")
    raw = await websocket.recv()
    data = raw.decode()
    print(data)
    msg = json.loads(data)

    print(f"< {msg}")
    name = msg["content"]
    greeting = f"Hello {name}!"
    msg = {
        "type" : "message",
        "content" : f"{greeting}"
    }
    dat = json.dumps(msg)
    await websocket.send(dat)
    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("server started")
asyncio.get_event_loop().run_forever()