# Austin, Aiden

import time
import socket

disconnect_log = []
# gets the current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
disconnect_log.append(current_time)
# print(current_time) to get current time when needed


def connection():
    try:
        socket.create_connection(("8.8.8.8",443))
    except:
        print('no_connection')

def connection_status():
    a_socket=socket.socket()
    try:
        a_socket.connection(("127.0.0.1", 80))
    except:
        print("No connection")

print(connection_status())


