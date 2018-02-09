#! /usr/bin/env python3

def pinyin(i):
    if(i == 0):
        return "ling"
    elif(i == 1):
        return "yi"
    elif(i == 2):
        return "er"
    elif(i == 3):
        return "san"
    elif(i == 4):
        return "si"
    elif(i == 5):
        return "wu"
    elif(i == 6):
        return "liu"
    elif(i == 7):
        return "qi"
    elif(i == 8):
        return "ba"
    elif(i == 9):
        return "jiu"

if(__name__ == "__main__"):
    num = int(input())
    sum = 0
    while(num != 0):
        sum = sum + num%10
        num = num//10
    #print("sum=",sum)
    list1 = []
    while(sum != 0):
        list1.append(sum%10)
        sum = sum //10
    list1.reverse()
    list2 = []
    for i in list1:
        list2.append(pinyin(i))
    #print(list2)
    print(' '.join(list2))