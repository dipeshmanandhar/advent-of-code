from math import prod

from src.common.read_input import read_input

CONDITION = "CONDITION"
NEXT = "NEXT"
CATEGORY = "CATEGORY"
COMPARATOR = "COMPARATOR"
RATING = "RATING"
LESS_THAN = "<"
GREATER_THAN = ">"
REJECTED = "R"
ACCEPTED = "A"
START_WORKFLOW = "in"
RATING_MIN = 1
RATING_MAX = 4000


def read_workflows(
    input: list[str],
) -> dict[str, list[dict[str, (str | dict[str, (str | int)])]]]:
    workflows: dict[str, list[dict[str, (str | dict[str, (str | int)])]]] = {}
    for line in input:
        name, rules = line.split("{")
        rules = rules[:-1].split(",")
        workflows[name] = []
        for rule in rules[:-1]:
            condition, next = rule.split(":")
            category = condition[0]
            comparator = condition[1]
            rating = int(condition[2:])
            workflows[name].append(
                {
                    CONDITION: {
                        CATEGORY: category,
                        COMPARATOR: comparator,
                        RATING: rating,
                    },
                    NEXT: next,
                }
            )
        workflows[name].append(
            {
                CONDITION: None,
                NEXT: rules[-1],
            }
        )
    return workflows


def accepted_combinations(
    workflows: dict[str, list[dict[str, (str | dict[str, (str | int)])]]],
    curr_workflow_name: str = START_WORKFLOW,
    rating_ranges: dict[str, tuple[int, int]] = {
        "x": (RATING_MIN, RATING_MAX),
        "m": (RATING_MIN, RATING_MAX),
        "a": (RATING_MIN, RATING_MAX),
        "s": (RATING_MIN, RATING_MAX),
    },
) -> int:
    if any([r_min > r_max for r_min, r_max in rating_ranges.values()]):
        return 0
    if curr_workflow_name == REJECTED:
        return 0
    if curr_workflow_name == ACCEPTED:
        return prod([(r_max - r_min + 1) for r_min, r_max in rating_ranges.values()])
    total = 0
    rating_ranges = rating_ranges.copy()
    for rule in workflows[curr_workflow_name]:
        condition = rule[CONDITION]
        if condition:
            r_min, r_max = rating_ranges[condition[CATEGORY]]
            next_r_min, next_r_max = rating_ranges[condition[CATEGORY]]
            if condition[COMPARATOR] == LESS_THAN:
                next_r_max = min(next_r_max, condition[RATING] - 1)
                r_min = max(r_min, condition[RATING])
            else:
                next_r_min = max(next_r_min, condition[RATING] + 1)
                r_max = min(r_max, condition[RATING])
            next_rating_ranges = rating_ranges.copy()
            next_rating_ranges[condition[CATEGORY]] = (next_r_min, next_r_max)
            rating_ranges[condition[CATEGORY]] = (r_min, r_max)
            total += accepted_combinations(workflows, rule[NEXT], next_rating_ranges)
        else:
            total += accepted_combinations(workflows, rule[NEXT], rating_ranges)
    return total


input = read_input("input.txt", 2023, 19)

empty_line = input.index("")

workflows = input[:empty_line]
workflows = read_workflows(workflows)

total = accepted_combinations(workflows)

print(total)
