#! /usr/bin/env python3

if(__name__ == "__main__"):
    peopel,count = list(map(int, input().split(' ')))
    fullMarks = list(map(int, input().split(' ')))
    answers = list(map(int, input().split(' ')))
    #print("answers = ", answers)
    i = 0
    list1 = []
    while(i < peopel):
        grades = list(map(int, input().split(' ')))
        index = 0
        sum = 0
        while(index < count):
            if(answers[index] == grades[index]):
                sum = sum + fullMarks[index]
            index = index+1
        list1.append(sum)
        i = i+1
    for i in list1:
        print(i)