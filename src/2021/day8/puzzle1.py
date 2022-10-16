from src.common.read_input import read_input

digit_displays = ['abcefg', 'cf', 'acdeg', 'acdfg',
                  'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
unique_digits = [1, 4, 7, 8]
unique_digits_lengths = [len(digit_displays[unique_digit])
                         for unique_digit in unique_digits]

input = read_input('input.txt', 2021, 8)

all_displays_raw = [line.split(' | ') for line in input]
input_displays_raw, output_displays_raw = list(zip(*all_displays_raw))
input_displays = [input_display_raw.split()
                  for input_display_raw in input_displays_raw]
output_displays = [output_display_raw.split()
                   for output_display_raw in output_displays_raw]
flat_output_digits = [output_digit for output_display in output_displays
                      for output_digit in output_display]
num_unique_output_digits = len([1 for output_digit in flat_output_digits
                                if len(output_digit) in unique_digits_lengths])

print(num_unique_output_digits)
