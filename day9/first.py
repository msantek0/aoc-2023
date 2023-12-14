import os, re

def solve(arr):
    if all(element == arr[0] for element in arr): return arr[0]
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append(arr[i+1] - arr[i])
    solved = solve(new_arr)
    return arr[-1] + solved

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

result = 0

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        result += solve([int(x) for x in line.split(" ")])
        
print(result)