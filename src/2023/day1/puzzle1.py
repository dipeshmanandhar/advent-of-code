from src.common.read_input import read_input

input = read_input('input.txt', 2023, 1)

total = 0
for line in input:
    first = -1
    last = -1
    curr = -1
    for c in line:
        if c.isdigit():
            curr = int(c)
            if first < 0:
                first = curr
    last = curr
    num = int(f'{first}{last}')
    total += num

print(total)
