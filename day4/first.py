import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

result = 0

with open(text_file, "r") as f:
    for i, line in enumerate(f):
        line = line.strip() 
        winning, mine = line.split("|")
        winning = winning.split(":")[1]
        win_set = set()
        me_set = set()
        for w in winning.split(" "):
            if w == "": continue
            win_set.add(int(w.strip()))
        for m in mine.split(" "):
            if m == "": continue
            me_set.add(int(m.strip()))
        how_much = len(win_set.intersection(me_set)) - 1 
        if how_much == -1: continue
        result += 2 ** how_much

print("Result:", result)