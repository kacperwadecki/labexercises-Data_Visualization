from typing import Set

s: Set[int] = set()

while len(s) < 10:
    wartosc: int = int(input('Wprowadz wartosc do zbioru: '))
    s.add(wartosc)
    print(len(s))
