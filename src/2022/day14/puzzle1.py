from src.common.read_input import read_input


def display(grid):
    for row in grid:
        print(''.join(row))


input = read_input('input.txt', 2022, 14)

furthest_left = 500
furthest_right = 500
furthest_up = 0
furthest_down = 0

rock_structures = [[] for _ in range(len(input))]

for i, line in enumerate(input):
    rock_structures[i] = [tuple(int(num) for num in coord.split(','))
                          for coord in line.split(' -> ')]
    for coord in rock_structures[i]:
        x, y = coord
        if x < furthest_left:
            furthest_left = x
        elif x > furthest_right:
            furthest_right = x
        if y > furthest_down:
            furthest_down = y

X_SIZE = furthest_right - furthest_left + 1
Y_SIZE = furthest_down - furthest_up + 1
grid = [['.'] * X_SIZE for _ in range(Y_SIZE)]


def x_to_c(x):
    return x - furthest_left


def drop_sand(grid):
    r = 0
    c = x_to_c(500)
    while True:
        r += 1
        if r >= Y_SIZE:
            return False
        elif grid[r][c] == '.':
            continue
        elif c-1 < 0:
            return False
        elif grid[r][c-1] == '.':
            c -= 1
        elif c+1 >= X_SIZE:
            return False
        elif grid[r][c+1] == '.':
            c += 1
        else:
            r -= 1
            break
    grid[r][c] = 'o'
    return True


for rock_structure in rock_structures:
    for rs1, rs2 in zip(rock_structure, rock_structure[1:]):
        if rs1[0] < rs2[0] or rs1[1] < rs2[1]:
            start = rs1
            stop = rs2
        else:
            start = rs2
            stop = rs1
        if start[0] == stop[0]:  # vertical
            x = start[0]
            c = x_to_c(x)
            for r in range(start[1], stop[1]+1):
                grid[r][c] = '#'
        elif start[1] == stop[1]:  # horizontal
            r = start[1]
            for x in range(start[0], stop[0]+1):
                c = x_to_c(x)
                grid[r][c] = '#'
grid[0][x_to_c(500)] = '+'
num_sand = 0
while(drop_sand(grid)):
    num_sand += 1
display(grid)
print(num_sand)
