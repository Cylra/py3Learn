#! /usr/bin/env python3

if(__name__ == "__main__"):
    list1 = input().split(' ')
    list1 = list(map(int, list1))
    sum = list1[0] + list1[1]
    if sum == 0: #0的任何进制都是0
        print('0')
    else:
        k = list1[2]
        listTmp = []
        while (sum != 0):
            listTmp.append(sum % k)
            sum = sum // k
        listTmp.reverse()
        print(''.join(list(map(str, listTmp))))