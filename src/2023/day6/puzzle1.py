from src.common.read_input import read_input

input = read_input("input.txt", 2023, 6)

race_times = [int(x) for x in input[0].split(":")[1].split()]
best_distances = [int(x) for x in input[1].split(":")[1].split()]

product = 1
for i, time in enumerate(race_times):
    ways_to_win = 0
    for ms_charge in range(time):
        curr_distance = (time - ms_charge) * ms_charge
        if curr_distance > best_distances[i]:
            ways_to_win += 1
    product *= ways_to_win

print(product)
