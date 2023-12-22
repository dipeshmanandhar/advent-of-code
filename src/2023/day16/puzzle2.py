from copy import deepcopy
from enum import Enum

from src.common.read_input import read_input


class Direction(Enum):
    UP, LEFT, DOWN, RIGHT = range(4)

    def flip(self):
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.LEFT:
            return Direction.RIGHT
        elif self == Direction.DOWN:
            return Direction.UP
        else:
            return Direction.LEFT

    def next(self, tile: str):
        if tile == "/":
            if self == Direction.UP:
                return (Direction.RIGHT,)
            elif self == Direction.LEFT:
                return (Direction.DOWN,)
            elif self == Direction.DOWN:
                return (Direction.LEFT,)
            else:
                return (Direction.UP,)
        elif tile == "\\":
            if self == Direction.UP:
                return (Direction.LEFT,)
            elif self == Direction.LEFT:
                return (Direction.UP,)
            elif self == Direction.DOWN:
                return (Direction.RIGHT,)
            else:
                return (Direction.DOWN,)
        elif tile == "|":
            if self == Direction.LEFT or self == Direction.RIGHT:
                return (Direction.UP, Direction.DOWN)
        elif tile == "-":
            if self == Direction.UP or self == Direction.DOWN:
                return (Direction.LEFT, Direction.RIGHT)
        return (self,)

    def reverse(self, tile: str):
        if tile == "/" or tile == "\\":
            return self.next(tile)[0].flip()
        else:
            return self.flip()


input = read_input("input.txt", 2023, 16)

original_board: list[list[str]] = [[char for char in line] for line in input]
NUM_ROWS = len(original_board)
NUM_COLS = len(original_board[0])
original_prev_dirs: list[list[list[Direction]]] = [
    [[] for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)
]


def shoot_beam(
    board: list[list[str]],
    prev_dirs: list[list[list[Direction]]],
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
        if (
            direction in prev_dirs[r][c]
            or direction.reverse(board[r][c]) in prev_dirs[r][c]
        ):
            break
        else:
            prev_dirs[r][c].append(direction)
        next_directions = direction.next(board[r][c])
        direction = next_directions[0]
        if len(next_directions) > 1:
            shoot_beam(board, prev_dirs, r, c, next_directions[1])


def count_energized(prev_dirs: list[list[list[Direction]]]):
    return sum([sum([bool(x) for x in row]) for row in prev_dirs])


max_energized = 0
for direction in Direction:
    loop_iterations = 0
    if direction == Direction.LEFT or direction == Direction.RIGHT:
        loop_iterations = NUM_ROWS
    else:
        loop_iterations = NUM_COLS
    for i in range(loop_iterations):
        board = deepcopy(original_board)
        prev_dirs = deepcopy(original_prev_dirs)
        if direction == Direction.UP:
            shoot_beam(board, prev_dirs, NUM_ROWS, i, direction)
        elif direction == Direction.LEFT:
            shoot_beam(board, prev_dirs, i, NUM_COLS, direction)
        elif direction == Direction.DOWN:
            shoot_beam(board, prev_dirs, -1, i, direction)
        else:
            shoot_beam(board, prev_dirs, i, -1, direction)
        curr_energized = count_energized(prev_dirs)

        if curr_energized > max_energized:
            max_energized = curr_energized

print(max_energized)
