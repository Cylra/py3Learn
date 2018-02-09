#! /usr/bin/env python3

if(__name__ == "__main__"):
    num = int(input())
    i = 0
    while(i < num):
        tmp = input()
        nums = list(map(int, tmp.split(' ')))
        if(nums[0] + nums[1] > nums[2]):
            print("Case #" + str(i+1) + ": true")
        else:
            print("Case #" + str(i+1) + ": false")
        
        i = i+1