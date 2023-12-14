import os, re

positions_to_check = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def find_number_at_position(i, j):
    number = arr[i][j]
    old_j = j
    j -= 1
    while j >= 0:
        if arr[i][j].isdigit():
            number = arr[i][j] + number
            j -= 1
            continue
        break
    j = old_j +1
    while j < len(arr[i]):
        if arr[i][j].isdigit():
            number =number + arr[i][j]
            j += 1
            continue
        break
    print(f"Na lokaciji ({i}, {j}) je broj:", number)
    return int(number)

def look_around(i, j):
    global arr
    print("ULAZIM za", arr[i][j])
    for position in positions_to_check:
        new_i = i + position[0]
        new_j = j + position[1]
        if new_i >= len(arr) or new_i < 0:
            continue
        if new_j >= len(arr[i]) or new_j < 0:
            continue
        print(arr[new_i][new_j], "i gledam na poziciji", new_i, new_j)
        if arr[new_i][new_j] != '.' and not arr[new_i][new_j].isdigit(): 
            print("NASO SAM")
            return True
    return False


TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

result = 0

arr = []

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        arr.append(line)

numbers_to_add = [] 
for i in range(len(arr)):
    j = 0
    while j < len(arr[i]):
        print(f"({i}, {j})")
        if arr[i][j].isdigit(): 
            if look_around(i, j):
                numbers_to_add.append((i, j))
                while j < len(arr[i]) and arr[i][j].isdigit(): j += 1
                continue
        j += 1


for number in numbers_to_add:
    result += find_number_at_position(number[0], number[1])

print(result)