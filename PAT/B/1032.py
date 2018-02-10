#! /usr/bin/env python3

if __name__ == "__main__":
    count = int(input())
    i = 0
    dict1 = {}
    while(i < count):
        list1 = input().split(' ')
        school = list1[0]
        score = int(list1[1])
        if school not in dict1:
            dict1[school] = 0 + score
        else:
            dict1[school] += score
        i = i+1
    list1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    #print(list1[0])
    print(' '.join(list(map(str, list(list1[0])))))