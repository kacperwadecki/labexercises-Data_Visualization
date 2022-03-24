import math


class Circle:
    r: float = 0

    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return math.pi * self.r ** 2

    def __sub__(self, other) -> float:
        return self.area() - other.area()


class Square:
    side: float = 0

    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2

    def __sub__(self, other) -> float:
        return self.area() - other.area()


object1: Circle = Circle(3)
object2: Square = Square(7)

object3: Circle = Circle(5)
object4: Square = Square(3)

print(object1.area())
print(object2.area())
print(object2 - object1)
print(object3 - object4)
