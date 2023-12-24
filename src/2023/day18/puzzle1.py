from __future__ import annotations

from enum import Enum

from src.common.read_input import read_input


class Direction(Enum):
    UP, LEFT, DOWN, RIGHT = range(4)

    @classmethod
    def from_str(cls, dir: str):
        if dir == "U":
            return Direction.UP
        elif dir == "L":
            return Direction.LEFT
        elif dir == "D":
            return Direction.DOWN
        elif dir == "R":
            return Direction.RIGHT
        else:
            return None


input = read_input("input.txt", 2023, 18)

board: list[list[str]] = [["#"]]
r = 0
c = 0
for line in input:
    dir, steps, color = line.split()
    dir = Direction.from_str(dir)
    steps = int(steps)
    for _ in range(steps):
        if dir == Direction.UP:
            r -= 1
        elif dir == Direction.LEFT:
            c -= 1
        elif dir == Direction.DOWN:
            r += 1
        else:
            c += 1
        if r == -1:
            board.insert(0, ["." for _ in range(len(board[0]))])
            r = 0
        elif r == len(board):
            board.append(["." for _ in range(len(board[0]))])
        if c == -1:
            for row in range(len(board)):
                board[row].insert(0, ".")
            c = 0
        elif c == len(board[0]):
            for row in range(len(board)):
                board[row].append(".")
        board[r][c] = "#"

for r, row in enumerate(board[:-1]):
    inside = False
    for c, char in enumerate(row):
        if char == "#" and board[r + 1][c] == "#":
            inside = not inside
        if inside:
            board[r][c] = "#"

size = sum([sum([char == "#" for char in row]) for row in board])

print(size)
