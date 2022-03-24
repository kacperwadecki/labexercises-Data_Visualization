from typing import Iterator


class Parzyste:

    def __init__(self, **kwargs: str) -> None:
        self.kwargs = kwargs

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> str:
        for i in self.kwargs:
            if ord(self.kwargs[i][0]) % 2 == 0:
                biszkopt: str = self.kwargs[i]
                del self.kwargs[i]
                return biszkopt


object: Parzyste = Parzyste(a='abc', b='bbc', c='cbd', d='dee', e='e')
iterator: Iterator = iter(object)
print(next(iterator))
print(next(iterator))
