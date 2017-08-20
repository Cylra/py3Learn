#! /usr/bin/python3

import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(("127.0.0.1", 9999))
print("Bind UDP on 9999...")
while True:
    data, addr = s1.recvfrom(1024)
    print("Received data from %s:%s." %(addr))
    s1.sendto(b"Hello, %s!" %(data), addr)