#! /usr/bin/env python3

def isOdd(num):
    if(num%2 == 1):
        return True
    else:
        return False

def getSeq(num):
    list1 = []
    while(num != 1):
        if(isOdd(num)):
            num = (3*num+1)/2
        else:
            num = num/2
        num = int(num)
        list1.append(num)
    #list1.reverse()
    return list1

#是否都访问过了
def isUnfinished(dict1):
    for key in dict1:
        if dict1[key] == False:
            return True
    return False

if(__name__ == "__main__"):
    count = int(input())
    nums = input()
    list1 = list(map(int, nums.split(' ')))
    #构建dict,设置是否已访问标记
    dict1 = {}
    for i in list1:
        dict1[i] = False
    while(isUnfinished(dict1)):
        for key in dict1:
            if dict1[key] == False:
                dict1[key] = True
                listOne = getSeq(key)
                for j in listOne:
                    if j in dict1:
                        del dict1[j]
                #print('----', dict1)
                break
    list1 = []
    for key in dict1:
        list1.append(key)
    list1.sort()
    list1.reverse()
    print(' '.join(list(map(str, list1))))