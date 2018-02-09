#! /usr/bin/env python3

def findCount(score, scores):
    i = 0
    for k in scores:
        if k == score:
            i = i+1
    return i

if(__name__ == "__main__"):
    num = input()
    scores = list(map(int , input().split(' ')))
    list1 = list(map(int , input().split(' ')))

    i = 1
    list2 = []
    while(i <= list1[0]):
        list2.append(str(findCount(list1[i], scores)))
        i = i+1
    
    print(' '.join(list2))