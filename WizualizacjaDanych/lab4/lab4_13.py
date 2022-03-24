from typing import Generator


def fib() -> Generator[int, None, None]:
    a1: int = 1
    a2: int = 1
    a3: int = 0
    while True:
        yield a1
        a3 = a1 + a2
        a1 = a2
        a2 = a3


generator: Generator[int, None, None] = fib()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))