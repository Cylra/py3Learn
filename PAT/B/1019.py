#! /usr/bin/env python3

#4位整数
def isEqual(num):
    if(num[0] == num[1] and num[1] == num[2] and num[2] == num[3]):
        return True
    else:
        return False

def getValue(result):
    list1 = []
    for i in result:
        list1.append(i)
    #print(list1)
    list1.sort()
    B = ''.join(list1)
    list1.reverse()
    A = ''.join(list1)
    return (A,B)

def repair(k):
    s1 = str(k)
    if 1 == len(s1):
        return '000' + s1
    elif 2 == len(s1):
        return '00' + s1
    elif 3 == len(s1):
        return '0' + s1
    elif 4 == len(s1):
        return s1

if(__name__ == "__main__"):
    num = input()
    if len(num) < 4:
        exit(-1)
    if isEqual(num):
        print("%s - %s = 0000" %(num, num))
    else:
        result = num
        while(result != '6174'):
            A,B = getValue(result)
            k = int(A) - int(B)
            result = repair(k)
            #result可能是3位数,需要在前面补0
            print("%s - %s = %s" %(A, B, result))