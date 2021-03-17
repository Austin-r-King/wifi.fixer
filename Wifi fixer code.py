# Austin, Aiden

import time
import socket

disconnect_log = []
# gets the current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
disconnect_log.append(current_time)

# print(current_time) to get current time when needed



def connection_status():
    try:
        socket.socket.connect(("8.8.8.8", 80))
        print("Connected")
    except:
        print("No connection")

print(connection_status())
