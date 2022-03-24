from typing import List, Tuple

class Meeting:
    title: str
    room: str
    duration: int

    def __init__(self, title, room, duration) -> None:
        self.title = title
        self.room = room
        self.duration = duration

    def info(self) -> str:
        return f'Spotkanie: {self.title} odbedzie sie w {self.room} i bedzie trwalo {self.duration}'

    def __add__(self, other) -> List[any]:
        list1: [any] = [self.title, other.room, self.duration + other.duration]
        return list1


object1: Meeting = Meeting('Gowno', 'burza', 30)
object2: Meeting = Meeting('Gowno2', 'burza2', 20)

object3: List[any] = object1 + object2
print(object3)