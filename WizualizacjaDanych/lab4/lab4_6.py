def arytmetyczna(*args: float) -> float:
    suma: float = 0
    for i in args:
        suma += i
    return suma / len(args)


print(arytmetyczna(2, 3, 4))
