import os, re
import numpy as np
from itertools import combinations

TEST = False 
first_task = False

text_file = "example1.txt" if TEST else "input.txt"

result = 0
space = [] 

colums = []
rows = []

galaxies = []

with open(text_file, "r") as f:
    for i, line in enumerate(f):
        line = line.strip() 
        if "#" not in line: rows.append(i)
        tmp = ['' for _ in range(len(line))]
        for j in range(len(line)):
            tmp[j] = line[j]
            if line[j] == "#": galaxies.append((i, j))
        space.append(tmp)
        

space = np.array(space)
print(space[galaxies[0]])
print(space) 
for i in range(len(space[:, 0])):
    if "#" not in space[:, i]: colums.append(i)

def distance(a, b):
    dis = abs(a[0] - b[0]) + abs(a[1] - b[1])
    bigger_universe = 1 if first_task else 999999 
    for c in colums:
        if a[1] > c and b[1] < c: dis += bigger_universe
        elif a[1] < c and b[1] > c: dis += bigger_universe 

    for r in rows:
        if a[0] > r and b[0] < r: dis += bigger_universe 
        elif a[0] < r and b[0] > r: dis += bigger_universe 
    
    return dis

print("Colums without galaxies:", colums)
print("Rows without galaxies:", rows)

combinations = combinations(galaxies, 2)

for first, second in combinations:
    result += distance(first, second)

print("Result:", result)