import os, re

TEST = False 

text_file = "example2.txt" if TEST else "input.txt"

result = 0
moving = ""
nodes = dict()

with open(text_file, "r") as f:
    for i, line in enumerate(f):
        line = line.strip() 
        if i == 0: moving = line
        if i > 1:
            start, location = line.split(" = ")
            left_location, right_location = location.split(", ")
            nodes[start] = (left_location[1:], right_location[:-1])

print(nodes)
start_node = 'AAA'
num_of_steps = 0
moving_index = 0
while start_node != 'ZZZ':
    if moving_index == len(moving): moving_index = 0
    move = 1 if moving[moving_index] == 'R' else 0
    start_node = nodes[start_node][move]
    moving_index += 1
    num_of_steps += 1

print(num_of_steps)
