#! /usr/bin/env python3

if(__name__ == "__main__"):
    num = input()
    dict1 = {}
    for i in range(10):
        dict1[str(i)] = 0
    #print(dict1)
    for i in num:
        dict1[i] = dict1[i] + 1
    for key,value in dict1.items():
        if value != 0:
            print("%s:%s" %(key, value))