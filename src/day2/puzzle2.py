from src.common.read_input import read_input


def aim(command):
    command_split = command.split()
    direction = command_split[0]
    change = int(command_split[1])

    aim_change = 0

    if direction == 'down':
        aim_change = change
    elif direction == 'up':
        aim_change = -change
    return aim_change


def cumulative_sum(nums):
    total = 0
    for num in nums:
        total += num
        yield total


def move(command, current_aim):
    command_split = command.split()
    direction = command_split[0]
    distance = int(command_split[1])

    horizontal_movement = 0
    depth_movement = 0

    if direction == 'forward':
        horizontal_movement = distance
        depth_movement = current_aim*distance
    return (horizontal_movement, depth_movement)


input = read_input('day2/input2.txt')

aim_changes = map(aim, input)
cumulative_aims = cumulative_sum(aim_changes)
movements = map(move, input, cumulative_aims)
horizontal_position, depth = (sum(i) for i in zip(*movements))

print(horizontal_position * depth)
