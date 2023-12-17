from src.common.read_input import read_input

EXPANSION_RATE = 1000000


def is_empty(l: list[str]):
    return all([x == "." for x in l])


def get_col(universe: list[list[str]], col: int):
    return [row[col] for row in universe]


def transpose(universe: list[list[str]]):
    return [get_col(universe, c) for c in range(len(universe[0]))]


def expand(universe: list[list[str]], galaxies: list[tuple[int, int]]):
    expanded_galaxies = [(r, c) for r, c in galaxies]
    for r, row in enumerate(universe):
        if is_empty(row):
            for i, (galaxy_r, galaxy_c) in enumerate(galaxies):
                if galaxy_r > r:
                    expanded_galaxy_r, expanded_galaxy_c = expanded_galaxies[i]
                    expanded_galaxy_r += EXPANSION_RATE - 1
                    expanded_galaxies[i] = (expanded_galaxy_r, expanded_galaxy_c)
    for c, col in enumerate(transpose(universe)):
        if is_empty(col):
            for i, (galaxy_r, galaxy_c) in enumerate(galaxies):
                if galaxy_c > c:
                    expanded_galaxy_r, expanded_galaxy_c = expanded_galaxies[i]
                    expanded_galaxy_c += EXPANSION_RATE - 1
                    expanded_galaxies[i] = (expanded_galaxy_r, expanded_galaxy_c)
    return expanded_galaxies


def manhattan_dist(p1: tuple[int, int], p2: tuple[int, int]):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


input = read_input("input.txt", 2023, 11)

universe = [[char for char in line] for line in input]
galaxies = []

for r, row in enumerate(universe):
    for c, char in enumerate(row):
        if char == "#":
            galaxies.append((r, c))

galaxies = expand(universe, galaxies)

total = 0
for i, galaxy_a in enumerate(galaxies):
    for galaxy_b in galaxies[i + 1 :]:
        curr_dist = manhattan_dist(galaxy_a, galaxy_b)
        total += curr_dist

print(total)
