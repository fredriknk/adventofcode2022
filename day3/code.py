import time
import numpy as np
t0 = time.time()
line = " "
#
#
# with open("input.txt","r") as f:
#     """
#     """
#     totval = 0
#     ba = ord("a")-1
#     bA = ord("A")-1
#     while line != "":
#         line = f.readline()
#         line =line[:-1]
#         split = int((len(line))/2)
#         l1 = line[:split]
#         l2 = line[split:]
#         charval = 0
#         if line != "":
#             for a in l1:
#                 for b in l2:
#                     if a == b:
#                         value = ord(a)
#                         if value<ba:
#                             charval = value - bA + 26
#                         else:
#                             charval = value - ba
#                         break
#                 if a == b:
#                     break
#             totval += charval
#
# t1 = time.time()-t0
# print("Part 1 Total sum of priority values are %d"%(totval))
# print("This took %.6f seconds to calculate" % (t1))


t0 = time.time()
l3 = " "


with open("input.txt","r") as f:
    """
    """
    totval = 0
    ba = ord("a")-1
    bA = ord("A")-1
    while l3 != "":
        l1 = f.readline()
        l2 = f.readline()
        l3 = f.readline()
        charval = 0
        found = False
        if line != "":
            for a in l1:
                for b in l2:
                    for c in l3:
                        if a == b and b == c:
                            value = ord(a)
                            found = True
                            if value<ba:
                                charval = value - bA + 26
                            else:
                                charval = value - ba
                            break
                    if found:
                        break
                if found:
                    break
        totval += charval

t1 = time.time()-t0
print("Part 2 Total sum of priority values are %d"%(totval))
print("This took %.6f seconds to calculate" % (t1))