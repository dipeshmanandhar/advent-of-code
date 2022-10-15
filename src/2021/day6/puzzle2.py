from src.common.read_input import read_input

num_descendents = [[-1] * 257 for _ in range(9)]


def calc_total_decendents(initial_age, days):
    if num_descendents[initial_age][days] >= 0:
        return num_descendents[initial_age][days]
    day_first_child = initial_age + 1
    if day_first_child > days:
        num_descendents[initial_age][days] = 0
        return 0
    num_children = (days-day_first_child)//7 + 1
    total_descendents = num_children
    for i in range(num_children):
        total_descendents += calc_total_decendents(8, days-day_first_child-i*7)
    num_descendents[initial_age][days] = total_descendents
    return total_descendents


input = read_input('input.txt', 2021, 6)

ages = list(map(int, input[0].split(',')))
total_new_fish = sum([calc_total_decendents(age, 256) for age in ages])
num_fish = len(ages) + total_new_fish

print(num_fish)
