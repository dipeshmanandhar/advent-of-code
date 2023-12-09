from src.common.read_input import read_input

input = read_input('input.txt', 2023, 2)

total = 0
for line in input:
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    possible = True
    game_info, game = line.split(":")
    game_id = int(game_info.split()[1])
    sets = game.split(";")
    for set in sets:
        colors = set.split(",")
        for color in colors:
            color = color.split()
            curr_cubes = int(color[0])
            curr_color = color[1]
            if curr_cubes > max_cubes[curr_color]:
                max_cubes[curr_color] = curr_cubes
    power = 1
    for num_cubes in max_cubes.values():
        power *= num_cubes
    total += power

print(total)
