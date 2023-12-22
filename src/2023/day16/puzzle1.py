from enum import Enum

from src.common.read_input import read_input


class Direction(Enum):
    UP, LEFT, DOWN, RIGHT = range(4)


input = read_input("input.txt", 2023, 16)

board: list[list[str]] = [[char for char in line] for line in input]
NUM_ROWS = len(board)
NUM_COLS = len(board[0])
prev_dirs: list[list[list[Direction]]] = [
    [[] for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)
]


def shoot_beam(
    r: int = 0,
    c: int = -1,
    direction: Direction = Direction.RIGHT,
):
    while True:
        if direction == Direction.UP:
            r -= 1
        elif direction == Direction.LEFT:
            c -= 1
        elif direction == Direction.DOWN:
            r += 1
        else:
            c += 1
        if r < 0 or r >= NUM_ROWS or c < 0 or c >= NUM_COLS:
            break
        if direction in prev_dirs[r][c]:
            break
        else:
            prev_dirs[r][c].append(direction)
        if board[r][c] == "/":
            if direction == Direction.UP:
                direction = Direction.RIGHT
            elif direction == Direction.LEFT:
                direction = Direction.DOWN
            elif direction == Direction.DOWN:
                direction = Direction.LEFT
            else:
                direction = Direction.UP
        elif board[r][c] == "\\":
            if direction == Direction.UP:
                direction = Direction.LEFT
            elif direction == Direction.LEFT:
                direction = Direction.UP
            elif direction == Direction.DOWN:
                direction = Direction.RIGHT
            else:
                direction = Direction.DOWN
        elif board[r][c] == "|":
            if direction == Direction.LEFT or direction == Direction.RIGHT:
                direction = Direction.DOWN
                shoot_beam(r, c, Direction.UP)
        elif board[r][c] == "-":
            if direction == Direction.UP or direction == Direction.DOWN:
                direction = Direction.RIGHT
                shoot_beam(r, c, Direction.LEFT)


def count_energized():
    return sum([sum([bool(x) for x in row]) for row in prev_dirs])


shoot_beam()

print(count_energized())
