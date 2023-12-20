from src.common.read_input import read_input

MIN_LEN = 0
MAX_LEN = 1
START_I = 2


def is_valid(
    conditions: str,
    known_groups: list[tuple[int, int, int]],
    group: int,
    group_start_i: int,
):
    indexes = [
        i
        for _, max_len, start_i in known_groups
        for i in range(start_i, start_i + max_len)
    ]
    valid = True
    for i in indexes:
        if i >= group_start_i and i < group_start_i + group:
            if conditions[i] == ".":
                valid = False
                break
        else:
            if conditions[i] == "#":
                valid = False
                break
    if valid:
        for i in range(group_start_i, group_start_i + group):
            if not (i in indexes):
                valid = False
                break
    return valid


def ways_to_map_group(
    conditions: str, known_groups: list[tuple[int, int, int]], group: int
):
    num_ways = 0
    known_groups_i = 0
    group_start_i = known_groups[0][START_I]
    total_spaces = sum([max_len for _, max_len, _ in known_groups])
    for _ in range(total_spaces - group + 1):
        if is_valid(conditions, known_groups, group, group_start_i):
            num_ways += 1

        group_start_i += 1
        if (
            group_start_i
            > known_groups[known_groups_i][START_I]
            + known_groups[known_groups_i][MAX_LEN]
            - group
        ):
            known_groups_i += 1
            if known_groups_i >= len(known_groups):
                break
            group_start_i = known_groups[known_groups_i][START_I]
    return num_ways


# min_len is irrelevantand thus ignored for this method (and may be filled with -1 as a dummy value)
def ways_to_map_groups(
    conditions: str, known_groups: list[tuple[int, int, int]], groups: list[int]
):
    num_ways = 0
    total_spaces = sum([max_len for _, max_len, _ in known_groups])
    total_groups = sum(groups)
    if not groups:
        return 1
    if len(groups) == 1:
        return ways_to_map_group(conditions, known_groups, groups[0])

    known_groups_i = 0
    start_i = known_groups[0][START_I]
    for _ in range(total_spaces - total_groups + 1):
        # calculate the next groups and known groups if you place the first group starting at start_i
        next_start_i = start_i + groups[0] + 1
        known_group = known_groups[known_groups_i]
        known_group_end_i = (
            known_groups[known_groups_i][START_I]
            + known_groups[known_groups_i][MAX_LEN]
            - 1
        )
        next_known_groups = known_groups[known_groups_i:]
        if next_start_i > known_group_end_i:
            next_known_groups.pop(0)
            if not next_known_groups:
                break
            next_start_i = next_known_groups[0][START_I]
        else:
            next_max_len = (
                next_known_groups[0][START_I]
                + next_known_groups[0][MAX_LEN]
                - next_start_i
            )
            next_known_groups[0] = (-1, next_max_len, next_start_i)
            prev_max_len = next_start_i - known_group[START_I]
            known_group = (-1, prev_max_len, known_group[START_I])

        if is_valid(
            conditions,
            known_groups[:known_groups_i] + [known_group],
            groups[0],
            start_i,
        ):
            num_ways += ways_to_map_groups(conditions, next_known_groups, groups[1:])

        start_i += 1
        if start_i > known_group_end_i + 1 - groups[0]:
            if not is_valid(conditions, known_groups[: known_groups_i + 1], -1, -1):
                break
            known_groups_i += 1
            if known_groups_i >= len(known_groups):
                break
            start_i = known_groups[known_groups_i][START_I]
    return num_ways


input = read_input("input.txt", 2023, 12)

total = 0
for line_num, line in enumerate(input):
    conditions, groups = line.split()
    groups = [int(group) for group in groups.split(",")]

    # first calculate what potential group lengths we know based on the conditions input
    known_groups = []
    curr_group_min_len = 0
    curr_group_max_len = 0
    start_i = -1
    for i, condition in enumerate(conditions):
        if condition == "#":
            if curr_group_max_len == 0:
                start_i = i
            curr_group_min_len += 1
            curr_group_max_len += 1
        elif condition == ".":
            if curr_group_max_len > 0:
                known_groups.append((curr_group_min_len, curr_group_max_len, start_i))
            curr_group_min_len = 0
            curr_group_max_len = 0
        elif condition == "?":
            if curr_group_max_len == 0:
                start_i = i
            curr_group_max_len += 1
    if curr_group_max_len > 0:
        known_groups.append((curr_group_min_len, curr_group_max_len, start_i))

    # now map the remaining expected groups to all of the remaining known groups
    num_ways = ways_to_map_groups(conditions, known_groups, groups)

    total += num_ways

print(total)
