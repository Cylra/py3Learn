#! /usr/bin/env python3

def isOdd(num):
    if(num%2 == 1):
        return True
    else:
        return False

if(__name__ == "__main__"):
    num = input()
    num = int(num)
    if(num > 1000 or num<1):
        exit(-1)
    i = 0
    while(num != 1):
        if(isOdd(num)):
            num = (3*num+1)/2
        else:
            num = num/2
        i = i+1
    print(i)