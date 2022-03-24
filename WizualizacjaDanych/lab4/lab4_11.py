from typing import Generator


def gen(x: int) -> Generator[int, None, None]:
    while True:
        if x % 2 == 0:
            yield x
        x += 1


generator: Generator[int, None, None] = gen(5)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))