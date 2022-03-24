import math

print('ax^2 + bx + c = 0')
a: float = float(input('a = '))
b: float = float(input('b = '))
c: float = float(input('c = '))

if a != 0:
    delta: float = (b * b) - (4 * a * c)
    if delta > 0:
        x1: float = (-b + math.sqrt(delta)) / (2 * a)
        x2: float = (-b - math.sqrt(delta)) / (2 * a)
        print(f'Miejsca zerowe to x1 = {x1} i x2 = {x2}  ')
    elif delta == 0:
        x1: float = (-b / (2 * a))
        print(f'Miejsce zerowe to x1 = {x1}')
    else:
        print('nie ma rozwiązań w zbiorze liczb rzeczywistych')
else:
    print('Nie jest to równanie kwadratowe!')