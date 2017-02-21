import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QMessageBox, QFileDialog, QApplication, QPushButton, QInputDialog, QLineEdit)
import socket
import msgpack
import os
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.fileName=""
        self.text=""
        btn1 = QPushButton("Press", self)
        btn1.clicked.connect(self.onBtn1)
        self.show()

    def onBtn1(self):

        self.fileName, _  = QFileDialog.getOpenFileName(self, 'Open file', '/pictures/pictures/ ')
        #######
        sock = socket.socket()
        sock.connect(('10.0.0.130', 9090))
        ######## PICTURE
        with open(self.fileName, "rb") as f:
            btf = f.read()
        #### TIME
        time = 300
        #### COOORD
        x = 100
        y = 100
        ### DICT
        dictry = {'Image': btf, 'Time': time, 'x': x, 'y': y}
        dumped_dict = msgpack.packb(dictry)
        #send_dict = bytes(dumped_dict)
        sock.sendall(dumped_dict)
        sock.close()
        print (self.fileName)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
