#!/usr/bin/env python

# WS client example

import asyncio
import websockets
from time import sleep

async def hello():
    async with websockets.connect(
            'ws://192.168.137.1:8765') as websocket:
        name = "GROUP 23 BOT "

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
sleep(10)