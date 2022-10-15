from src.common.read_input import read_input


def draw_line(board, line):
    x1, y1 = line[0]
    x2, y2 = line[1]
    if y1 == y2:    # horizontal line (y is same)
        # force x1 to be less than x2
        if x2 < x1:
            x1, x2 = x2, x1
        for i in range(x2-x1+1):
            board[y1][x1+i] += 1
    elif x1 == x2:    # vertical line (x is same)
        # force y1 to be less than y2
        if y2 < y1:
            y1, y2 = y2, y1
        for i in range(y2-y1+1):
            board[y1+i][x1] += 1
    else:   # diagonal line at 45 degrees
        # force x1 to be less than x2
        if x2 < x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        y_i_mult = 1
        if y2 < y1:
            y_i_mult = -1
        for i in range(x2-x1+1):
            board[y1+y_i_mult*i][x1+i] += 1


def calculate_dangerous_points(board):
    return len([1 for row in board for cell in row if cell >= 2])


input = read_input('input.txt', 2021, 5)

# lines is a list<list<tuple<int, int>>>
lines = [[tuple(int(coord) for coord in point_str.split(','))
          for point_str in row.split(' -> ')] for row in input]
max_x, max_y = [max(all_coord) for all_coord in
                zip(*[point for line in lines for point in line])]
width = max_x + 1
height = max_y + 1
board = [[0] * width for _ in range(height)]
for line in lines:
    draw_line(board, line)
num_dangerous_points = calculate_dangerous_points(board)

print(num_dangerous_points)
