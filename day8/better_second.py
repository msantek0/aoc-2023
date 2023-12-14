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
all_importat = []
for start_node in start_nodes:
    print("Starting with node", start_node)
    endings = []
    num_of_steps = 1
    moving_index = 0
    move = 1 if moving[moving_index] == 'R' else 0
    where_going = nodes[start_node][move]
    wisited = [(start_node, where_going)]
    moving_index += 1
    while True:
        if moving_index == len(moving): moving_index = 0
        move = 1 if moving[moving_index] == 'R' else 0
        start_node = where_going
        where_going = nodes[start_node][move]
        if start_node[2] == 'Z': 
            endings.append(num_of_steps)
            break
        if (start_node, where_going) in wisited: break
        wisited.append(start_node)
        moving_index += 1
        num_of_steps += 1
    all_importat.append(endings)

print(all_importat)
result = 1
for item in all_importat:
    result *= item[0]

print("Result", result)