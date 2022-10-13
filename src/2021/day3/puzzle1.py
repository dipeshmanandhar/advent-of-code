from src.common.read_input import read_input


def bits_to_decimal(bits):
    binary_str = ''.join(map(lambda bit: str(int(bit)), bits))
    decimal = int(binary_str, 2)
    return decimal


input = read_input('input.txt', 2021, 3)

num_lines = len(input)
digits = map(lambda line: (int(digit) for digit in line), input)
num_ones_list = (sum(column) for column in zip(*digits))
gamma_bits = list(map(lambda num_ones: num_ones > num_lines/2, num_ones_list))
epsilon_bits = map(lambda gamma_bit: not gamma_bit, gamma_bits)
gamma_rate = bits_to_decimal(gamma_bits)
epsilon_rate = bits_to_decimal(epsilon_bits)

print(gamma_rate * epsilon_rate)
