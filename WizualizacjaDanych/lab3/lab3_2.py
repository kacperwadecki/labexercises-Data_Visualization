from typing import List

li: List[int] = []
pom1: bool = True

while pom1:
    wartosc: int = int(input('Wprowadz wartosc: '))

    for i in li:
        if wartosc == i:
            pom1 = False
    if pom1:
        li.append(wartosc)