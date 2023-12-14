import re

result = 0
with open("input.txt", "r") as f:
    for line in f:
        numbers = re.findall(r'\d+', line.strip())
        print(numbers)
        first_digit = numbers[0]
        if len(first_digit) > 1: first_digit = first_digit[0]
        last_digit = numbers[-1]
        if len(last_digit) > 1: last_digit = last_digit[-1]
        result += int(first_digit + last_digit)

print("Result:", result)