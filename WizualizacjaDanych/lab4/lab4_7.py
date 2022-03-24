def wazona(** kwargs: float) -> float:
    den: float = 0
    cou: float = 0
    list1: list = list(kwargs.values())

    for i in range(0, len(list1), 2):
        den += list1[i] * list1[i+1]
        cou += list1[i+1]
    return den / cou


print(wazona(v0=2, w0=1, v1=6, w1=1))
