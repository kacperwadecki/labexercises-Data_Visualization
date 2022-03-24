from typing import Generator
from cw3 import Ball


def gen(color: str) -> Generator[Ball, None, None]:
    tmp: int = 0
    n: int = 1
    while True:
        n += 1
        for i in range(n + 1):
            if n % (i + 1) == 0:
                tmp += 1
        if tmp > 2:
            tmp = 0
        else:
            tmp = 0
            x: Ball = Ball(n, color)
            yield x


generator: Generator[Ball, None, None] = gen('red')
a: Ball = next(generator)
print(a.area())