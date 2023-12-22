from src.common.read_input import read_input


def HASH(step: str):
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val %= 256
    return val


def remove_label(hashmap: list[list[tuple[str, int]]], label: str):
    hash = HASH(label)
    keys = [k for k, _ in hashmap[hash]]
    if label in keys:
        hashmap_i = keys.index(label)
        hashmap[hash].pop(hashmap_i)


def set_lens(hashmap: list[list[tuple[str, int]]], label: str, lens: int):
    hash = HASH(label)
    keys = [k for k, _ in hashmap[hash]]
    if label in keys:
        hashmap_i = keys.index(label)
        hashmap[hash][hashmap_i] = (label, lens)
    else:
        hashmap[hash].append((label, lens))


def calc_focusing_power(hashmap: list[list[tuple[str, int]]]):
    fp = 0
    for box_number, lenses in enumerate(hashmap):
        for slot_number, (_, lens) in enumerate(lenses):
            fp += (box_number + 1) * (slot_number + 1) * lens
    return fp


input = read_input("input.txt", 2023, 15)

steps = input[0].split(",")
hashmap: list[list[tuple[str, int]]] = [[] for _ in range(256)]

for step in steps:
    if "=" in step:
        label, lens = step.split("=")
        lens = int(lens)
        set_lens(hashmap, label, lens)
    else:
        label = step[:-1]
        remove_label(hashmap, label)

print(calc_focusing_power(hashmap))
