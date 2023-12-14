import os, re

TEST = False 

text_file = "example1.txt" if TEST else "input.txt"

result = 0

def what_number(color):
    return int(re.findall("\d+", color)[0])

def get_number(s):
    for color in s:
        if "blue" in color and what_number(color) > 14: return True
        if "red" in color and what_number(color) > 12: return True
        if "green" in color and what_number(color) > 13: return True
    return False

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        game_number, game = line.split(":")
        game_number = int(game_number.split(" ")[1])
        game = game.split(";")
        how_to_sum = 0
        for pull in game:
            colors = pull.split(",")
            if get_number(colors):
                how_to_sum = 0 
                break
            else:
                if how_to_sum == 0: how_to_sum += game_number
        result += how_to_sum

print("Result is", result)