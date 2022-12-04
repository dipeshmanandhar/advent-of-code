from src.common.read_input import read_input


def fully_contained(range_a, range_b):
    range_a_start, range_a_end = [int(num) for num in range_a.split('-')]
    range_b_start, range_b_end = [int(num) for num in range_b.split('-')]
    if range_a_start <= range_b_start and range_a_end >= range_b_end:   # b is entirely in a
        return True
    elif range_a_start >= range_b_start and range_a_end <= range_b_end:   # a is entirely in b
        return True
    else:
        return False


input = read_input('input.txt', 2022, 4)

pairs = [line.split(',') for line in input]
pairs_is_fully_contained = [fully_contained(pair[0], pair[1])
                            for pair in pairs]
print(sum(pairs_is_fully_contained))
