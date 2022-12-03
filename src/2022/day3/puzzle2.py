from src.common.read_input import read_input

priorities = {}
for i in range(26):
    priorities[chr(ord('a') + i)] = i + 1
    priorities[chr(ord('A') + i)] = i + 27


def find_common_item(rucksack_a, rucksack_b, rucksack_c):
    a_items = [0]*52
    b_items = [0]*52
    for a_item in rucksack_a:
        a_items[priorities[a_item]-1] += 1
    for b_item in rucksack_b:
        b_items[priorities[b_item]-1] += 1
    for c_item in rucksack_c:
        if a_items[priorities[c_item]-1] > 0 and b_items[priorities[c_item]-1] > 0:
            return c_item
    return None


input = read_input('input.txt', 2022, 3)

num_groups = len(input) // 3
groups = [input[i*3:i*3+3] for i in range(num_groups)]
common_items = [find_common_item(group[0], group[1], group[2])
                for group in groups]
priorities = [priorities[common_item] for common_item in common_items]
print(sum(priorities))
