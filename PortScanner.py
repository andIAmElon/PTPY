#!/usr/bin/python3

import socket

s = socket.socket()

HOST = "127.0.0.1"
PORT = 7777

#connecting 
s.connect((HOST,PORT))
#connecting
#socket.create_connection ((HOST,PORT))

