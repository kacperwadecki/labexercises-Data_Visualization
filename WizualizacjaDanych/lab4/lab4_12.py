from typing import Generator


def arytmetyczny(a1: int, r: int) -> Generator[int, None, None]:
    while True:
        a1 += r
        yield a1

generator: Generator[int, None, None] = arytmetyczny(1, 2)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))