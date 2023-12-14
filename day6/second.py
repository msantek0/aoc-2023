import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

arr = []
with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        arr.append(line.split(":")[1])

times = [x for x in arr[0].split(" ") if x.isdigit()]

records = [x for x in arr[1].split(" ") if x.isdigit()]


def status(index, time):
    return index * (time - index)

def how_much_record_holders():
    global times, records
    first_win = -1
    last_win = -1
    for i in range(1, times-1):
        if status(i, times) > records:
            first_win = i
            break
    for i in range(times - 1, 1, -1):
        if status(i, times) > records:
            last_win = i
            break
    return last_win - first_win + 1 

result = 1
times = int("".join(times))
records = int("".join(records))
print(times)
print(records)


print("Result:", how_much_record_holders())