from src.common.read_input import read_input


def distance_to_fuel(distance):
    return (distance+1)*distance//2  # sum of 1 + 2 + 3 + ... + distance


def calc_fuel_cost(positions, target_position):
    fuel_costs = [distance_to_fuel(abs(position-target_position))
                  for position in positions]
    fuel_cost = sum(fuel_costs)
    return fuel_cost


input = read_input('input.txt', 2021, 7)

positions = [int(position) for position in input[0].split(',')]
max_position = max(positions)
total_fuel_costs = [calc_fuel_cost(positions, position)
                    for position in range(len(positions))]
min_total_fuel_cost = min(total_fuel_costs)

print(min_total_fuel_cost)
