#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#参考网页
#http://blog.sina.com.cn/s/blog_53d874320102vdvu.html
#http://python.jobbole.com/87088/
#write by cc

import paramiko
import threading
import time

def passive(myServer):
    print('thread [ %s ] is running...' % threading.current_thread().name)
    # 在远程机执行shell命令
    cmd_Line = "netperfmeter 9000"
    stdin, stdout, stderr = myServer.exec_command(cmd_Line)

def active(myClient, server_IP, run_Time):
    print('thread [ %s ] is running...' % threading.current_thread().name)
    cmd_Line = "netperfmeter "+ server_IP + ":9000 -runtime=" + str(run_Time)
    print("客户端命令为%s" %cmd_Line)
    stdin, stdout, stderr = myClient.exec_command(cmd_Line)
    time.sleep(run_Time)
    #卡住,不使用print会导致runtime无效
    #print(stdout.read().decode('utf-8'))

def main(server_IP, server_User, server_Pwd,
         client_IP, client_User, client_Pwd,
         run_Time):
    # 新建一个ssh客户端对象
    myServer = paramiko.SSHClient()
    myClient = paramiko.SSHClient()
    # 设置成默认自动接受密钥
    myServer.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    myClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接远程主机
    myServer.connect(server_IP, username=server_User, password=server_Pwd)
    myClient.connect(client_IP, username=client_User, password=client_Pwd) #本机

    t1 = threading.Thread(target=passive, name='被动端', args=(myServer, ))
    t2 = threading.Thread(target=active, name='主动端', args=(myClient, server_IP, run_Time))
    t1.start()
    t2.start()
    t2.join()
    myServer.exec_command("pkill netperfmeter")
    t1.join()
    #断开
    myClient.close()
    print('OK')

if __name__ == "__main__":
    main("192.168.5.16", "long", "nornet", "192.168.5.13", "long", "hp", 10)