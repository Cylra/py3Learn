#! /usr/bin/env python3

import math
#质数生成器
def genPrime(max):
    count = 0
    yield 2
    count = 1
    yield 3
    count = 2
    num = 5
    while(count < max):
        val = int(math.sqrt(num)) + 1 #取平方根
        for i in range(2, val):
            if num %i == 0: #被整除,说明不是质数
                break
            if i == val-1:  #是质数
                yield num
                count = count + 1;
        num = num + 2

if(__name__ == "__main__"):
    nums = input()
    low, high = list(map(int, nums.split(' ')))
    g1 = genPrime(high)
    listAll = list(g1)[low-1:] #取得全部满足要求的质数list

    list1 = []
    k = (high-low)//10 + 1
    for i in range(k):
        listTmp = list(map(str, listAll[i*10:(i+1)*10]))
        list1.append(listTmp)
    for i in list1:
        print(' '.join(i))