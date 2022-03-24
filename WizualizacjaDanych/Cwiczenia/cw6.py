import linecache
import random
from typing import List


list1: List[int] = []

for i in range(30):
    list1.append(random.randint(0, 30))

open('text.txt', 'w').write(str(list1))
print(open('text.txt', 'r').readline())