#! /usr/bin/python3

import os

print('Process (%s) start...' %(os.getpid()))
# Only works on Unix/Linux/Mac
pid = os.fork()
if 0 == pid:
    print('This is a child process,my id is (%s), my parent is (%s).' \
           %(os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' %(os.getpid(), pid))