from typing import List

li: List[List[int]] = [[], [], [], []]

# tmp: int = 0
#
# for i in range(4):
#     for j in range(4):
#         if tmp % 5 != 0:
#             li[j].append(tmp)
#             tmp += 1
#         else:
#             li[j].append(0)
#             tmp += 1

# j: int = 0
#
# for i in range(16):
#     if tmp % 5 != 0:
#         li[j].append(tmp)
#         tmp += 1
#         j += 1
#     else:
#         li[j].append(0)
#         tmp += 1
#         j += 1
#     if j == 4:
#         j = 0

for k in li:
    print(k)

