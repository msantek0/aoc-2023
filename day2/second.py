import os, re

TEST = False 

text_file = "example2.txt" if TEST else "input.txt"

result = 0

def what_number(color):
    return int(re.findall("\d+", color)[0])

def get_numbers(s):
    blue = -1
    red = -1
    green = -1
    for color in s:
        if "blue" in color: blue =  what_number(color)
        if "red" in color: red = what_number(color)
        if "green" in color: green = what_number(color)
    return blue, green, red 

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        game_number, game = line.split(":")
        game_number = int(game_number.split(" ")[1])
        game = game.split(";")
        max_blue = 0 
        max_green = 0
        max_red = 0
        for pull in game:
            colors = pull.split(",")
            blue, green, red = get_numbers(colors)
            if blue != -1: max_blue = max(blue, max_blue) 
            if green != -1: max_green = max(green, max_green) 
            if red != -1: max_red = max(red, max_red) 
        result += max_blue * max_red * max_green 

print("Result is", result)