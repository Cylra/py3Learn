#! /usr/bin/env python3

if(__name__ == "__main__"):
    C1,C2 = list(map(int, input().split(' ')))
    CLK_TCK = 100
    value = C2 - C1
    #四舍五入
    #print(value)
    if value % CLK_TCK <50:
        value = value // CLK_TCK
    else:
        value = value // CLK_TCK + 1
    #print('----', value)
    list1 = []
    list1.append(value // 3600)
    value = value % 3600
    list1.append(value // 60)
    list1.append(value % 60)
    list1 = list(map(str, list1))
    #print(list1)
    for i in range(3):
        if len(list1[i]) < 2:
            list1[i] = '0' + list1[i]
    #print('---', list1)
    print(':'.join(list1))