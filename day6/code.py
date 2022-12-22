import time
import re
import timeit
t0 = time.time()
p_size = 4
with open("input.txt", "r") as f:
    """
    """
    line = f.readline()
    non_repeat = False
    for i in range(len(line)-p_size):
        group = line[i:i+p_size]
        if line[i] not in line[i+1:i+p_size]:
            non_repeat = True
            for j,char in enumerate(group):
                if char in group[:j]+group[j + 1:]:
                    non_repeat = False
                    break

        if non_repeat == True:
            break


t1 = time.time() - t0
print(f"First non repeating {p_size} cahracters is at position {i+p_size}, consisting of characters '{line[i:i+p_size]}'")
print(f"This took {t1:.10f} seconds to calculate")
