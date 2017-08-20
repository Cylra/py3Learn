#! /usr/bin/python3

import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Long', b'Yu', b'Com']:
    s1.sendto(data, ("127.0.0.1", 9999))
    print(s1.recv(1024).decode("utf-8"))
s1.close()