from collections import deque

from src.common.read_input import read_input


def play_turn(monkeys, curr_monkey, modder):
    while curr_monkey['items']:
        item = curr_monkey['items'].pop()
        operation_amount = curr_monkey['operation_amount']
        if operation_amount == 'old':
            operation_amount = item
        if curr_monkey['operation'] == '+':
            item += operation_amount
        elif curr_monkey['operation'] == '*':
            item *= operation_amount
        item %= modder
        next_monkey_index = curr_monkey['true_next'] if item % curr_monkey[
            'test_divisible'] == 0 else curr_monkey['false_next']
        monkeys[next_monkey_index]['items'].append(item)
        curr_monkey['num_inspections'] += 1


def play_round(monkeys, modder):
    # print('num_items:', [len(monkey['items']) for monkey in monkeys])
    for monkey in monkeys:
        play_turn(monkeys, monkey, modder)
    # print('num_inspections:', [monkey['num_inspections']
    #       for monkey in monkeys])


input = read_input('input.txt', 2022, 11)

num_monkeys = (len(input)+1) // 7
monkeys = [{
    'items': deque(),
    'operation': '',
    'operation_amount': 0,
    'test_divisible': 1,
    'true_next': -1,
    'false_next': -1,
    'num_inspections': 0
} for _ in range(num_monkeys)]

modder = 1
for i in range(num_monkeys):
    items = input[i*7+1].split(':')[1].strip().split(', ')
    operation = input[i*7+2].split(':')[1].split()
    test_divisible = input[i*7+3].split(':')[1].split()[-1]
    true_next = input[i*7+4].split(':')[1].split()[-1]
    false_next = input[i*7+5].split(':')[1].split()[-1]

    for item in items:
        monkeys[i]['items'].append(int(item))
    monkeys[i]['operation'] = operation[-2]
    try:
        monkeys[i]['operation_amount'] = int(operation[-1])
    except ValueError:
        monkeys[i]['operation_amount'] = operation[-1]
    monkeys[i]['test_divisible'] = int(test_divisible)
    modder *= monkeys[i]['test_divisible']
    monkeys[i]['true_next'] = int(true_next)
    monkeys[i]['false_next'] = int(false_next)

for i in range(10000):
    play_round(monkeys, modder)

max_num_inspections = 0
second_max_num_inspections = 0
for monkey in monkeys:
    if monkey['num_inspections'] > max_num_inspections:
        second_max_num_inspections = max_num_inspections
        max_num_inspections = monkey['num_inspections']
    elif monkey['num_inspections'] > second_max_num_inspections:
        second_max_num_inspections = monkey['num_inspections']

print(max_num_inspections * second_max_num_inspections)
