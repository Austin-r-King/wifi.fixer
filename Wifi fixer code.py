# Austin, Aiden

import time
import os
import socket
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox




# checks if connected to wifi
def connection_status():
    a_socket = socket.socket()
    try:
        a_socket.connect(("google.com", 80))
        print("Connected")
        time.sleep(5)
        print(connection_status())
        # Connected
    except:
        print("Not connected")
        print(log())


# resets wifi and connects
def reconnect():
    var = os.popen("/usr/local/bin/resetinet.sh")
    print(var)
    time.sleep(3)
    print(connection_status())


def GUI():
    class App(QWidget):

        def __init__(self):
            super().__init__()
            self.title = 'PyQt5 messagebox'
            self.left = 10
            self.top = 10
            self.width = 320
            self.height = 200
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)

            buttonReply = QMessageBox.question(self, 'Wifi reset', "Do you want to reconnect to wifi?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                print('Yes')
                print(reconnect())
            else:
                print('No')
                time.sleep(60)
                print(connection_status())
            self.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

def log():
    disconnect_log = []
    # gets the current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    disconnect_log.append(current_time)
    print(GUI())
    # print(current_time) to get current time when needed

print(connection_status())
