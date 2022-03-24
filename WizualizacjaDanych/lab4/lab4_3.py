import math


def zero(a: int, b: int, c: int) -> any:
    if a != 0:
        delta: float = b ** 2 - 4 * a * c
        if delta > 0:
            x1: float = (-b + math.sqrt(delta))/2 * a
            x2: float = (-b - math.sqrt(delta))/2 * a
            return x1, x2
        elif delta == 0:
            x1: float = -b / (2*a)
            return x1
        else:
            return 'Funkcja nie ma miejsc zerowych'
    else:
        return 'To nie jest funkcja kwadratowa'


a: int = int(input('Wprowadz a: '))
b: int = int(input('Wprowadz b: '))
c: int = int(input('Wprowadz c: '))

print(zero(a, b, c))