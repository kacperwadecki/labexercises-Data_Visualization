from typing import List


class Matrix:
    def __init__(self, *args: List, value2=4) -> None:
        self.value2 = value2
        self.args = args

    def transpose(self) -> List[List[int]]:
        li1: List[List[int]] = []

        for i in range(len(self.args[0])):
            li1.append([])

        for j in range(len(self.args[0])):
            for i in range(len(self.args[0])):
                li1[i].append(self.args[j][i])

        return li1

    def size(self) -> str:
        return f'Ilosc wierszy = {len(self.args)}, Ilosc kolumn = {len(self.args[0])}'

    def set_value(self, x: int, y: int, value: int) -> List[List[int]]:
        self.args[x][y] = value
        return list(self.args)

    def get_value(self, x: int, y: int) -> int:
        return self.args[x][y]

    def is_identiti(self) -> bool:
        tmp: bool = True

        for i in range(len(self.args)):
            for j in range(len(self.args)):

                if self.args[i][j] != 1 and i == j:
                    tmp = False
                elif self.args[i][j] != 0 and i != j:
                    tmp = False

        return tmp


object1: Matrix = Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1])
object2: Matrix = Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1])

