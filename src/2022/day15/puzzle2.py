from src.common.read_input import read_input


def manhattan_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


input = read_input('input.txt', 2022, 15)

sensors = [(0, 0, 0, 0) for _ in range(len(input))]

for i, line in enumerate(input):
    coords_raw = line.replace('Sensor at x=', '').replace(', y=', ' ')\
        .replace(': closest beacon is at x=', ' ').replace(', y=', ' ')
    sensors[i] = tuple(int(num) for num in coords_raw.split())

max_pos = 4000000

y = 0
while y <= max_pos:
    is_beacon = True
    x = 0
    while x <= max_pos:
        is_beacon = True
        for sensor in sensors:
            sensor_x, sensor_y, beacon_x, beacon_y = sensor
            dist_max = manhattan_dist(sensor_x, sensor_y, beacon_x, beacon_y)
            dist_cur = manhattan_dist(sensor_x, sensor_y, x, y)
            if dist_cur <= dist_max:
                is_beacon = False
                y_dist = abs(y - sensor_y)
                x_dist = dist_max - y_dist
                x = sensor_x + x_dist
                break
        if is_beacon:
            tuning_freq = x * 4000000 + y
            print(tuning_freq)
            break
        x += 1
    if is_beacon:
        break
    y += 1
