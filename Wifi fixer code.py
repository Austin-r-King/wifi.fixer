# Austin, Aiden

import time
import os
import socket
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

disconnect_log = []
# gets the current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
disconnect_log.append(current_time)
# print(current_time) to get current time when needed


# checks if connected to wifi
def connection_status():
    a_socket = socket.socket()
    try:
        a_socket.connect(("google.com", 80))
        print("Connected")
    except:
        print("No connection")


# resets wifi and connects
def reconnect():
    var = os.popen("/usr/local/bin/resetinet.sh")
    print(var)


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
            else:
                print('No')

            self.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())

forever=0
while forever==0:
    if print(connection_status())=="No connection":
        print(print(current_time))
        if print(GUI())=="Yes":
            print(reconnect())
        else:
            forever=0
    else:
        forever = 0
    time.sleep(2)
