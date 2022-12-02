from src.common.read_input import read_input

input = read_input('input.txt', 2022, 1)

elf_calories = [[]]
for line in input:
    if line:
        elf_calories[-1].append(int(line))
    else:
        elf_calories.append([])
elf_total_calories = [sum(calories_list) for calories_list in elf_calories]
sorted_elf_total_calories = sorted(elf_total_calories)
highest_three_calories = sorted_elf_total_calories[-3:]
total_highest_three_calories = sum(highest_three_calories)

print(total_highest_three_calories)
