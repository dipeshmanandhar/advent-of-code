from src.common.read_input import read_input


def HASH(step: str):
    val = 0
    for char in step:
        val += ord(char)
        val *= 17
        val %= 256
    return val


input = read_input("input.txt", 2023, 15)

steps = input[0].split(",")

total = 0
for step in steps:
    total += HASH(step)

print(total)
