#! /usr/bin/env python3

if(__name__ == "__main__"):
    s1 = input()
    s2 = input()
    N,M = list(map(int, s1.split(' ')))
    list2 = list(map(int, s2.split(' ')))

    #需要考虑一种特殊情况: N < M
    while N-M < 0:
        M = M-N

    listResult = []
    for i in range(N):
        pos = (i-M+N) % N
        value = list2[pos]
        listResult.append(str(value))
    print(' '.join(listResult))