#!/usr/bin/env python

import asyncio
import websockets
import json
import time
from enum import Enum

visualiser = 0
robot = 0

async def join_network(data, ws):
    if data["content"] == "robot":
        robot = ws
    elif data["content"] == "visualiser":
        visualiser = ws
    
    await ws.send(json.dumps({
        "type" : "message",
        "content" : "Registered to network"
    }))

async def message(data, ws):
    pass

async def update_robot(data, ws):
    for i in range(100):
        msg = {
            "type" : "robot update",
            "content" : ""
        }

        dat = json.dumps(msg)
        await ws.send(dat)
        await asyncio.sleep(3)

sort_input = {
    'join' : join_network,
    'message' : message,
    'robot updated' : update_robot
}

async def handler(websocket, path):
    ws = websocket
    async for message in websocket:
        data = message.decode()
        recieved = json.loads(data)

        print(f"< {recieved}")

        await sort_input[recieved['type']](recieved, ws)

    # name = recived["content"]
    # greeting = f"Hello {name}!"
    # msg = {
    #     "type" : "message",
    #     "content" : f"{greeting}"
    # }
    # dat = json.dumps(msg)
    # await websocket.send(dat)
    # print(f"> {greeting}")

    # if recived["type"] == "join" and recived["content"] == "visualiser":
    #     print("Visualiser detected")
    
    # for i in range(100):
    #     msg = {
    #         "type" : "robot update",
    #         "content" : ""
    #     }
    #     dat = json.dumps(msg)
    #     await websocket.send(dat)
    #     print("> robot updated")
    #     await asyncio.sleep(1)

start_server = websockets.serve(handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("server started")
asyncio.get_event_loop().run_forever()