from src.common.read_input import read_input


def scenic_score(grid, row, col):
    num_rows = len(input)
    num_cols = len(input[0])
    if row == 0 or row == num_rows-1 or col == 0 or col == num_cols-1:
        return 0

    left_score = col
    for c in range(col-1, 0, -1):
        if grid[row][c] >= grid[row][col]:
            left_score = col-c
            break
    right_score = num_cols-1-col
    for c in range(col+1, num_cols):
        if grid[row][c] >= grid[row][col]:
            right_score = c-col
            break
    up_score = row
    for r in range(row-1, 0, -1):
        if grid[r][col] >= grid[row][col]:
            up_score = row-r
            break
    down_score = num_rows-1-row
    for r in range(row+1, num_rows):
        if grid[r][col] >= grid[row][col]:
            down_score = r-row
            break
    return left_score * right_score * up_score * down_score


input = read_input('input.txt', 2022, 8)

num_rows = len(input)
num_cols = len(input[0])

grid = [[int(num) for num in list(line)] for line in input]

max_scenic_score = 0
for row in range(1, num_rows-1):
    for col in range(1, num_cols-1):
        curr_scenic_score = scenic_score(grid, row, col)
        if curr_scenic_score > max_scenic_score:
            max_scenic_score = curr_scenic_score

print(max_scenic_score)
