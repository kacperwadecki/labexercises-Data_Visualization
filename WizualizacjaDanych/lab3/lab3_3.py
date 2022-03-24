from typing import List

li: List[int] = []

n: int = int(input('Wprowadz rozmiar: '))

tmp1: int = 1
tmp2: int = 0
tmp3: int = 0

for j in range(n):
    if tmp1 == 1:
        li.append([tmp1])
        tmp1 = 0
        for k in range(n-1):
            li[j].append(tmp1)
    else:
        li.append([tmp1])
        for k in range(n-1):
            if tmp2 == tmp3:
                li[j].append(1)
            else:
                li[j].append(0)
            tmp2 += 1

        tmp2 = 0
        tmp3 += 1

for elements in li:
    print(elements)