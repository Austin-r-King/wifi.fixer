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
        socket.create_connection(("8.8.8.8",443))
        return 'True'
    except OSError:
        pass
    return 'False'

print(connection_status)


