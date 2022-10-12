from src.common.read_input import read_input

input = read_input('day1/input1.txt')
depths = [int(line) for line in input]
times_increased = sum(map(lambda x, y: y>x, depths, depths[1:]))

print(times_increased)
