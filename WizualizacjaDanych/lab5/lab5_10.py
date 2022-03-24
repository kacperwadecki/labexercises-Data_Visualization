from typing import List, Iterator


class Iloczyn:

    def __init__(self, list1: List[int], list2: List[int] ) -> None:
        self.list1 = list1
        self.list2 = list2
        self.result: int = 0
        self.i = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        i = self.i
        while True:
            self.result += self.list1[i] * self.list2[i]
            self.i += 1
            return self.result


object: Iloczyn = Iloczyn([1, 2, 3], [2, 3, 4])
iterator: Iterator = iter(object)

print(next(iterator))
print(next(iterator))
print(next(iterator))