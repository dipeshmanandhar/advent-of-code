from src.common.read_input import read_input

input = read_input('input.txt', 2022, 10)

x = 1
clock = 1
signal_strength_sum = 0
for line in input:
    line_arr = line.split()
    if line_arr[0] == 'noop':
        clock += 1
    elif line_arr[0] == 'addx':
        clock += 1
        if (clock-20) % 40 == 0:
            signal_strength_sum += clock * x
        x += int(line_arr[1])
        clock += 1
    if (clock-20) % 40 == 0:
        signal_strength_sum += clock * x

print(signal_strength_sum)
