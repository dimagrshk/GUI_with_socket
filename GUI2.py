import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QMessageBox, QFileDialog, QApplication, QPushButton, QInputDialog, QLineEdit)
import socket

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.fileName=""
        self.text=""
        btn1 = QPushButton("Press", self)
        btn1.clicked.connect(self.onBtn1)
        self.show()

    def onBtn1(self):

        self.fileName, _  = QFileDialog.getOpenFileName(self, 'Open file', '/pictures/pictures/ ')
        sock = socket.socket()
        sock.connect(('77.47.198.64', 9090))
        bytes = open(self.fileName).read()
        sock.send(bytes)
        sock.close()
        print (self.fileName)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())