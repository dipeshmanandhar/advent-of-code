from src.common.read_input import read_input


# assumes map is sorted by src_start
def follow_map(src: int, map: list[tuple[int]]):
    dest = src
    for dest_start, src_start, range_len in map:
        if src < src_start:
            break
        elif src >= src_start and src < src_start + range_len:
            dest = src - src_start + dest_start
            break
    return dest


# assumes map is sorted by src_start
def follow_map_reverse(src: int, map: list[tuple[int]]):
    dest = src
    for src_start, dest_start, range_len in map:
        if src < src_start:
            break
        elif src >= src_start and src < src_start + range_len:
            dest = src - src_start + dest_start
            break
    return dest


# assumes seeds_info is sorted by start seed
def check_seed_in_seeds(search_seed: int, seeds_info: list[tuple[int]]):
    for start, length in seeds_info:
        if search_seed < start:
            return False
        if search_seed >= start and search_seed < start + length:
            return True


input = read_input("input.txt", 2023, 5)

seeds_info = [int(seed) for seed in input[0].split(":")[1].split()]
seeds_info = sorted(zip(seeds_info[::2], seeds_info[1::2]), key=lambda x: x[0])

seed_to_soil_start_i = input.index("seed-to-soil map:")
soil_to_fertilizer_start_i = input.index("soil-to-fertilizer map:")
fertilizer_to_water_start_i = input.index("fertilizer-to-water map:")
water_to_light_start_i = input.index("water-to-light map:")
light_to_temperature_start_i = input.index("light-to-temperature map:")
temperature_to_humidity_start_i = input.index("temperature-to-humidity map:")
humidity_to_location_start_i = input.index("humidity-to-location map:")

seed_to_soil = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[seed_to_soil_start_i + 1 : soil_to_fertilizer_start_i - 1]
    ],
    key=lambda x: x[1],
)
soil_to_fertilizer = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[
            soil_to_fertilizer_start_i + 1 : fertilizer_to_water_start_i - 1
        ]
    ],
    key=lambda x: x[1],
)
fertilizer_to_water = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[fertilizer_to_water_start_i + 1 : water_to_light_start_i - 1]
    ],
    key=lambda x: x[1],
)
water_to_light = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[water_to_light_start_i + 1 : light_to_temperature_start_i - 1]
    ],
    key=lambda x: x[1],
)
light_to_temperature = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[
            light_to_temperature_start_i + 1 : temperature_to_humidity_start_i - 1
        ]
    ],
    key=lambda x: x[1],
)
temperature_to_humidity = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[
            temperature_to_humidity_start_i + 1 : humidity_to_location_start_i - 1
        ]
    ],
    key=lambda x: x[1],
)
humidity_to_location = sorted(
    [
        tuple(int(x) for x in line.split())
        for line in input[humidity_to_location_start_i + 1 :]
    ],
    key=lambda x: x[1],
)

seed_to_soil_reverse = sorted(seed_to_soil, key=lambda x: x[0])
soil_to_fertilizer_reverse = sorted(soil_to_fertilizer, key=lambda x: x[0])
fertilizer_to_water_reverse = sorted(fertilizer_to_water, key=lambda x: x[0])
water_to_light_reverse = sorted(water_to_light, key=lambda x: x[0])
light_to_temperature_reverse = sorted(light_to_temperature, key=lambda x: x[0])
temperature_to_humidity_reverse = sorted(temperature_to_humidity, key=lambda x: x[0])
humidity_to_location_reverse = sorted(humidity_to_location, key=lambda x: x[0])

location = 0
while True:
    humidity = follow_map_reverse(location, humidity_to_location_reverse)
    temperature = follow_map_reverse(humidity, temperature_to_humidity_reverse)
    light = follow_map_reverse(temperature, light_to_temperature_reverse)
    water = follow_map_reverse(light, water_to_light_reverse)
    fertilizer = follow_map_reverse(water, fertilizer_to_water_reverse)
    soil = follow_map_reverse(fertilizer, soil_to_fertilizer_reverse)
    seed = follow_map_reverse(soil, seed_to_soil_reverse)
    if check_seed_in_seeds(seed, seeds_info):
        break
    else:
        location += 1

print(location)
