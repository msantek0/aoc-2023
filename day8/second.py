import os, re

TEST = False 

text_file = "example3.txt" if TEST else "input.txt"

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

def its_not_over(starting):
    for node in starting:
        if node[2] != 'Z': return True
    return False

print(nodes)
start_nodes = [node for node in nodes if node[2] == 'A']
print(start_nodes) 
num_of_steps = 0
moving_index = 0
while its_not_over(start_nodes):
    if num_of_steps % 10000 == 0: print(num_of_steps)
    if moving_index == len(moving): moving_index = 0
    move = 1 if moving[moving_index] == 'R' else 0
    for i in range(len(start_nodes)):
        start_nodes[i] = nodes[start_nodes[i]][move]
    moving_index += 1
    num_of_steps += 1

print(num_of_steps)
