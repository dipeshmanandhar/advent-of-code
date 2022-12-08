from src.common.read_input import read_input

__SIZE__ = '__size__'
SUM_SIZES = 0


def cd(curr_dir, next_dir):
    return curr_dir[next_dir]


def ls(curr_dir, lines):
    for line in lines:
        line_arr = line.split()
        if line_arr[0] == 'dir':
            if line_arr[1] not in curr_dir:
                curr_dir[line_arr[1]] = {'..': curr_dir}
        else:
            curr_dir[line_arr[1]] = int(line_arr[0])


def get_size(dir):
    global SUM_SIZES
    if __SIZE__ in dir:
        return dir[__SIZE__]
    total_size = 0
    for child_name, child_value in dir.items():
        if child_name == '..':
            continue
        elif isinstance(child_value, int):
            total_size += child_value
        else:
            total_size += get_size(child_value)
    dir[__SIZE__] = total_size

    if total_size <= 100000:
        SUM_SIZES += total_size

    return total_size


input = read_input('input.txt', 2022, 7)


root = {
    '/': {}
}

curr_dir = root

for i, line in enumerate(input):
    line_arr = line.split()
    if line_arr[0] != '$':
        continue
    elif line_arr[1] == 'cd':
        curr_dir = cd(curr_dir, line_arr[2])
    elif line_arr[1] == 'ls':
        end_index = len(input)
        for j in range(i+1, len(input)):
            if input[j][0] == '$':
                end_index = j
                break
        lines = input[i+1:end_index]
        ls(curr_dir, lines)

get_size(root)

print(SUM_SIZES)
