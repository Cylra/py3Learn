#! /usr/bin/env python3

if(__name__ == "__main__"):
    list1 = input().split(' ')
    list1 = list(map(int, list1))
    #没有给0
    if list1[0] == 0:
        for index in range(1,10):
            list1[index] = str(index) * list1[index]
        print("".join(list(map(str, list1[1:]))))
    else:
        k = 0
        #print(list1)
        for index in range(1,10):
            if list1[index] > 0:
                k = index
                list1[index] -= 1
                break
        for index in range(0,10):
            list1[index] = str(index) * list1[index]
        print(str(k) + "".join(list(map(str, list1))))        