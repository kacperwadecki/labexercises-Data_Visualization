from typing import List


def typing(*args: any) -> List[List[any]]:
    li1: List = []
    result: List = []
    tmp: int = 0
    for i in range(len(args[0])):
        li1.append(type(args[0][i]))
    li1 = list(set(li1))

    for j in li1:  # typy
        result.append([])
        for k in args[0]:  # wartosci
            if type(k) == j:
                result[tmp].append(k)
        tmp += 1
    return result


li: List = ['lol', 3, 4.5, 3, 'sr', False, 5]

print(typing(li))
