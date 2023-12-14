import os, re
from functools import cmp_to_key
from collections import Counter

TEST = False 
strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

text_file = "example1.txt" if TEST else "input.txt"

result = 0

cards_played = []
bids = []

with open(text_file, "r") as f:
    for line in f:
        line = line.strip() 
        cards_played.append(line.split(" ")[0])
        bids.append(line.split(" ")[1])

print(cards_played)
print(bids)

def get_strength(hand):
    count_cards = Counter(hand)
    if len(count_cards) == 1: return 5
    _, count_of_most_common = count_cards.most_common(1)[0]
    _, count_of_second_most_common = count_cards.most_common(2)[1]
    if count_of_most_common >= 4: return count_of_most_common 
    if count_of_most_common == 3:
        if count_of_second_most_common == 2: return 3
        return 2
    if count_of_most_common == 2:
        if count_of_second_most_common == 2: return 1
        return 0
    return -1

def custom_sort(a, b):
    a_strength = get_strength(a[0])
    b_strength = get_strength(b[0])
    if a_strength > b_strength: return 1
    elif a_strength < b_strength: return -1
    else:
        for i in range(len(a[0])):
            a_ind = strength.index(a[0][i])
            b_ind = strength.index(b[0][i])
            if a_ind > b_ind: return 1
            elif a_ind < b_ind: return -1 
    return -1

combined = list(zip(cards_played, bids))

compare = cmp_to_key(custom_sort)
# Sort based on the custom sorting function
combined.sort(key=compare)

# Extract the second array in the sorted order
sorted_array1 = [x[0] for x in combined]
sorted_array2 = [int(x[1]) for x in combined]
result = 0

for i, element in enumerate(sorted_array2):
    result += (i+1) * element
print(sorted_array1)
print(sorted_array2)
print("Result:", result)