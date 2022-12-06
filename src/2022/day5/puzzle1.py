from collections import deque

from src.common.read_input import read_input

input = read_input('input.txt', 2022, 5)

num_stacks = None
raw_stacks = None
raw_moves = None

for index, line in enumerate(input):
    if not line:
        numbers = input[index-1].split()
        num_stacks = len(numbers)
        raw_stacks = input[:index-1]
        raw_moves = input[index+1:]

stacks = [deque() for i in range(num_stacks)]
for line in reversed(raw_stacks):
    for i in range(num_stacks):
        curr_item = line[1+i*4].strip()
        if curr_item:
            stacks[i].append(curr_item)

for move in raw_moves:
    num_items_to_move, from_stack, to_stack = [
        int(num) for num in move.split()[1::2]]
    for _ in range(num_items_to_move):
        item = stacks[from_stack-1].pop()
        stacks[to_stack-1].append(item)

top_items = ''.join([stack[-1] for stack in stacks])

print(top_items)
