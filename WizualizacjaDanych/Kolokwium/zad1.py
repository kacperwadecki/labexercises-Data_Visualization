def number_format(number: int, mask: str) -> str:
    tmp1: str = str(number)
    result: str = ''
    tmp2: int = 0
    tmp3: int = 0

    for i in mask:
        if mask[tmp2] == '#':
            result += tmp1[tmp3]
            tmp3 += 1
            tmp2 += 1
        else:
            result += mask[tmp2]
            tmp2 += 1

    return result


print(number_format(1234567, '##,##,###'))
