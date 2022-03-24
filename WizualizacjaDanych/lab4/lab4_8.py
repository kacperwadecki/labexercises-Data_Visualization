from typing import List


def parzystosc(li: List) -> list:
    even: List = []
    odd: List = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]


print(parzystosc([1, 2, 3, 4, 5, 6, 7]))


