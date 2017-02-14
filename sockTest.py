#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import cv2
from PIL import Image
import numpy

file_Name = 'NEWPICTURE.jpg'
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('77.47.198.64', 9090))
sock.setblocking(False)
sock.listen(1)


def maybeNewImage():
    try:
        conn, addr = sock.accept()
    except:
        return None
    conn.setblocking(True)
    data = conn.recv(8000)
    new_file = open(file_Name, 'w')
    new_file.write(data)
    new_file.close()
    imgRet = cv2.imread(file_Name)
    conn.close()
    return(imgRet)



