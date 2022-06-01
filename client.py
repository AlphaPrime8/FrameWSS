#!/usr/bin/env python

import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://localhost:8765") as websocket:
        await websocket.send(str(300))
        data = await websocket.recv()
        data = bytearray(data)
        frame = data[:-3]
        idx = data[-3:]
        idx = int.from_bytes(idx, 'little', signed=False)
        print(f" got index {int(idx)}")
        print(f"got data frame of type {type(frame)} and len {len(frame)}")

asyncio.run(hello())
