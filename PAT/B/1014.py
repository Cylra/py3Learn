#! /usr/bin/env python3

def translate(list2):
    list3 = []
    listWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    listTmp = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
    listHour = listTmp + list(map(str, list(range(10,24))))
    listMinute = listTmp + list(map(str, list(range(10,60))))
    
    tmp = list2[0]
    list3.append(listWeek[ord(tmp) - ord('A')])
    tmp = list2[1]
    if(tmp >= '0' and tmp <= '9'):
        list3.append(listHour[ord(tmp) - ord('0')])
    else:
        list3.append(listHour[ord(tmp) - ord('A')+ 9 + 1])
    tmp = list2[2]
    list3.append(listMinute[tmp])

    #print("list3 = ", list3)
    print("%s %s:%s" % tuple(list3))

if(__name__ == "__main__"):
    i = 0
    list1 = []
    while(i < 4):
        list1.append(input())
        i = i + 1
    i = 0
    list2 = []
    for index in range(len(list1[0])):
        tmp = list1[0][index]
        if (tmp >= 'A' and tmp <= 'Z') or (tmp >= 'a' and tmp <= 'z'): 
            if(tmp == list1[1][index]):
                list2.append(tmp)
                i = i + 1
                if(2 == i):
                    break

    for index in range(len(list1[2])):
        tmp = list1[2][index]
        if (tmp >= 'A' and tmp <= 'Z') or (tmp >= 'a' and tmp <= 'z'):
            if(tmp == list1[3][index]):
                list2.append(index)
                break
    
    translate(list2)