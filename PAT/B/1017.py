#! /usr/bin/env python3

if(__name__ == "__main__"):
    nums = input()
    list1 = list(map(int, nums.split(' ')))
    list2 = []

    list2.append(str(list1[0] % list1[1]))
    list2.append(str(list1[0] // list1[1]))
    list2.reverse()
    print(' '.join(list2))