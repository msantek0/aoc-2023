import os, re

TEST = True

text_file = "example2.txt" if TEST else "input.txt"

result = 0

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 