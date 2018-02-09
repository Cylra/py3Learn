#! /usr/bin/env python3

def judge(list1):
    LEN = len(list1)
    list2 = []
    list2.append(''.join(list(map(str, list(range(1,list1[0]+1))))))
    if(1 == LEN):
        pass
    elif(2 == LEN):
        list2.append('S'*list1[1])
    elif(3 == LEN):
        list2.append('S'*list1[1])
        list2.append('B'*list1[2])
    list2.reverse()
    print(''.join(list2))

if(__name__ == "__main__"):
    num = int(input())
    list1 = []
    while(num != 0):
        list1.append(num%10)
        num = num // 10
    judge(list1)