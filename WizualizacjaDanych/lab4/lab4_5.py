from typing import List


def max_(x: List) -> str:
    tmp1: int = len(x[0])
    tmp2: str = x[0]

    for element in x:
        if tmp1 < len(element):
            tmp1 = len(element)
            tmp2 = element
    return tmp2


li: List[str] = ['jeden', 'dwa', 'piec milionow', 'trzy', 'cztery']

print(max_(li))