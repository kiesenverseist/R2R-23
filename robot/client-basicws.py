#!/usr/bin/env python3
import asyncio
import websockets
from time import sleep

ws = None

async def init():
    async with websockets.connect(
            'ws://192.168.137.1:8765') as websocket:
        name = "GROUP 23 BOT"
        ws = websocket
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))

def send_message(dat):
    asyncio.get_event_loop().run_until_complete(_sm(dat))

async def _sm(dat):
    async with websockets.connect(
            'ws://192.168.137.1:8765') as websocket:
        name = "GROUP 23 BOT"
        ws = websocket
        await websocket.send(name)
        print("> {}".format(name))

        recv = await websocket.recv()
        print("< {}".format(recv))

def start():
    asyncio.get_event_loop().run_until_complete(init())

start()