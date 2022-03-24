class Square:
    a: float

    def __init__(self, a: float) -> None:
        self.a = a

    def perimeter(self) -> float:
        return 4 * self.a

    def area(self) -> float:
        return self.a ** 2


# square1: Square = Square(5)
# print(square1.area())
