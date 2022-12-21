import time
import numpy as np

# t0 = time.time()
# l1 = ""
#
# with open("input.txt", "r") as f:
#     """
#     """
#     l1 = f.readline()
#     totval = 0
#     while l1 != "":
#         groups = l1.split(",")
#         A = list(map(int, groups[0].split("-")))
#         B = list(map(int, groups[1].split("-")))
#         l1 = f.readline()
#         a0b0 = (A[0] - B[0])
#         a1b1 = (A[1] - B[1])
#
#         if (a0b0 >= 0 and a1b1 <= 0) or (a0b0 <= 0 and a1b1 >= 0):
#             totval += 1
#
# t1 = time.time() - t0
# print(f"Part 1: {totval} assignments fully contains the other ")
# print(f"This took {t1:.4f} seconds to calculate")

t0 = time.time()

with open("input.txt", "r") as f:
    """
    """
    l1 = f.readline()
    totval = 0
    while l1 != "":
        groups = l1.split(",")

        A = list(map(int, groups[0].split("-")))
        B = list(map(int, groups[1].split("-")))

        a1b0 = (A[1] - B[0])
        a0b1 = (A[0] - B[1])

        if (a1b0 >= 0 and a0b1 <= 0) or (a0b1 <= 0 and a1b0 >= 0) :
            totval += 1

        print(f"in:{l1}groups:{groups}\tA:{A}\tB:{B}\ta1b0:{a1b0}\ta0b1:{a0b1}\tOVERLAP:{(a1b0 >= 0 and a0b1 < 0) or (a0b1 <= 0 and a1b0 > 0) }")
        l1 = f.readline()
t1 = time.time() - t0
print(f"Part 1: {totval} assignments partially contains the other ")
print(f"This took {t1:.4f} seconds to calculate")
