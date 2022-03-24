from typing import Generator


def pierwsze() -> Generator[int, None, None]:
    i: int = 3
    counter: int = 0
    while True:
        for j in range(i):
            if i % (j + 1) == 0:
                counter += 1
        if counter < 3:
            yield i
        counter = 0
        i += 1



generator: Generator[int, None, None] = pierwsze()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))