from typing import List
import random


class Tree:
    name: str
    height: float
    leafs: int

    def __init__(self, name: str, height: float, leafs: int) -> None:
        self.name = name
        self.height = height
        self.leafs = leafs

    def grow_up(self, extraheight: float) -> None:
        self.height += extraheight

    def grow_wide(self, extraleafs) -> None:
        self.leafs += extraleafs

    def show(self) -> None:
        print(f'imię drzewa: {self.name}')
        print(f'wysokość drzewa [m]: {self.height}')
        print(f'liczba liści: {self.leafs}')


li1: List[Tree] = [Tree('Bartek', 30, 300000),
                Tree('Klon', 40, 354000),
                Tree('Dąb', 50, 3300),
                Tree('Jacek', 20, 3200),
                Tree('Placek', 70, 12300)]

for i in range(len(li1)):
    li1[i].show()

for i in range(2):
    li1[random.randint(0, len(li1) - 1)].grow_up(5)

for i in range(len(li1)):
    li1[i].show()
