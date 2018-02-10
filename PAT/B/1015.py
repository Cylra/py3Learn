#! /usr/bin/env python3

def Rule(listAll, L, H):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for i in listAll:
        deGrade = i[1]
        caiGrade = i[2]
        if deGrade >= H and caiGrade >= H:
            list1.append(i)
        elif deGrade >= H and caiGrade< H:
            list2.append(i)
        elif deGrade < H and caiGrade < H and deGrade >= caiGrade :
            list3.append(i)
        else:
            list4.append(i)
    return (list1, list2, list3, list4)

#排序
def Sort(listTmp):
    for i in listTmp:
        i.append(i[1] + i[2])
    sorted(listTmp, key=lambda x: x[3])
    print("listTmp = ", listTmp)

if __name__ == "__main__":
    list1 = input().split(' ')
    N, L, H = list(map(int, list1))
    i = 0
    listAll = []
    while(i < N):
        list1 = input().split(' ')
        list1 = list(map(int, list1))
        #均高于及格线才行
        if list1[1] >= L and list1[2] >= L:
            listAll.append(list1)
        i = i+1
    
    #print(listAll)
    listR1, listR2,listR3,listR4 = Rule(listAll, L, H)
    #print("listR1 = ", listR1)
    # print("listR2 = ", listR2)
    # print("listR3 = ", listR3)
    # print("listR4 = ", listR4)
    Sort(listR1)