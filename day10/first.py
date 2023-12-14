import os, re
from math import ceil



def get_starting_position(star_pos):
    check = [(1, 0), (-1, 0), (0,1), (0,-1)]
    if arr[star_pos[0] - 1][star_pos[1]] in {"F", "|", "7"}: return (star_pos[0]-1, star_pos[1]), "bottom"
    if arr[star_pos[0] + 1][star_pos[1]] in {"L", "|", "J"}: return (star_pos[0]+1, star_pos[1]), "top"
    if arr[star_pos[0]][star_pos[1] + 1] in {"-", "7", "J"}: return (star_pos[0], star_pos[1] + 1), "left"
    if arr[star_pos[0]][star_pos[1] - 1] in {"-", "F", "L"}: return (star_pos[0], star_pos[1] - 1), "right"
    return None, None

def get_position(position, sign, from_where):
    if sign == "|":
        if from_where == "bottom": return (position[0] - 1, position[1]), "bottom"
        return (position[0] + 1, position[1]), "top"
    elif sign == "-":
        if from_where == "left": return (position[0], position[1] + 1), "left"
        return (position[0], position[1] - 1), "right"
    elif sign == "L": 
        if from_where == "top": return (position[0], position[1] + 1), "left"
        return (position[0] - 1, position[1]), "bottom"
    elif sign == "F":
        if from_where == "bottom": return (position[0], position[1] + 1), "left" 
        return (position[0] + 1, position[1]), "top"
    elif sign == "J":
        if from_where == "left": return (position[0] - 1, position[1]), "bottom"
        return (position[0], position[1] - 1), "right"
    elif sign == "7":
        if from_where == "bottom": return (position[0], position[1] - 1), "right"
        return (position[0] + 1, position[1]), "top"
    return None, None


TEST = False 

text_file = "example2.txt" if TEST else "input.txt"

result = 0
starting_position = None
arr = []

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        new_arr = []
        for i, elem in enumerate(line):
            if elem == "S": starting_position = (len(arr), i)
            new_arr.append(elem)
        arr.append(new_arr)

print(starting_position)
print(arr)
position, from_where = get_starting_position(starting_position)
print(position, from_where)
num_of_steps = 0
while True:
    sign = arr[position[0]][position[1]]
    if sign == "S": break
    position, from_where = get_position(position, sign, from_where) 
    print(position, from_where)
    num_of_steps += 1

print("Result:", ceil(num_of_steps / 2))