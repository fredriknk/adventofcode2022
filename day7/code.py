##FIX
import time
import re
import timeit
t0 = time.time()
FO = "FOLDER"
FI = "FILE"
class folder(object):
    def __init__(self,name=None, type=None, owner = None, weight = None):
        self.name=name
        self.type=type
        self.folders=[]
        self.files=[]
        self.weight = weight
        self.owner = owner

    def add_object(self,name):
        self.folder.append(name)

    def command(self,command):
        if "cd " in command:
            cwd = re.findall(r'cd (.*)', line)[0]
            if cwd != "..":
                if cwd not in self.folders:
                    self.add_child(cwd,type=FO,owner=self.name)
        if "dir " in command:
            folder_name = re.findall(r'dir (.*)', line)[0]






with open("input.txt", "r") as f:
    """
    """
    fs = {"/":{}}
    line = " "
    cwd = ""

    while line !=  "":
        line = f.readline()
        print(f"command: {line[:-1]}")

        if "$ cd" in line:
            cwd = re.findall(r'cd (.*)', line)[0]
            print(f"changed CWD to {cwd}")
        elif "$ ls" in line:
            print("Turn on lsdir")
            LS_DIRS = True
        elif "dir " in line:
            diradd = re.findall(r'dir (.*)', line)[0]
            fs[cwd][diradd] = {}


t1 = time.time() - t0
print(f"'")
print(f"This took {t1:.10f} seconds to calculate")
