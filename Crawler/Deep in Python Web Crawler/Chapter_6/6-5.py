#! /usr/bin/python3

import threading
import queue

class A(threading.Thread):
    def __init__(self):
        #初始化该线程
        threading.Thread.__init__(self)
    def run(self):
        #该线程要执行的程序内容
        for i in range(10):
            print("我是线程 A")

class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(10):
            print("我是线程 B")

t1 = A()
t2 = B()
t1.start()
t2.start()

a = queue.Queue()
a.put("hello")
a.put("world")
a.task_done()
print(a.get())