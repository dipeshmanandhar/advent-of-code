from src.common.read_input import read_input

TOTAL_SPIN_CYCLES = 1000000000


def find_empty_space(board: list[list[str]], r: int, c: int):
    final_r = 0
    for r_i in range(r - 1, -1, -1):
        if r_i < 0:
            final_r = 0
            break
        if board[r_i][c] != ".":
            final_r = r_i + 1
            break
    return final_r


def tilt_north(board: list[list[str]]):
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] == "O":
                final_r = find_empty_space(board, r, c)
                if final_r != r:
                    board[final_r][c] = "O"
                    board[r][c] = "."


def rotate(board: list[list[str]]):
    return [[row[c] for row in reversed(board)] for c in range(len(board))]


def spin_cycle(board: list[list[str]]):
    for _ in range(4):
        tilt_north(board)
        board = rotate(board)
    return board


def calc_load(board: list[list[str]]):
    load = 0
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] == "O":
                load += len(board) - r
    return load


def board_to_str(board: list[list[str]]):
    return "\n".join(["".join(row) for row in board])


def str_to_board(board_str: str):
    return [[char for char in line] for line in board_str.split()]


input = read_input("input.txt", 2023, 14)

board = [[char for char in line] for line in input]
previous_boards: list[str] = [board_to_str(board)]

for i in range(1, TOTAL_SPIN_CYCLES):
    board = spin_cycle(board)
    board_str = board_to_str(board)
    if board_str in previous_boards:
        prev_i = previous_boards.index(board_str)
        remaining_cycles = (TOTAL_SPIN_CYCLES - i) % (i - prev_i)
        board = str_to_board(previous_boards[prev_i + remaining_cycles])
        break
    else:
        previous_boards.append(board_str)

print(calc_load(board))
