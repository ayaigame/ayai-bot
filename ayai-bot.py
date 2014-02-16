#!/usr/bin/python

from websocket import create_connection
import json
import time
import random
ws = create_connection("ws://192.168.100.10/ws")
init_msg = {'type': 'init'}

ws.send(json.dumps(init_msg))

time.sleep(1)

while True:
    direction = random.randint(0, 7)
    move_msg = {'type': 'move', 'dir': direction, 'start': True}
    ws.send(json.dumps(move_msg))
    time.sleep(random.randint(2, 10))
    move_msg = {'type': 'move', 'dir': direction, 'start': False}
    ws.send(json.dumps(move_msg))


ws.close()
