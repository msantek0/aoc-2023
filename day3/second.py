import os, re

TEST = False 

positions_to_check = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

text_file = "example1.txt" if TEST else "input.txt"

result = 0

all_numbers = []
all_stars = []
arr = []
line_number = -1

with open(text_file, "r") as f:
    for line in f:
        line_number += 1
        line = line.strip() 
        arr.append(line)
        active_index = 0
        while active_index < len(line):
            if line[active_index].isdigit():
                number = line[active_index]
                start = active_index
                active_index += 1
                while active_index < len(line) and line[active_index].isdigit():
                    number += line[active_index]
                    active_index += 1
                end = active_index - 1
                all_numbers.append((number, (start, end, line_number)))
            if active_index < len(line) and line[active_index] == "*":
                all_stars.append((line_number, active_index))
            active_index += 1
    

def close(star, number): 
    global arr
    for position in positions_to_check:
        new_i = star[0] + position[0]
        new_j = star[1] + position[1]
        if new_i >= len(arr) or new_i < 0:
            continue
        if new_j >= len(arr[star[0]]) or new_j < 0:
            continue
        if new_i == number[1][2] and new_j <= number[1][1] and new_j >= number[1][0]:
            return True
    return False

for star in all_stars:
    close_numbers = []
    for number in all_numbers:
        if close(star, number): close_numbers.append(number[0])
    if len(close_numbers) == 2:
        result += int(close_numbers[0]) * int(close_numbers[1])

print("Result is:", result)

            

