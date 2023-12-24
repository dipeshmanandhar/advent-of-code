from __future__ import annotations

from enum import Enum

from src.common.read_input import read_input


class Direction(Enum):
    UP, LEFT, DOWN, RIGHT = range(4)

    @classmethod
    def from_str(cls, dir: str):
        if dir == "3":
            return Direction.UP
        elif dir == "2":
            return Direction.LEFT
        elif dir == "1":
            return Direction.DOWN
        elif dir == "0":
            return Direction.RIGHT
        else:
            return None


input = read_input("input.txt", 2023, 18)

plan: list[tuple[Direction, int]] = []
x = 0
y = 0
max_x = 0

for line in input:
    dir, steps, color = line.split()
    dir = color[7]
    steps = color[2:7]
    dir = Direction.from_str(dir)
    steps = int(steps, 16)
    plan.append((dir, steps))
    if dir == Direction.UP:
        y += steps
    elif dir == Direction.LEFT:
        x -= steps
    elif dir == Direction.DOWN:
        y -= steps
    else:
        x += steps
        if x > max_x:
            max_x = x

area = 0
prev_horiz_dir = None
for i, (dir, steps) in enumerate(plan):
    next_horiz_dir = plan[(i + 1) % len(plan)][0]
    if dir == Direction.UP:
        y += steps
        offset = 0
        if prev_horiz_dir == Direction.RIGHT:
            offset -= 1
        else:
            offset += 1
        if next_horiz_dir == Direction.LEFT:
            offset -= 1
        else:
            offset += 1
        offset //= 2
        area += (max_x - x + 1) * (steps + offset)
    elif dir == Direction.LEFT:
        x -= steps
        prev_horiz_dir = dir
    elif dir == Direction.DOWN:
        y -= steps
        offset = 0
        if prev_horiz_dir == Direction.LEFT:
            offset -= 1
        else:
            offset += 1
        if next_horiz_dir == Direction.RIGHT:
            offset -= 1
        else:
            offset += 1
        offset //= 2
        area -= (max_x - x) * (steps + offset)
    else:
        x += steps
        prev_horiz_dir = dir

print(area)
