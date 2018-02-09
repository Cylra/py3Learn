#! /usr/bin/env python3

import math
def primes(num):
    list1 = [2, 3]
    for i in list(range(3, num+1, 2)):
        #取根号,减少计算量
        tmp = int(math.sqrt(i))+1
        for j in list(range(2, tmp)):
            if i % j == 0:
                break
            if(j == tmp-1):
                list1.append(i)
    return list1

if(__name__ == "__main__"):
    num = int(input())
    list1 = primes(num)
    #print("list1= ", list1)
    i = 0
    for index in range(len(list1)-1):
        if(2 == list1[index+1] - list1[index]):
            i = i+1
    print(i)