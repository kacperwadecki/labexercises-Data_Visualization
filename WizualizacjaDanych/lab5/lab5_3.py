from lab5_1 import Square
from lab5_2 import Traingle
from typing import List
import random

li1: List[Square] = []
li2: List[Traingle] = []


for i in range(10):
    square: Square = Square(random.randint(11, 20))
    li1.append(square)
    print(square.area())
    print(square.perimeter())

for i in range(25):
    traingle: Traingle = Traingle(random.randint(6, 10), random.randint(15, 19))
    li2.append(traingle)
    print(traingle.perimeter())
    print(traingle.area())
