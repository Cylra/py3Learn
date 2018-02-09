#! /usr/bin/env python3

if(__name__ == "__main__"):
    str1 = input()
    list1 = [[], [], [], [], [], []]
    for i in str1:
        if 'P' == i:
            list1[0].append(i)
        elif 'A' == i:
            list1[1].append(i)
        elif 'T' == i:
            list1[2].append(i)
        elif 'e' == i:
            list1[3].append(i)
        elif 's' == i:
            list1[4].append(i)
        elif 't' == i:
            list1[5].append(i)

    # for i in list1:
    #     print(i)
    # print("------------")
    lenList = [len(x) for x in list1]
    #print("lenList = " ,lenList)
    High = max(lenList)
    index = 0
    while(index < High):
        if(index < lenList[0]):
            print(list1[0][index], end = '')
        if(index < lenList[1]):
            print(list1[1][index], end = '')
        if(index < lenList[2]):
            print(list1[2][index], end = '')
        if(index < lenList[3]):
            print(list1[3][index], end = '')
        if(index < lenList[4]):
            print(list1[4][index], end = '')
        if(index < lenList[5]):
            print(list1[5][index], end = '')

        index = index + 1