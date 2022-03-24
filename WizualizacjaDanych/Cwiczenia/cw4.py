from typing import List


class Vector:
    data: List[any] = []

    def __init__(self, *args: [any]) -> None:
        self.args = args
        self.data = list(args)

    def len(self) -> int:
        return len(self.data)

    def get_value(self, indeks: int) -> any:
        return self.data[indeks]

    def set_value(self, new: any) -> None:
        self.data.insert(0, new)

    def __mul__(self, other) -> float:
        for i in range(len(self.data)):
            if not str(self.data[i]).isnumeric():
                self.data[i] = 0

        for i in range(len(other.data)):
            if not str(other.data[i]).isnumeric():
                other.data[i] = 0

        result: float = 0
        for i in range(len(self.data)):
            result += (self.data[i] * other.data[i])
        return result


object1: Vector = Vector(1, 2, 3)
object2: Vector = Vector(2, 'h', 4)
object3: Vector = Vector(2, 'h', 4)
object4: Vector = Vector(2, 'h', 4)

# print(object1.len())
# print(object1.get_value(1))
# object1.set_value(2)
# print(object1.get_value(0))
# print(object1.data)

object5: float = object1 * object2

print(object5)
