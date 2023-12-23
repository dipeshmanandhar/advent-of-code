from __future__ import annotations

import heapq
from enum import Enum
from functools import total_ordering

from src.common.read_input import read_input


@total_ordering
class Direction(Enum):
    UP, LEFT, DOWN, RIGHT = range(4)

    @classmethod
    def all(cls) -> list[Direction]:
        return [Direction(x) for x in range(4)]

    def reverse(self) -> Direction:
        if self == Direction.UP:
            return Direction.DOWN
        elif self == Direction.LEFT:
            return Direction.RIGHT
        elif self == Direction.DOWN:
            return Direction.UP
        else:
            return Direction.LEFT

    def possible_next_directions(self, count: int) -> list[tuple[Direction, int]]:
        next_directions = [(dir, 1) for dir in Direction.all()]
        next_directions.remove((self.reverse(), 1))
        if count >= 3:
            next_directions.remove((self, 1))
        else:
            next_directions[next_directions.index((self, 1))] = (self, count + 1)
        return next_directions

    def to_int(self) -> int:
        return Direction.all().index(self)

    def __lt__(self, other: Direction) -> bool:
        return self.to_int() < other.to_int()


input = read_input("input.txt", 2023, 17)

original_heat_loss_map = [[int(heat_loss) for heat_loss in line] for line in input]

NUM_ROWS = len(original_heat_loss_map)
NUM_COLS = len(original_heat_loss_map[0])


def min_heat_loss(heat_loss_map: list[list[int]]):
    r = 0
    c = 0
    end_r = NUM_ROWS - 1
    end_c = NUM_COLS - 1
    prev_heat_losses: list[list[list[tuple[Direction, int, int]]]] = [
        [[] for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)
    ]

    curr_nodes: list[tuple[int, int, int, Direction, int]] = []
    heapq.heappush(curr_nodes, (0, 0, 0, None, 0))

    while curr_nodes:
        curr_node = heapq.heappop(curr_nodes)
        curr_total_heat_loss, r, c, curr_direction, curr_direction_count = curr_node
        next_directions = [(dir, 1) for dir in Direction.all()]
        if curr_direction:
            next_directions = curr_direction.possible_next_directions(
                curr_direction_count
            )
        for next_direction, next_direction_count in next_directions:
            next_r, next_c = r, c
            if next_direction == Direction.UP:
                next_r -= 1
            elif next_direction == Direction.LEFT:
                next_c -= 1
            elif next_direction == Direction.DOWN:
                next_r += 1
            else:
                next_c += 1
            if next_r >= 0 and next_r < NUM_ROWS and next_c >= 0 and next_c < NUM_COLS:
                next_total_heat_loss = (
                    curr_total_heat_loss + heat_loss_map[next_r][next_c]
                )
                prev_heat_loss_nodes = prev_heat_losses[next_r][next_c]
                prev_directions = [
                    (prev_direction, prev_direction_count)
                    for prev_direction, prev_direction_count, _ in prev_heat_loss_nodes
                ]
                if (next_direction, next_direction_count) in prev_directions:
                    prev_i = prev_directions.index(
                        (next_direction, next_direction_count)
                    )
                    (
                        _,
                        _,
                        prev_total_heat_loss,
                    ) = prev_heat_loss_nodes[prev_i]
                    if next_total_heat_loss < prev_total_heat_loss:
                        prev_heat_losses[next_r][next_c][prev_i] = (
                            next_direction,
                            next_direction_count,
                            next_total_heat_loss,
                        )
                        heapq.heappush(
                            curr_nodes,
                            (
                                next_total_heat_loss,
                                next_r,
                                next_c,
                                next_direction,
                                next_direction_count,
                            ),
                        )
                else:
                    prev_heat_losses[next_r][next_c].append(
                        (next_direction, next_direction_count, next_total_heat_loss)
                    )
                    heapq.heappush(
                        curr_nodes,
                        (
                            next_total_heat_loss,
                            next_r,
                            next_c,
                            next_direction,
                            next_direction_count,
                        ),
                    )
    return min(
        [total_heat_loss for _, _, total_heat_loss in prev_heat_losses[end_r][end_c]]
    )


print(min_heat_loss(original_heat_loss_map))
