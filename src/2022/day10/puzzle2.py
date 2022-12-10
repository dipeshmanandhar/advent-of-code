from src.common.read_input import read_input

input = read_input('input.txt', 2022, 10)

x = 1
clock = 0
for line in input:
    line_arr = line.split()
    end = '\n' if clock % 40 == 39 else ''
    if abs(clock % 40 - x) <= 1:
        print('#', end=end)
    else:
        print('.', end=end)
    if line_arr[0] == 'noop':
        clock += 1
    elif line_arr[0] == 'addx':
        clock += 1
        end = '\n' if clock % 40 == 39 else ''
        if abs(clock % 40 - x) <= 1:
            print('#', end=end)
        else:
            print('.', end=end)
        x += int(line_arr[1])
        clock += 1
