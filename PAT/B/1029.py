#! /usr/bin/env python3

if(__name__ == "__main__"):
    src = input().upper()
    actual = input().upper()
    list1 = []
    list2 = []
    for i in src:
        if i not in list1:
            list1.append(i)
    for i in actual:
        if i not in list2:
            list2.append(i)
    
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    print(''.join(list3))