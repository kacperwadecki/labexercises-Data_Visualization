import math


def euklides(x0: float, y0: float, x1: float, y1: float) -> float:
    return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


x0: float = float(input('Wprowadz x0: '))
y0: float = float(input('Wprowadz y0: '))
x1: float = float(input('Wprowadz x1: '))
y1: float = float(input('Wprowadz y1: '))

print(euklides(x0, y0, x1, y1))
