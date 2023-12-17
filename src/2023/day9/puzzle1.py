from src.common.read_input import read_input


def all_same(seq: list[int]):
    check = seq[0]
    for num in seq[1:]:
        if num != check:
            return False
    return True


def predict_next(seq: list[int]):
    if all_same(seq):
        return seq[0]
    diffs = [b - a for a, b in zip(seq, seq[1:])]
    return seq[-1] + predict_next(diffs)


input = read_input("input.txt", 2023, 9)

total = 0
for line in input:
    seq = [int(x) for x in line.split()]
    total += predict_next(seq)

print(total)
