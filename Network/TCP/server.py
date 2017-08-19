#! /usr/bin/python3

import socket
import threading
import time

def tcplink(sock, addr):
    print("Accept new connectin from %s:%s..." %(addr))
    sock.send(b"Welcome!")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        print(("Hello, %s!" %(data)).encode('utf-8'))
        sock.send(("Hello, %s!" %(data)).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' %(addr))

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind(('127.0.0.1', 9999))
s1.listen(5)
print('Waiting for connection...')
while True:
    sock, addr = s1.accept()
    # 创建新线程处理TCP连接请求
    t =  threading.Thread(target=tcplink, args=(sock, addr))
    t.start()