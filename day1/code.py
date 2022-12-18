import time
import numpy as np

t0  =time.time()
elfs = []
line =" "
with open("input.txt","r") as f:
    elfsumsum = 0
    while line != "":
        line = f.readline()
        if line != "":
            if line != "\n":
                elfsumsum += int(line)
            else:
                elfs.append(elfsumsum)
                elfsumsum = 0

elfno =elfs.index(max(elfs))
t1 = time.time()-t0
print("Elf no %d carries the most calories with %d calories"%(elfno,elfs[elfno]))
print("This took %.6f seconds to calculate" % (t1))

t0  =time.time()
elfs = []
line =" "
with open("input.txt","r") as f:
    elfsumsum = 0
    while line != "":
        line = f.readline()
        if line != "":
            if line != "\n":
                elfsumsum += int(line)
            else:
                elfs.append(elfsumsum)
                elfsumsum = 0

elfs = sorted(elfs)
elfsum = np.sum(elfs[-3:])
t1 = time.time()-t0
print("Top three elves carries %d"%(elfsum))
print("This took %.6f seconds to calculate" % (t1))
