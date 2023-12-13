import math

from src.common.read_input import read_input

input = read_input("input.txt", 2023, 6)

race_time = int("".join(input[0].split(":")[1].split()))
best_distance = int("".join(input[1].split(":")[1].split()))

ways_to_win = 0
# for ms_charge in range(race_time):
#     curr_distance = (race_time - ms_charge) * ms_charge
#     if curr_distance > best_distance:
#         ways_to_win += 1

min_ms_charge = math.ceil(
    (race_time - (race_time**2 - 4 * best_distance) ** (1 / 2)) / 2
)
max_ms_charge = math.floor(
    (race_time + (race_time**2 - 4 * best_distance) ** (1 / 2)) / 2
)
ways_to_win = max_ms_charge - min_ms_charge + 1

print(ways_to_win)

# (race_time - ms_charge) * ms_charge > best_distance
# (t - x) * x > d
# -x^2 + tx > d
# x^2 - tx + d < 0

# x = -b +/- sqrt(b^2 - 4ac)
#             / 2a
# x > t - sqrt(t^2 - 4d)
#             / 2
# x < t + sqrt(t^2 - 4d)
#             / 2
