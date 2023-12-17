from src.common.read_input import read_input

LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"
DOWN = "DOWN"


def char_to_pipe(char: str):
    pipe = {LEFT: False, RIGHT: False, UP: False, DOWN: False}
    if char == "|":
        pipe[UP] = True
        pipe[DOWN] = True
    elif char == "-":
        pipe[LEFT] = True
        pipe[RIGHT] = True
    elif char == "L":
        pipe[UP] = True
        pipe[RIGHT] = True
    elif char == "J":
        pipe[UP] = True
        pipe[LEFT] = True
    elif char == "7":
        pipe[LEFT] = True
        pipe[DOWN] = True
    elif char == "F":
        pipe[DOWN] = True
        pipe[RIGHT] = True
    return pipe


def s_to_pipe(board: list[list[dict[str, bool]]], start_r: int, start_c: int):
    if r - 1 >= 0:
        if board[r - 1][c][DOWN]:
            board[r][c][UP] = True
    if r + 1 < len(board):
        if board[r + 1][c][UP]:
            board[r][c][DOWN] = True
    if c - 1 >= 0:
        if board[r][c - 1][RIGHT]:
            board[r][c][LEFT] = True
    if c + 1 < len(board):
        if board[r][c + 1][LEFT]:
            board[r][c][RIGHT] = True


def move_next(board: list[list[dict[str, bool]]], r: int, c: int, prev: str):
    for dir in board[r][c]:
        if dir != prev and board[r][c][dir]:
            if dir == LEFT:
                c -= 1
                prev = RIGHT
            elif dir == RIGHT:
                c += 1
                prev = LEFT
            elif dir == UP:
                r -= 1
                prev = DOWN
            elif dir == DOWN:
                r += 1
                prev = UP
            break
    return r, c, prev


# checks is this a wall when passing from left to right, on the bottom half
def is_wall(board: list[list[dict[str, bool]]], r: int, c: int):
    return board[r][c][DOWN]


input = read_input("input.txt", 2023, 10)

board_str = [[char for char in line] for line in input]
board = [[char_to_pipe(char) for char in line] for line in input]
board_is_loop = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
start_r, start_c = -1, -1

for r, line in enumerate(input):
    c = line.find("S")
    if c >= 0:
        start_r, start_c = r, c
        break
s_to_pipe(board, start_r, start_c)
board_is_loop[start_r][start_c] = True

curr_r, curr_c = start_r, start_c
curr_prev = ""
# first pass to mark the pipes that are part of the main loop
while True:
    curr_r, curr_c, curr_prev = move_next(board, curr_r, curr_c, curr_prev)
    board_is_loop[curr_r][curr_c] = True
    if (curr_r, curr_c) == (start_r, start_c):
        break

# remove extra pipes
for r, row in enumerate(board_str):
    for c, char in enumerate(row):
        if not board_is_loop[r][c]:
            board_str[r][c] = "."

# mark inside cells as I and count number of cells inside
num_inside = 0
for r, row in enumerate(board_str):
    is_inside = False
    for c, char in enumerate(row):
        if board_is_loop[r][c]:
            if is_wall(board, r, c):
                is_inside = not is_inside
        else:
            if is_inside:
                board_str[r][c] = "I"
                num_inside += 1
    # print("".join(row))

print(num_inside)
