import random
import time
import json
from threading import Thread
from tornado.websocket import WebSocketClosedError

thread = None

def background_thread():
    """Example of how to send server generated events to clients."""
    while True:
        time.sleep(1)

        try:
            ws.send(
                json.dumps({
                    'response': [
                        [int(time.time())*1000, random.randint(0, 1000)]
                    ]
                })
            )

            # socket_handler.write_message({
            #     'response': [
            #         [int(time.time())*1000, random.randint(0, 1000)]
            #     ]})
        except WebSocketClosedError as e:
            print "error"
            print e.message
            return

import websocket
ws = websocket.WebSocket()
ws.connect("ws://localhost:8888/ws")

global thread
if thread is None:
    thread = Thread(target=background_thread)
    thread.start()
