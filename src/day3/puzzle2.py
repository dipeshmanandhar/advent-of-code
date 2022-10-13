from src.common.read_input import read_input


# bit_position is index from the left side of the number
def most_common_value(digits, bit_position):
    num_lines = len(digits)
    num_ones = sum(list(zip(*digits))[bit_position])
    return num_ones >= num_lines/2


def least_common_value(digits, bit_position):
    return not most_common_value(digits, bit_position)


def bits_to_decimal(bits):
    binary_str = ''.join(map(lambda bit: str(int(bit)), bits))
    decimal = int(binary_str, 2)
    return decimal


def calculate_rating(digits, bit_criteria):
    for bit_position in range(num_digits):
        digits = [number for number in digits
                  if number[bit_position] == int(bit_criteria(digits, bit_position))]
        if len(digits) == 1:
            break
    rating = bits_to_decimal(digits[0])
    return rating


input = read_input('day3/input2.txt')

num_digits = len(input[0])
digits = [tuple(int(digit) for digit in line) for line in input]
oxygen_generator_rating = calculate_rating(digits, most_common_value)
co2_scrubber_rating = calculate_rating(digits, least_common_value)

print(oxygen_generator_rating * co2_scrubber_rating)
