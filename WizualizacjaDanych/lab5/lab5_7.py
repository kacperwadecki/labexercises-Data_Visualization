from typing import Iterator


class LiczbyPierwsze:
    def __init__(self) -> None:
        self.i: int = 1
        self.tmp: int = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        self.i += 1
        while True:
            for j in range(self.i + 1):
                if self.i % (j + 1) == 0:
                    self.tmp += 1

            if self.tmp > 2:
                self.tmp = 0
                self.i += 1
            else:
                self.tmp = 0
                return self.i


object: LiczbyPierwsze = LiczbyPierwsze()
iterator: Iterator = iter(object)



