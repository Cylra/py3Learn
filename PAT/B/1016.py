#! /usr/bin/env python3

if(__name__ == "__main__"):
    list1 = input().split(' ')
    s1, s2 = list1[0], list1[2]
    key1, key2 = list1[1], list1[3]
    count1, count2 = 0, 0
    for i in s1:
        if i == key1:
            count1 = count1 + 1
    for i in s2:
        if i == key2:
            count2 = count2 + 1
    A = key1*count1
    B = key2*count2
    if A == '':
        A = '0'
    if B == '':
        B ='0'
    print("%d" %(int(A)+ int(B)))