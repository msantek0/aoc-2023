import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"
len_arr = 6 if TEST else 219
result = 0

scratch_card_number = [1 for _ in range(len_arr)]

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
        how_much = len(win_set.intersection(me_set))
        for index in range(how_much):
            scratch_card_number[index + i + 1] += 1 * scratch_card_number[i]
print("Result", sum(scratch_card_number))