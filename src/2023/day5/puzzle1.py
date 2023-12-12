from src.common.read_input import read_input


def follow_map(src: int, map: list[tuple[int]]):
    dest = src
    for dest_start, src_start, range_len in map:
        if src >= src_start and src <= src_start + range_len:
            dest = src - src_start + dest_start
            break
    return dest


input = read_input("input.txt", 2023, 5)

seeds = [int(seed) for seed in input[0].split(":")[1].split()]

seed_to_soil_start_i = input.index("seed-to-soil map:")
soil_to_fertilizer_start_i = input.index("soil-to-fertilizer map:")
fertilizer_to_water_start_i = input.index("fertilizer-to-water map:")
water_to_light_start_i = input.index("water-to-light map:")
light_to_temperature_start_i = input.index("light-to-temperature map:")
temperature_to_humidity_start_i = input.index("temperature-to-humidity map:")
humidity_to_location_start_i = input.index("humidity-to-location map:")

seed_to_soil = [
    tuple(int(x) for x in line.split())
    for line in input[seed_to_soil_start_i + 1 : soil_to_fertilizer_start_i - 1]
]
soil_to_fertilizer = [
    tuple(int(x) for x in line.split())
    for line in input[soil_to_fertilizer_start_i + 1 : fertilizer_to_water_start_i - 1]
]
fertilizer_to_water = [
    tuple(int(x) for x in line.split())
    for line in input[fertilizer_to_water_start_i + 1 : water_to_light_start_i - 1]
]
water_to_light = [
    tuple(int(x) for x in line.split())
    for line in input[water_to_light_start_i + 1 : light_to_temperature_start_i - 1]
]
light_to_temperature = [
    tuple(int(x) for x in line.split())
    for line in input[
        light_to_temperature_start_i + 1 : temperature_to_humidity_start_i - 1
    ]
]
temperature_to_humidity = [
    tuple(int(x) for x in line.split())
    for line in input[
        temperature_to_humidity_start_i + 1 : humidity_to_location_start_i - 1
    ]
]
humidity_to_location = [
    tuple(int(x) for x in line.split())
    for line in input[humidity_to_location_start_i + 1 :]
]

locations = [0 for _ in range(len(seeds))]
for i, seed in enumerate(seeds):
    soil = follow_map(seed, seed_to_soil)
    fertilizer = follow_map(soil, soil_to_fertilizer)
    water = follow_map(fertilizer, fertilizer_to_water)
    light = follow_map(water, water_to_light)
    temperature = follow_map(light, light_to_temperature)
    humidity = follow_map(temperature, temperature_to_humidity)
    location = follow_map(humidity, humidity_to_location)
    locations[i] = location

print(min(locations))
