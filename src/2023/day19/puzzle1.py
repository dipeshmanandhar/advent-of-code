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


def read_parts(input: list[str]) -> list[dict[str, int]]:
    return [
        {rating[0]: int(rating[2:]) for rating in line.strip("{}").split(",")}
        for line in input
    ]


def evaluate_workflow(
    workflow: list[dict[str, (str | dict[str, (str | int)])]], part: dict[str, int]
) -> str:
    for rule in workflow:
        condition = rule[CONDITION]
        if condition:
            condition_true = False
            if condition[COMPARATOR] == LESS_THAN:
                condition_true = part[condition[CATEGORY]] < condition[RATING]
            else:
                condition_true = part[condition[CATEGORY]] > condition[RATING]
            if condition_true:
                return rule[NEXT]
        else:
            return rule[NEXT]
    return "ERROR"


def is_accepted(
    workflows: dict[str, list[dict[str, (str | dict[str, (str | int)])]]],
    part: dict[str, int],
) -> bool:
    curr_workflow_name = START_WORKFLOW
    while curr_workflow_name not in [REJECTED, ACCEPTED]:
        curr_workflow_name = evaluate_workflow(workflows[curr_workflow_name], part)
    return curr_workflow_name == ACCEPTED


input = read_input("input.txt", 2023, 19)

empty_line = input.index("")

workflows = input[:empty_line]
parts = input[empty_line + 1 :]

workflows = read_workflows(workflows)
parts = read_parts(parts)

total = 0
for part in parts:
    if is_accepted(workflows, part):
        total += sum(part.values())

print(total)
