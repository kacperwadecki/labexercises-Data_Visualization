import math


class Ball:

    r: float
    color: str

    def __init__(self, r: float, color: str) -> None:
        self.r = r
        self.color = color

    def area(self) -> float:
        return 4 * math.pi * self.r ** 2

    def volume(self) -> float:
        return 4 / 3 * math.pi * self.r ** 3

    def set_color(self, color: str) -> None:
        print(f'Zmieniles kolor na: {color} :)')
        self.color = color


