from typing import Generator


def gen(*args: any) -> Generator[any, None, None]:
    i: int = 0
    while True:
        if i == len(args) - 1:
            yield args[i]
            i += 1

        elif len(args) > i:
            n: float = args[i]
            if str(n).isnumeric():
                result: float = n ** (n+1)
                yield result
            i += 1

        else:
            yield 'Skonczyly sie'


generator: Generator[any, None, None] = gen(1, 2, 'trzy', 4, 5, 6)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))




