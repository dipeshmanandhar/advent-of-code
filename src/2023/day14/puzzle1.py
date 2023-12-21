from src.common.read_input import read_input


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


def calc_load(board: list[list[str]]):
    load = 0
    for c in range(len(board[0])):
        for r in range(len(board)):
            if board[r][c] == "O":
                load += len(board) - r
    return load


input = read_input("input.txt", 2023, 14)

board = [[char for char in line] for line in input]

tilt_north(board)

print(calc_load(board))
