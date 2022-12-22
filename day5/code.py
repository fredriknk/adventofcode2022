import time
import re
import timeit
t0 = time.time()

with open("input.txt", "r") as f:
    """
    """
    rows = 8
    cols = 9

    containers = []
    for x in range(cols):
        containers.append([])
    #turn strings into array
    string_arr = []
    for i in range(rows):
        string_arr.append(f.readline())
    key = f.readline()
    colarr = []
    for i in range(cols):
        colarr.append(key.find(str(i+1)))

    for row in string_arr[::-1]:
        for col_no,col in enumerate(colarr):
            char = row[col]
            if char != " ":
                containers[col_no].append(char)

    line = f.readline() # Throw away blank line
    line = f.readline()
    while line != "":
        m = [int(s) for s in re.findall(r'\d+',line)]
        m[1] -= 1
        m[2] -= 1
        move_array = containers[m[1]]
        for j in range(m[0]):
            containers[m[2]].append(containers[m[1]].pop(-1))

        line = f.readline()
    outstring = ""
    for stacks in containers:
        outstring+=stacks[-1]

t1 = time.time() - t0
print(f"Part 1: Topmost row is {outstring} ")
print(f"This took {t1:.4f} seconds to calculate")
