from src.common.read_input import read_input


def is_correct_order(left, right):
    left_type = type(left)
    right_type = type(right)
    if left_type is int and right_type is int:
        return None if left == right else left < right
    elif left_type is list and right_type is list:
        left_len = len(left)
        right_len = len(right)
        for i in range(min(left_len, right_len)):
            curr_comparison = is_correct_order(left[i], right[i])
            if curr_comparison != None:
                return curr_comparison
        return None if left_len == right_len else left_len < right_len
    else:
        if left_type is int:
            left = [left]
        else:
            right = [right]
        return is_correct_order(left, right)


input = read_input('input.txt', 2022, 13)

num_pairs = (len(input)+1) // 3
sum_correct_pair_indexes = 0

for pair_index in range(num_pairs):
    left = eval(input[pair_index*3])
    right = eval(input[pair_index*3+1])
    if is_correct_order(left, right):
        sum_correct_pair_indexes += pair_index + 1

print(sum_correct_pair_indexes)
