from src.common.read_input import read_input

input = read_input('input.txt', 2023, 1)

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

total = 0
for line in input:
    first = -1
    first_i = -1
    last = -1
    last_i = -1
    
    for num_minus_1, num_str in enumerate(nums):
        curr_i = line.find(num_str)
        if curr_i != -1:
            if curr_i < first_i or first_i == -1:
                first = num_minus_1 + 1
                first_i = curr_i
        curr_i = line.rfind(num_str)
        if curr_i != -1:
            if curr_i > last_i:
                last = num_minus_1 + 1
                last_i = curr_i
        curr_i = line.find(str(num_minus_1 + 1))
        if curr_i != -1:
            if curr_i < first_i or first_i == -1:
                first = num_minus_1 + 1
                first_i = curr_i
        curr_i = line.rfind(str(num_minus_1 + 1))
        if curr_i != -1:
            if curr_i > last_i:
                last = num_minus_1 + 1
                last_i = curr_i
    
    num = int(f'{first}{last}')
    total += num

print(total)
