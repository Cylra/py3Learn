#! /usr/bin/python3

def triangles():
    L1 = [1]
    while True:
        #print(L1)
        yield L1
        L2 = tuple(L1)
        L1.append(1)
        n = len(L1)
        if n > 2:
            for i in list(range(1, n-1)):
                L1[i] = L2[i-1] + L2[i]

n = 0
z = triangles()
for i in z:
    print(i)
    n = n + 1
    if 10 == n:
        break
print('done')