from typing import Generator, List


def gen(x: List, n: int) -> Generator[List, None, None]:
    li1: List[List[int]] = []
    count1: int = 0
    count2: int = 0
    tmp: int = int(len(x) / n)
    tmp1: int = len(x) - (tmp * n)  # reszta pileczek
    for i in range(n):
        li1.append([])
    for j in x:
        li1[count1].append(j)
        if (count2 + 1) % (int(len(x) / n)) == 0 and count2 < len(x) - tmp1 - 1:
            yield li1[count1]
            count1 += 1  # do ktorej szufladki

        count2 += 1  # ktory wyraz
    yield li1[-1]


li: List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
generator: Generator[List, None, None] = gen(li, 5)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
