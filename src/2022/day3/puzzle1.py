from src.common.read_input import read_input

priorities = {}
for i in range(26):
    priorities[chr(ord('a') + i)] = i + 1
    priorities[chr(ord('A') + i)] = i + 27


def find_common_item(compartment_a, compartment_b):
    a_items = [0]*52
    for a_item in compartment_a:
        a_items[priorities[a_item]-1] += 1
    for b_item in compartment_b:
        if a_items[priorities[b_item]-1] > 0:
            return b_item
    return None


input = read_input('input.txt', 2022, 3)

rucksacks = [[line[:len(line)//2], line[len(line)//2:]] for line in input]
common_items = [find_common_item(rucksack[0], rucksack[1])
                for rucksack in rucksacks]
priorities = [priorities[common_item] for common_item in common_items]
print(sum(priorities))
