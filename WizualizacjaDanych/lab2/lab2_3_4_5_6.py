import cmath
import math

n: int = int(input('Wprowadź numer zadania: '))

if n == 3:
    c = cmath.sqrt(-1)
    print(c)
    print(c.imag)
    print(c.real)
elif n == 4:
    print(math.sin(15), math.sin(30), math.sin(45), math.sin(60))
    print(math.cos(15), math.cos(30), math.cos(45), math.cos(60))
    print(math.tan(15), math.tan(30), math.tan(45), math.tan(60))
    print(1 / math.tan(15), 1 / math.tan(30), 1 / math.tan(45), 1 / math.tan(60))
elif n == 5:
    r: float = float(input('Wprowadź promień koła: '))
    obw: float = 2 * math.pi * r
    pole: float = math.pi * r ** 2
    print(f'Obwód wynosi:{obw} Pole wynosi:{pole}')
elif n == 6:
    r: float = float(input('Wprowadź promień kuli: '))
    pole: float = 4 * math.pi * r * r
    obj: float = 4 / 3 * math.pi * r ** 3
    print(f'Pole wynosi:{pole} Objętość wynosi:{obj}')