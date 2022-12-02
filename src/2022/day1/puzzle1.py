from src.common.read_input import read_input

input = read_input('input.txt', 2022, 1)

elf_calories = [[]]
for line in input:
    if line:
        elf_calories[-1].append(int(line))
    else:
        elf_calories.append([])
elf_total_calories = [sum(calories_list) for calories_list in elf_calories]
highest_calories = max(elf_total_calories)

print(highest_calories)
