#! /usr/bin/env python3

if(__name__ == "__main__"):
    nums = input()
    list1 =list(map(int, nums.split(' ')))
    #警惕第1个数,代表后面给出的数的数目N
    del list1[0]
    listA1 = [x for x in list1 if x%5==0 and x%2 ==0]
    listA2 = [x for x in list1 if x%5==1] 
    listA3 = [x for x in list1 if x%5==2]
    listA4 = [x for x in list1 if x%5==3]
    listA5 = [x for x in list1 if x%5==4] 
    listAll = []
    index = 1
    while(index < len(listA2)):
        listA2[index] = -1 * listA2[index]
        index = index + 2

    if 0 == len(listA1):
        listAll.append('N')
    else:
        listAll.append(str(sum(listA1)))
    if 0 == len(listA2):
        listAll.append('N')
    else:
        listAll.append(str(sum(listA2)))
    if 0 == len(listA3):
        listAll.append('N')
    else:
        listAll.append(str(len(listA3)))
    if 0 == len(listA4):
        listAll.append('N')
    else:
        listAll.append(str(round(sum(listA4)/len(listA4), 1)))
    if 0 == len(listA5):
        listAll.append('N')
    else:
        listAll.append(str(max(listA5)))

    print(' '.join(listAll))