from src.common.read_input import read_input


def add_row(grid):
    WIDTH = len(grid[0])
    grid.append(['.' for _ in range(WIDTH)])
    grid[-1][0] = '|'
    grid[-1][-1] = '|'


def remove_row(grid):
    grid.pop()


def display(grid, rock_pos=[]):
    grid_copy = [row.copy() for row in grid]
    for r, c in rock_pos:
        grid_copy[r][c] = '@'
    for row in reversed(grid_copy):
        print(''.join(row))
    print()


def add_rock(grid, rock_type, total_height):
    for _ in range(len(grid), total_height + 4):
        add_row(grid)
    for _ in range(len(grid), total_height + 4, -1):
        remove_row(grid)
    rock_pos = []
    r = len(grid)
    add_row(grid)
    if rock_type == 0:
        for c in range(3, 7):
            rock_pos.append((r, c))
    elif rock_type == 1:
        add_row(grid)
        add_row(grid)
        c = 4
        rock_pos.append((r, c))
        rock_pos.append((r+2, c))
        r += 1
        for c in range(3, 6):
            rock_pos.append((r, c))
    elif rock_type == 2:
        add_row(grid)
        add_row(grid)
        for c in range(3, 6):
            rock_pos.append((r, c))
        c = 5
        rock_pos.append((r+1, c))
        rock_pos.append((r+2, c))
    elif rock_type == 3:
        add_row(grid)
        add_row(grid)
        add_row(grid)
        c = 3
        for row in range(r, len(grid)):
            rock_pos.append((row, c))
    elif rock_type == 4:
        add_row(grid)
        for row in range(r, len(grid)):
            for c in range(3, 5):
                rock_pos.append((row, c))
    else:
        print('ERROR')

    return rock_pos


# returns True if there is a collision
def check_collision(grid, rock_pos):
    for r, c in rock_pos:
        if grid[r][c] != '.':
            return True
    return False


def move_horizontal(grid, rock_pos, dir):
    d_c = 1 if dir == '>' else -1
    new_rock_pos = [(r, c+d_c) for r, c in rock_pos]
    if not check_collision(grid, new_rock_pos):
        return new_rock_pos
    return rock_pos


# returns True if the rock has reached steady state
def move_vertical(grid, rock_pos, safe):
    new_rock_pos = [(r-1, c) for r, c in rock_pos]
    if safe or not check_collision(grid, new_rock_pos):
        return (new_rock_pos, False)
    return (rock_pos, True)


# returns True if the rock has reached steady state
def move_rock(grid, rock_pos, dir, safe=False):
    new_rock_pos = move_horizontal(grid, rock_pos, dir)
    new_rock_pos, is_steady = move_vertical(grid, new_rock_pos, safe)
    for i in range(len(new_rock_pos)):
        rock_pos[i] = new_rock_pos[i]
    return is_steady


def stop_rock(grid, rock_pos):
    max_height = 0
    for r, c in rock_pos:
        grid[r][c] = '#'
        if r > max_height:
            max_height = r
    return max_height


input = read_input('input.txt', 2022, 17)

input = input[0]
INPUT_LEN = len(input)
WIDTH = 9
grid = [['-' for _ in range(WIDTH)]]
grid[0][0] = '+'
grid[0][-1] = '+'
total_height = 0
input_i = 0
rock_num_one_iteration = 0
prev_rock_num = 0
prev_total_height = 0
rock_num_diffs = [0]
total_height_diffs = [0]
input_iterations = 0
height_from_rock = [[] for _ in range(5)]
second_half = False

rock_num = 0
while True:
    rock_pos = add_rock(grid, rock_num % 5, total_height)
    # display(grid, rock_pos)
    rock_move_i = 0
    while not move_rock(grid, rock_pos, input[input_i], safe=rock_move_i < 3):
        input_i = (input_i + 1) % INPUT_LEN
        if input_i == 0:
            rock_num_diff = rock_num - prev_rock_num
            prev_rock_num = rock_num
            total_height_diff = total_height - prev_total_height
            prev_total_height = total_height
            rock_num_diffs.append(rock_num_diff)
            total_height_diffs.append(total_height_diff)
            input_iterations += 1
            if input_iterations % 5 == 0:
                if input_iterations == 10:
                    break
        rock_move_i += 1
    if input_iterations == 10:
        break
    input_i = (input_i + 1) % INPUT_LEN
    if input_i == 0:
        print('BRUH')
        # For some reason we will never reach this case? (input end reached at the same time that a new rock is generated)
    rock_move_i += 1
    curr_rock_height = stop_rock(grid, rock_pos)
    if second_half:
        height_from_rock[input_iterations -
                         5].append(max(curr_rock_height - total_height, 0))
    if curr_rock_height > total_height:
        total_height = curr_rock_height
    if input_iterations >= 5:
        second_half = True
    rock_num += 1

rocks_first_5 = sum(rock_num_diffs[1:6])
rocks_second_5 = sum(rock_num_diffs[-5:])
height_first_5 = sum(total_height_diffs[1:6])
height_second_5 = sum(total_height_diffs[-5:])

target_rocks = 1000000000000
remaining_rocks = target_rocks - rocks_first_5
remaining_cycles = remaining_rocks // rocks_second_5
total_rocks = rocks_first_5 + rocks_second_5 * remaining_cycles
total_height = height_first_5 + height_second_5 * remaining_cycles

for i, (rock_diff, total_height_diff) in enumerate(zip(rock_num_diffs[-5:], total_height_diffs[-5:])):
    if total_rocks + rock_diff < target_rocks:
        total_rocks += rock_diff
        total_height += total_height_diff
    else:
        actual_rock_diff = target_rocks - total_rocks
        total_height += sum(height_from_rock[i][:actual_rock_diff])
        break

print(total_height)
