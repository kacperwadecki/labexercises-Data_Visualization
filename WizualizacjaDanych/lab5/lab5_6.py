from typing import List


class Time:
    hours: int = 10
    minutes: int = 30

    def __init__(self, hours: int, minutes: int) -> None:
        self. hours = hours
        self. minutes = minutes

    def add_time(self, hours: int, minutes: int) -> None:
        self.hours += hours
        self.minutes += minutes

    def display(self) -> tuple[int, int]:
        return self.hours, self.minutes


czas: Time = Time(10,30)
print(czas.hours)

czas.add_time(2, 20)
print(czas.display())