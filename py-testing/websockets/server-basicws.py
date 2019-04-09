#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    print("connection attempted")
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, '192.168.137.1', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("server started")
asyncio.get_event_loop().run_forever()