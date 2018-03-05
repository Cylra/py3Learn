#! /usr/bin/env python3
#-*- coding: utf-8 -*-
#参考网页
#http://blog.sina.com.cn/s/blog_53d874320102vdvu.html
#http://python.jobbole.com/87088/
#write by cc

import paramiko
import threading
import time
import subprocess
import os

def passive(myServer):
    print('thread [ %s ] is running...' % threading.current_thread().name)
    # 在远程机执行shell命令
    cmd_Line = "netperfmeter 9000"
    stdin, stdout, stderr = myServer.exec_command(cmd_Line)

def active(myClient, server_IP, run_Time):
    print('thread [ %s ] is running...' % threading.current_thread().name)
    cmd_Line = "netperfmeter "+ server_IP + ":9000 -runtime=" + str(run_Time) + ' ' + \
                '-scalar=scalar.sca' + ' ' + \
                '-vector=vector.vec -control-over-tcp -tcp const0:const0:const0:const1460' + \
                ':cmt=off'  #:rcvbuf=4000000:sndbuf=4000000
    print("客户端命令为\n%s" %cmd_Line)
    myClient.exec_command('mkdir -p mptcp; rm -rf mptcp/*.vec; ')
    stdin, stdout, stderr = myClient.exec_command(cmd_Line)
    #time.sleep(run_Time)
    #卡住,不使用print会导致runtime无效
    #20180305更新 必须读取stdout并输出,用于阻塞线程,
    #若使用sleep阻塞,会导致发送端统计的数据不全
    for line in stdout.readlines():
        print(line.strip('\n'))
    #print(stdout.read().decode('utf-8'))
    print(stderr.read().decode('utf-8'))
    myClient.exec_command('mv *.vec mptcp/')

#客户端和服务器端发消息
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
    myServer.close()
    myClient.close()
    print('OK')

if __name__ == "__main__":
    main("192.168.5.16", "long", "nornet", "192.168.5.13", "long", "hp", 10)

#定量分析
def analysis_2(vec_file):
    #写死vec文件和py脚本在同一文件夹下,不然文件的绝对路径中的 和'不好处理
    vec_file = os.path.split(vec_file)[1]
    file_tmp = '111'
    cmd = 'grep Total # | grep Received |' + \
       "awk '{printf (\"%.2f\\n\", $9/1024/1024)}'" + \
       "| sed -n '2,61p' > " + file_tmp
    cmd = cmd.replace('#', vec_file)
    #print(cmd)
    subprocess.call(cmd, shell = True)
    list1 = []
    list2 = []
    i = 0
    with open(file_tmp, 'r') as f:
        for line in f.readlines():
            if i<30:
                list1.append(float(line.strip('\n')))
            else:
                list2.append(float(line.strip('\n')))
            i += 1
    list3 = list(map(lambda x: float("%.2f" %(x[0]-x[1])), zip(list1, list2)))
    #print(list3)
    avg = float("%.2f" %(sum(list3)/len(list3)))
    return avg