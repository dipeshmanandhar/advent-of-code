from src.common.read_input import read_input


def is_empty(l: list[str]):
    return all([x == "." for x in l])


def get_col(universe: list[list[str]], col: int):
    return [row[col] for row in universe]


def transpose(universe: list[list[str]]):
    return [get_col(universe, c) for c in range(len(universe[0]))]


def expand(universe: list[list[str]]):
    expanded = [row.copy() for row in universe]
    for r, row in enumerate(reversed(universe)):
        r = len(row) - r
        if is_empty(row):
            expanded.insert(r, row)
    for c, col in enumerate(reversed(transpose(universe))):
        c = len(col) - c
        if is_empty(col):
            for row in expanded:
                row.insert(c, ".")
    return expanded


def manhattan_dist(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


input = read_input("input.txt", 2023, 11)

universe = [[char for char in line] for line in input]
universe = expand(universe)
galaxies = []

for r, row in enumerate(universe):
    for c, char in enumerate(row):
        if char == "#":
            galaxies.append((r, c))

total = 0
for i, galaxy_a in enumerate(galaxies):
    for galaxy_b in galaxies[i + 1 :]:
        curr_dist = manhattan_dist(galaxy_a, galaxy_b)
        total += curr_dist

print(total)
