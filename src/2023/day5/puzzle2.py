import math

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
def find_seeds_in_seeds(search_seeds: tuple[int], seeds_info: list[tuple[int]]):
    search_start, search_length = search_seeds
    search_end = search_start + search_length - 1
    for start, length in seeds_info:
        end = start + length - 1
        if search_end < start:
            return -1
        if search_end >= start and search_start <= end:
            return max(search_start, start)
    return -1


def range_to_valid_seed_range(
    seeds_info: list[tuple[int]],
    maps_reverse: list[list[tuple[int]]],
    maps_reverse_i: int,
    curr_range: tuple[int],
):
    if maps_reverse_i < 0:
        return find_seeds_in_seeds(curr_range, seeds_info)
    curr_start, curr_length = curr_range
    curr_end = curr_start + curr_length - 1
    for dest_start, src_start, length in maps_reverse[maps_reverse_i]:
        dest_end = dest_start + length - 1
        if curr_end < dest_start:
            next_start = curr_start
            next_range = curr_end - curr_start + 1
            return range_to_valid_seed_range(
                seeds_info, maps_reverse, maps_reverse_i - 1, (next_start, next_range)
            )
        elif curr_end >= dest_start and curr_start <= dest_end:
            if curr_start < dest_start:
                next_start = curr_start
                next_range = dest_start - curr_start  # does not include dest_start
                seed = range_to_valid_seed_range(
                    seeds_info,
                    maps_reverse,
                    maps_reverse_i - 1,
                    (next_start, next_range),
                )
                if seed >= 0:
                    return seed
                curr_start = dest_start
            if curr_end <= dest_end:
                next_start = (curr_start - dest_start) + src_start
                next_range = curr_end - curr_start + 1
                return range_to_valid_seed_range(
                    seeds_info,
                    maps_reverse,
                    maps_reverse_i - 1,
                    (next_start, next_range),
                )
            else:
                next_start = (curr_start - dest_start) + src_start
                next_range = dest_end - curr_start + 1  # includes dest_end
                seed = range_to_valid_seed_range(
                    seeds_info,
                    maps_reverse,
                    maps_reverse_i - 1,
                    (next_start, next_range),
                )
                if seed >= 0:
                    return seed
                curr_start = dest_end + 1  # does not include dest_end
                # continues the for loop to the next range
    next_start = curr_start
    next_range = curr_end - curr_start + 1
    return range_to_valid_seed_range(
        seeds_info,
        maps_reverse,
        maps_reverse_i - 1,
        (next_start, next_range),
    )


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

maps_reverse = [
    seed_to_soil_reverse,
    soil_to_fertilizer_reverse,
    fertilizer_to_water_reverse,
    water_to_light_reverse,
    light_to_temperature_reverse,
    temperature_to_humidity_reverse,
    humidity_to_location_reverse,
]

min_seed = range_to_valid_seed_range(
    seeds_info, maps_reverse, len(maps_reverse) - 1, (0, math.inf)
)

soil = follow_map(min_seed, seed_to_soil)
fertilizer = follow_map(soil, soil_to_fertilizer)
water = follow_map(fertilizer, fertilizer_to_water)
light = follow_map(water, water_to_light)
temperature = follow_map(light, light_to_temperature)
humidity = follow_map(temperature, temperature_to_humidity)
location = follow_map(humidity, humidity_to_location)

print(location)
