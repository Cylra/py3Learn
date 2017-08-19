#! /usr/bin/python3

import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('www.sina.com.cn', 80))
s1.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    d = s1.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s1.close()

header, html = data.split(b'\r\n\r\n', 1)
print("Sina's Header:\n---------")
print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:
    f.write(html)