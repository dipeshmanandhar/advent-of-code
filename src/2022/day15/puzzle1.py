from src.common.read_input import read_input


def manhattan_dist(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)


input = read_input('input.txt', 2022, 15)

sensors = [(0, 0, 0, 0) for _ in range(len(input))]

for i, line in enumerate(input):
    coords_raw = line.replace('Sensor at x=', '').replace(', y=', ' ')\
        .replace(': closest beacon is at x=', ' ').replace(', y=', ' ')
    sensors[i] = tuple(int(num) for num in coords_raw.split())

check_y = 2000000
beacon_present = set()
beacon_not_present = set()
for sensor in sensors:
    sensor_x, sensor_y, beacon_x, beacon_y = sensor
    dist = manhattan_dist(sensor_x, sensor_y, beacon_x, beacon_y)
    if beacon_y == check_y:
        beacon_present.add(beacon_x)
    y_dist = abs(check_y - sensor_y)
    x_dist = dist - y_dist
    if x_dist >= 0:
        for x_offset in range(x_dist+1):
            beacon_not_present.add(sensor_x+x_offset)
            beacon_not_present.add(sensor_x-x_offset)

beacon_not_present -= beacon_present

print(len(beacon_not_present))
