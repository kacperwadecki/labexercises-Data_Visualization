class Traingle:
    side: float
    base: float

    def __init__(self, side, base) -> None:
        self.side = side
        self.base = base

    def perimeter(self) -> float:
        return self.base + 2 * self.side

    def area(self) -> float:
        p: float = self.perimeter() / 2
        return (p * (p - self.base) * (p - self.side) * (p - self.side)) ** (1/2)


# traingle: Traingle = Traingle(13, 10)
# print(traingle.perimeter())
# print(traingle.area())

