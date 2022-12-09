from src.common.read_input import read_input


def is_visible(grid, row, col):
    num_rows = len(input)
    num_cols = len(input[0])
    if row == 0 or row == num_rows-1 or col == 0 or col == num_cols-1:
        return True

    is_visible_left = True
    for c in range(0, col):
        if grid[row][c] >= grid[row][col]:
            is_visible_left = False
            break
    is_visible_right = True
    for c in range(col+1, num_cols):
        if grid[row][c] >= grid[row][col]:
            is_visible_right = False
            break
    is_visible_up = True
    for r in range(0, row):
        if grid[r][col] >= grid[row][col]:
            is_visible_up = False
            break
    is_visible_down = True
    for r in range(row+1, num_rows):
        if grid[r][col] >= grid[row][col]:
            is_visible_down = False
            break
    is_visible_middle = is_visible_left or is_visible_right or is_visible_up or is_visible_down
    return is_visible_middle


input = read_input('input.txt', 2022, 8)

num_rows = len(input)
num_cols = len(input[0])

grid = [[int(num) for num in list(line)] for line in input]

num_visible = 0
for row in range(num_rows):
    for col in range(num_cols):
        if is_visible(grid, row, col):
            num_visible += 1

print(num_visible)
