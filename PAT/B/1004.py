#! /usr/bin/env python3

if(__name__ == "__main__"):
    num = int(input())
    i = 0
    list1 = []
    while(i < num):
        tmp1 = input()
        list1.append(tmp1.split(' '))
        i = i+1
    #print(list1)
    list2 = []
    for i in list1:
        list2.append(int(i[-1]))
    High  = list2.index(max(list2))
    Low = list2.index(min(list2))
    print(' '.join(list1[High][:-1]))
    print(' '.join(list1[Low][:-1]))