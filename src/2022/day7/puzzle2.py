from src.common.read_input import read_input

__SIZE__ = '__size__'
MAX_STORAGE = 70000000


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

    return total_size


def find_smallest_dir_to_delete(dir, need_to_delete):
    if dir[__SIZE__] < need_to_delete:
        return MAX_STORAGE
    min_to_delete = dir[__SIZE__]
    for child_name, child_value in dir.items():
        if child_name == '..' or isinstance(child_value, int):
            continue
        elif __SIZE__ in child_value:
            child_smallest_size = find_smallest_dir_to_delete(
                child_value, need_to_delete)
            if child_smallest_size < min_to_delete:
                min_to_delete = child_smallest_size
    return min_to_delete


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

total_size = get_size(root)
remaining_storage = MAX_STORAGE - total_size
need_to_delete = 30000000 - remaining_storage

print(find_smallest_dir_to_delete(root, need_to_delete))
