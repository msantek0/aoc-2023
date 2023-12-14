import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

arr = []
with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        arr.append(line.split(":")[1])

times = [int(x) for x in arr[0].split(" ") if x.isdigit()]

records = [int(x) for x in arr[1].split(" ") if x.isdigit()]

print(times)
print(records)

def status(index, time):
    return index * (time - index)

def how_much_record_holders(index):
    global times, records
    win_count = 0
    for i in range(1, times[index]-1):
        if status(i, times[index]) > records[index]: win_count += 1
    return win_count

result = 1
for i in range(len(times)):
    r = how_much_record_holders(i)
    print(i, r)
    result *= r 

print("Result:", result)