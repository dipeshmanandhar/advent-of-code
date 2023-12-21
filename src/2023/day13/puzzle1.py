from src.common.read_input import read_input


def get_col(pattern: list[list[str]], c: int):
    return [row[c] for row in pattern]


def transpose(pattern: list[list[str]]):
    return [get_col(pattern, c) for c in range(len(pattern[0]))]


def check_horiz_reflection(pattern: list[list[str]], reflection_r: int):
    for offset in range(min(len(pattern) - reflection_r, reflection_r)):
        if pattern[reflection_r + offset] != pattern[reflection_r - offset - 1]:
            return False
    return True


def find_horiz_rows(pattern: list[list[str]]):
    for r in range(len(pattern)):
        if r == 0:
            continue
        if check_horiz_reflection(pattern, r):
            return r
    return -1


def find_vert_cols(pattern: list[list[str]]):
    return find_horiz_rows(transpose(pattern))


input = read_input("input.txt", 2023, 13)

patterns: list[list[list[str]]] = [[]]
i = 0
for line in input:
    if line:
        patterns[i].append([char for char in line])
    else:
        i += 1
        patterns.append([])

total = 0
for pattern in patterns:
    horiz_rows = find_horiz_rows(pattern)
    if horiz_rows >= 0:
        total += horiz_rows * 100
    vert_cols = find_vert_cols(pattern)
    if vert_cols >= 0:
        total += vert_cols

print(total)
