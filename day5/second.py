import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

result = 0

seeds = []
arr = []
help_arr = []

with open(text_file, "r") as f:
    for i, line in enumerate(f):
        line = line.strip() 
        if i == 0:
            unpro_seeds = line.split(":")[1]
            for seed in unpro_seeds.split(" "):
                if seed == "": continue
                seeds.append(int(seed))
        elif len(line) == 0:
            if len(help_arr) > 0: arr.append(help_arr[1:])
            help_arr.clear()
        else:
            help_arr.append([int(x) for x in line.split(" ") if x.isdigit()])

    if len(help_arr) > 0: arr.append(help_arr[1:])
    help_arr.clear()

locations = []
def get_seeds(seeds):
    for i in range(len(seeds)):
        print(i)
        if i % 2 == 0:
            yield seeds[i]
        else:
            for j in range(1, seeds[i]):
                yield seeds[i-1] + j 


def inside(range, next_stage):
    if range[1] <= next_stage and range[1] + range[2] >= next_stage:
        shift = next_stage - range[1] 
        return range[0] + shift
    return -1

def get_next_value(con, next_stage):
    for c in con:
        where = inside(c, next_stage)
        if where != -1: return where
    return next_stage

import math
result = math.inf
for seed in get_seeds(seeds):
    next_stage = seed
    for conversion in arr:
        next_stage = get_next_value(conversion, next_stage)
    result = min(result, next_stage)

print("Result is:", result)
