import time
import re
import numpy as np
import timeit
t0 = time.time()

with open("input.txt", "r") as f:
    """
    """
    rows = 8
    cols = 9
    maxstack = 100
    containers = []
    for x in range(cols):
        containers.append([])

    containers = np.zeros(shape=(cols, maxstack),dtype=int)

    #turn strings into array
    string_arr = []
    for i in range(rows):
        string_arr.append(f.readline())
    key = f.readline()

    colarr = []
    for i in range(cols):
        colarr.append(key.find(str(i+1)))

    for row_no, row in enumerate(string_arr[::-1]):
        stack = np.array([])
        for col_no,col in enumerate(colarr):
            char = row[col]
            if char != " ":
                containers[col_no][row_no+1]=ord(char)
                containers[col_no][0]+=1

    line = f.readline() # Throw away blank line
    line = f.readline()
    while line != "":

        m = np.array([int(s) for s in re.findall(r'\d+',line)])
        m[1:3] = m[1:3]-1
        num_containers = m[0]
        from_pos = m[1]
        to_pos = m[2]

        containers[to_pos][containers[to_pos][0]+1:containers[to_pos][0]+num_containers+1] =\
            containers[from_pos][containers[from_pos][0]-num_containers+1:containers[from_pos][0]+1]
        containers[from_pos][containers[from_pos][0]-num_containers+1:containers[from_pos][0]+1] = 0
        containers[to_pos][0]+=num_containers
        containers[from_pos][0]-=num_containers

        line = f.readline()
    outstring = ""

    for stacks in containers:
        outstring+=chr(stacks[int(stacks[0])])

t1 = time.time() - t0
print(f"Part 1: Topmost row is {outstring} ")
print(f"This took {t1:.6f} seconds to calculate")
