from typing import List, Iterator


class Suma:

    def __init__(self, lista: List[int]) -> None:
        self.lista = lista
        self.suma = 0
        self.indeks = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        self.suma += self.lista[self.indeks]
        self.indeks += 1

        if self.indeks > len(self.lista):
            raise StopIteration

        return self.suma


object: Suma = Suma([1, 2, 3, 4, 5, 6 ,7])
iterator: Iterator = iter(object)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))