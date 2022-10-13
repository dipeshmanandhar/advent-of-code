from src.common.read_input import read_input


def move(command):
    command_split = command.split()
    direction = command_split[0]
    distance = int(command_split[1])

    horizontal_movement = 0
    depth_movement = 0

    if direction == 'forward':
        horizontal_movement = distance
    elif direction == 'down':
        depth_movement = distance
    elif direction == 'up':
        depth_movement = -distance
    return (horizontal_movement, depth_movement)


input = read_input('input.txt', 2021, 2)

movements = map(move, input)
horizontal_position, depth = (sum(i) for i in zip(*movements))

print(horizontal_position * depth)
