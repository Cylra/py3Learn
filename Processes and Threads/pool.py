#! /usr/bin/python3

from multiprocessing import Pool

import os, time, random

def long_time_task(name):
    print('Run task %s (id is %s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end   = time.time()
    print('Task %s runs %.2f secondes.' %(name, (end - start)))

if __name__ == "__main__":
    print("Parent process's id %s." %(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args = (i, ))
    print('Waitng for all subprocesses done...')
    p.close()
    #wait for all subprocesses
    p.join()
    print("All subprocesses done.")