from typing import List


def min_(x: List) -> int:
    tmp: int = x[0]
    for element in x:
        if tmp > element:
            tmp = element

    return tmp


li: List[int] = [5, 4, 1, -2, 2]

print(min_(li))