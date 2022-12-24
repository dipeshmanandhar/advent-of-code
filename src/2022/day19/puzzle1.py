import math

from src.common.read_input import read_input


class Blueprint:
    def __init__(self, id, ore_bot_ore_cost, clay_bot_ore_cost, obsidian_bot_ore_cost, obsidian_bot_clay_cost, geode_bot_ore_cost, geode_bot_obsidian_cost):
        self.id = id
        self.ore_bot_ore_cost = ore_bot_ore_cost
        self.clay_bot_ore_cost = clay_bot_ore_cost
        self.obsidian_bot_ore_cost = obsidian_bot_ore_cost
        self.obsidian_bot_clay_cost = obsidian_bot_clay_cost
        self.geode_bot_ore_cost = geode_bot_ore_cost
        self.geode_bot_obsidian_cost = geode_bot_obsidian_cost

    def __str__(self):
        return f'Blueprint {self.id}: Each ore robot costs {self.ore_bot_ore_cost} ore. Each clay robot costs {self.clay_bot_ore_cost} ore. Each obsidian robot costs {self.obsidian_bot_ore_cost} ore and {self.obsidian_bot_clay_cost} clay. Each geode robot costs {self.geode_bot_ore_cost} ore and {self.geode_bot_obsidian_cost} obsidian.'


def max_geodes(bp: Blueprint, ore=0, clay=0, obsidian=0, geode=0, ore_bots=1, clay_bots=0, obsidian_bots=0, geode_bots=0, minutes_left=24):
    if minutes_left <= 0:
        return geode, [], [], [], []
    make_something_geode = [0] * 4
    make_something_ore_bots = [[] for _ in range(4)]
    make_something_clay_bots = [[] for _ in range(4)]
    make_something_obsidian_bots = [[] for _ in range(4)]
    make_something_geode_bots = [[] for _ in range(4)]
    num_something = 0
    MAX_SOMETHING = 4

    for i in range(4):
        if num_something >= MAX_SOMETHING:
            break
        num_something += 1
        minutes_diff = 0
        next_ore_bots = ore_bots
        next_clay_bots = clay_bots
        next_obsidian_bots = obsidian_bots
        next_geode_bots = geode_bots
        ore_cost = 0
        clay_cost = 0
        obsidian_cost = 0
        if i == 0:
            if obsidian_bots == 0:
                num_something -= 1
                continue
            ore_diff = max(bp.geode_bot_ore_cost - ore, 0)
            obsidian_diff = max(bp.geode_bot_obsidian_cost - obsidian, 0)
            ore_cost = bp.geode_bot_ore_cost
            obsidian_cost = bp.geode_bot_obsidian_cost
            minutes_diff = max(math.ceil(ore_diff / ore_bots),
                               math.ceil(obsidian_diff / obsidian_bots)) + 1
            next_geode_bots += 1
        elif i == 1:
            if clay_bots == 0:
                num_something -= 1
                continue
            if obsidian_bots >= bp.geode_bot_obsidian_cost:
                continue
            ore_diff = max(bp.obsidian_bot_ore_cost - ore, 0)
            clay_diff = max(bp.obsidian_bot_clay_cost - clay, 0)
            ore_cost = bp.obsidian_bot_ore_cost
            clay_cost = bp.obsidian_bot_clay_cost
            minutes_diff = max(math.ceil(ore_diff / ore_bots),
                               math.ceil(clay_diff / clay_bots)) + 1
            next_obsidian_bots += 1
        elif i == 2:
            if clay_bots >= bp.obsidian_bot_clay_cost:
                continue
            ore_diff = max(bp.clay_bot_ore_cost - ore, 0)
            ore_cost = bp.clay_bot_ore_cost
            minutes_diff = math.ceil(ore_diff / ore_bots) + 1
            next_clay_bots += 1
        elif i == 3:
            if ore_bots >= max(bp.ore_bot_ore_cost, bp.clay_bot_ore_cost, bp.obsidian_bot_ore_cost, bp.geode_bot_ore_cost):
                continue
            ore_diff = max(bp.ore_bot_ore_cost - ore, 0)
            ore_cost = bp.ore_bot_ore_cost
            minutes_diff = math.ceil(ore_diff / ore_bots) + 1
            next_ore_bots += 1
        next_ore = ore - ore_cost + ore_bots * minutes_diff
        next_clay = clay - clay_cost + clay_bots * minutes_diff
        next_obsidian = obsidian - obsidian_cost + obsidian_bots * minutes_diff
        next_geode = geode + geode_bots * minutes_diff
        next_minutes = minutes_left - minutes_diff
        if next_minutes <= 0:
            make_something_geode[i], make_something_ore_bots[i], make_something_clay_bots[i], make_something_obsidian_bots[i], make_something_geode_bots[i] = (
                geode + geode_bots * minutes_left, [], [], [], [])
        else:
            make_something_geode[i], make_something_ore_bots[i], make_something_clay_bots[i], make_something_obsidian_bots[i], make_something_geode_bots[i] = max_geodes(bp,
                                                                                                                                                                         next_ore, next_clay, next_obsidian, next_geode,
                                                                                                                                                                         next_ore_bots, next_clay_bots, next_obsidian_bots, next_geode_bots,
                                                                                                                                                                         next_minutes)
    max_index = -1
    max_make_something_geode = 0
    for i, g in enumerate(make_something_geode):
        if g > max_make_something_geode:
            max_make_something_geode = g
            max_index = i
    return make_something_geode[max_index], [ore_bots, *make_something_ore_bots[max_index]], [clay_bots, *make_something_clay_bots[max_index]], [obsidian_bots, *make_something_obsidian_bots[max_index]], [geode_bots, *make_something_geode_bots[max_index]]


def quality(bp: Blueprint):
    geode, ore_bots, clay_bots, obsidian_bots, geode_bots = max_geodes(bp)
    print(bp)
    print(geode)

    print(f"[{','.join([f'{i+1:2}' if i>0 else f'{i+1}' for i in range(24)])}]")
    print(ore_bots)
    print(clay_bots)
    print(obsidian_bots)
    print(geode_bots)
    print()
    return bp.id * geode


input = read_input('input.txt', 2022, 19)

total_quality = 0
for line in input:
    line = line.replace('Blueprint ', '').replace(': Each ore robot costs ', ' ').replace(' ore. Each clay robot costs ', ' ')\
        .replace(' ore. Each obsidian robot costs ', ' ').replace(' ore and ', ' ').replace(' clay. Each geode robot costs ', ' ').replace(' obsidian.', '')
    line = [int(num) for num in line.split()]
    bp = Blueprint(*line)
    total_quality += quality(bp)

print(total_quality)
