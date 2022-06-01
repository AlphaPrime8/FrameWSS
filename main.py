import asyncio
import websockets
import os

dpath = "/home/myware/PycharmProjects/makeBalls"
MAX_FRAME = 114527


def lookup_frame(n):
    fpath = os.path.join(dpath, f"frame{n}.jpg")
    with open(fpath, "rb") as f:
        data = f.read()
        frame = bytearray(data)
    return frame


async def echo(websocket):
    async for message in websocket:
        try:
            print(f"got message {message}")
            n = int(message)
            if 0 <= n <= MAX_FRAME:
                frame = lookup_frame(n)
                index_bytes = int(n).to_bytes(3, 'little', signed=False)
                index_bytes = bytearray(index_bytes)
                print(f"got index bytes {index_bytes}")
                print(f"got frame bytes of len {len(frame)}")
                frame.extend(index_bytes)
                print(f"attempting to send frame of new total len {len(frame)}")
                await websocket.send(frame)
        except Exception as e:
            print(f"got exception {e}")


async def main():
    async with websockets.serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())


