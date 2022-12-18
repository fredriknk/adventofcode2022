import time
import numpy as np
t0 = time.time()
line = " "
with open("input.txt","r") as f:
    """
    A = ROCK    = X
    B = PAPER   = Y
    C = SCISSOR = Z
    
    """
    key = { "A X": 3,
            "A Y": 6,
            "A Z": 0,
            "B X": 0,
            "B Y": 3,
            "B Z": 6,
            "C X": 6,
            "C Y": 0,
            "C Z": 3}

    RPSsum = 0
    while line != "":
        line = f.readline()
        if line != "":
            RPSsum+=key[line[:-1]]
            if "X" in line:
                RPSsum += 1
            if "Y" in line:
                RPSsum += 2
            if "Z" in line:
                RPSsum += 3


t1 = time.time()-t0
print("Part 1: Competition sum is %d"%(RPSsum))
print("This took %.6f seconds to calculate" % (t1))

t0 = time.time()
line = " "
with open("input.txt", "r") as f:
    """
    A = ROCK    = 1
    B = PAPER   = 2
    C = SCISSOR = 3
    
    X = LOOSE   = 0
    Y = DRAW    = 3
    Z = WIN     = 6
    """
    key = {"A X": 0+3,  #Loose SCISSOR
           "A Y": 3+1,  #Draw  ROCK
           "A Z": 6+2,  #WIN   PAPER
           "B X": 0+1,  #Loose
           "B Y": 3+2,  #Draw
           "B Z": 6+3,  #WIN
           "C X": 0+2,  #Loose
           "C Y": 3+3,  #Draw
           "C Z": 6+1  #WIN
           }

    RPSsum = 0
    while line != "":
        line = f.readline()
        if line != "":
            RPSsum += key[line[:-1]]


t1 = time.time() - t0
print("Competition sum is %d" % (RPSsum))
print("This took %.6f seconds to calculate" % (t1))
