from typing import List, Iterator


class Menu:
    name: str
    dishes: List[str] = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.dishes = []

    def count(self) -> int:
        return len(self.dishes)

    def add(self, dish: str) -> None:
        flaga: bool = True
        for i in self.dishes:
            if i == dish:
                print('Te danie juz sie znajduje na liscie')
                flaga = False

        if flaga:
            self.dishes.append(dish)

    def our_dishes(self, x: dishes) -> List[str]:
        list2: List[str] = self.dishes
        for i in x.dishes:
            for j in self.dishes:
                if i == j:
                    list2.remove(i)

        return list2


object: Menu = Menu('JEC')
object.add('kurczak')
object.add('golab')
object.add('abc')
object.add('def')
object.add('losos')

object2: Menu = Menu('JAK')
object2.add('kurczak')
object2.add('lol')
object2.add('golab')
object2.add('def')
object2.add('abc')
object2.add('cx')
object2.add('zxzx')

print(object2.our_dishes(object))
