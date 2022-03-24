import math

x: float = float(input('Wprowadź x:'))
y: float = float(input('Wprowadź y:'))
z: float = float(input('Wprowadź z:'))

n: int = int(input('Wprowadź numer przykładu'))

if n == 1:
    result: float = (x + y / z) ** (x - z)
elif n == 2:
    result: float = (math.sqrt(x) - x ** (1 / z)) / ((x ** 1 / z) - math.sqrt(x))
elif n == 3:
    result: float = (math.pi / x) - math.atan(y)
elif n == 4:
    result: float = ((x ** 1 / 3 - y) ** math.pi) / ((z ** y) / (math.e ** 10))
elif n == 5:
    result: float = (math.sin(x) + math.cos(y)) / (math.sin(x) + math.cos(y))
elif n == 6:
    result: float = math.log(x, y)

print(f'Dla x={x}, y={y}, z={z} wartość wyrażenia z przykładu {n} wynosi: {result}')