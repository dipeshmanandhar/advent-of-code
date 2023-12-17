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


input = read_input("input.txt", 2023, 10)

board = [[char_to_pipe(char) for char in line] for line in input]
start_r, start_c = -1, -1

for r, line in enumerate(input):
    c = line.find("S")
    if c >= 0:
        start_r, start_c = r, c
        break
s_to_pipe(board, start_r, start_c)

steps = 1
a_r, a_c = start_r, start_c
b_r, b_c = start_r, start_c
a_prev = ""
b_prev = ""
a_started = False
if board[start_r][start_c][LEFT]:
    a_c -= 1
    a_prev = RIGHT
    a_started = True
if board[start_r][start_c][RIGHT]:
    if a_started:
        b_c += 1
        b_prev = LEFT
    else:
        a_c += 1
        a_prev = LEFT
        a_started = True
if board[start_r][start_c][UP]:
    if a_started:
        b_r -= 1
        b_prev = DOWN
    else:
        a_r -= 1
        a_prev = DOWN
        a_started = True
if board[start_r][start_c][DOWN]:
    if a_started:
        b_r += 1
        b_prev = UP
    else:
        a_r += 1
        a_prev = UP
        a_started = True

while (a_r, a_c) != (b_r, b_c):
    a_r, a_c, a_prev = move_next(board, a_r, a_c, a_prev)
    b_r, b_c, b_prev = move_next(board, b_r, b_c, b_prev)
    steps += 1

print(steps)
