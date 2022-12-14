from src.common.read_input import read_input

input = read_input('input.txt', 2021, 1)
depths = [int(line) for line in input]
sums = list(map(lambda x, y, z: x+y+z, depths, depths[1:], depths[2:]))
times_increased = sum(map(lambda x, y: y>x, sums, sums[1:]))

print(times_increased)

