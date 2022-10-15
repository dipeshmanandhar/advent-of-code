from src.common.read_input import read_input


def step_one_day(ages):
    num_new_fish = len([1 for age in ages if age == 0])
    new_ages = [age-1+(7 if age==0 else 0) for age in ages]
    new_ages.extend([8] * num_new_fish)
    return new_ages


input = read_input('input.txt', 2021, 6)

ages = list(map(int, input[0].split(',')))
for _ in range(80):
    ages = step_one_day(ages)
num_fish = len(ages)

print(num_fish)
