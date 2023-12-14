substrings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
              '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        min_r = 1000
        max_r = -1
        min_index = -1 
        max_index = -1 
        for i, substring in enumerate(substrings):
            index = line.find(substring)
            last_index = line.rfind(substring)
            if index != -1 and index < min_r:
                min_r = index
                min_index = i
            
            if last_index != -1 and last_index > max_r:
                max_r = last_index
                max_index = i

        if min_index == -1 or max_index == -1: 
            print("Nesto je krivo")
            print(line)
            exit(0)
        if min_index > 9: min_index -= 9
        if max_index > 9: max_index -= 9
        result += int(str(min_index) + str(max_index))
            

print("Result", result)