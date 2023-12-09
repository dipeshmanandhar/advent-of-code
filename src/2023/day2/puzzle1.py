from src.common.read_input import read_input

input = read_input('input.txt', 2023, 2)

cubes_expected = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
for line in input:
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
            if curr_cubes > cubes_expected[curr_color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        total += game_id

print(total)
