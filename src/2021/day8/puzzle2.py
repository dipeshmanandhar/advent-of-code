from src.common.read_input import read_input


def difference_string(a, b):
    return a.translate(str.maketrans('', '', b))


def complement_string(wires):
    return difference_string(all_wires, wires)


def intersection_string(a, b):
    return difference_string(a, complement_string(b))


all_wires = 'abcdefg'
digit_display_wires = ['abcefg', 'cf', 'acdeg', 'acdfg',
                       'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
digit_display_wire_lengths = [len(wire) for wire in digit_display_wires]
length_to_digit = [[i for i, x in enumerate(digit_display_wire_lengths) if x == wire_length]
                   for wire_length in range(len(digit_display_wire_lengths))]
length_to_required_wires = []
for digits in length_to_digit:
    required_wires = all_wires if len(digits) > 0 else ''
    for digit in digits:
        required_wires = intersection_string(
            required_wires, digit_display_wires[digit])
    length_to_required_wires.append(required_wires)
unique_digits = [1, 4, 7, 8]
unique_digits_lengths = [len(digit_display_wires[unique_digit])
                         for unique_digit in unique_digits]


def char_to_index(c):
    return ord(c) - ord('a')


def index_to_char(i):
    return chr(ord('a')+i)


def wires_to_indexes(wires):
    return [char_to_index(wire) for wire in wires]


def calc_wire_mappings(input_digits):
    wire_mappings = [all_wires] * 7
    # first pass, only looking at the unique digits (1, 4, 7, 8)
    for input_digit_wires in input_digits:
        unique_digits_index = -1
        try:
            unique_digits_index = unique_digits_lengths.index(
                len(input_digit_wires))
        except ValueError:
            pass

        if unique_digits_index >= 0:
            input_digit = unique_digits[unique_digits_index]
            input_digit_wire_indexes = wires_to_indexes(input_digit_wires)
            for wire_index, wire_mapping in enumerate(wire_mappings):
                if wire_index in input_digit_wire_indexes:
                    # the current wire is on, so the wire must be enabled by the current digit
                    wire_mappings[wire_index] = intersection_string(
                        wire_mapping, digit_display_wires[input_digit])
                else:
                    # the current wire is off, so the wire must be disabled by the current digit
                    wire_mappings[wire_index] = difference_string(
                        wire_mapping, digit_display_wires[input_digit])
    # second pass, looking at remaining digits
    for input_digit_wires in input_digits:
        possible_digits = length_to_digit[len(input_digit_wires)]
        if len(possible_digits) > 1:
            required_wires = length_to_required_wires[len(input_digit_wires)]
            input_digit_wire_indexes = wires_to_indexes(
                sorted(input_digit_wires))
            wire_mappings_at_input_indexes = [
                (i, wire_mappings[i]) for i in input_digit_wire_indexes]
            for required_wire in required_wires:
                required_wire_input_indexes = [
                    wire[0] for wire in wire_mappings_at_input_indexes if required_wire in wire[1]]
                if len(required_wire_input_indexes) == 1:
                    wire_mappings[required_wire_input_indexes[0]
                                  ] = required_wire
    # finally, we need to clean up the remaining mappings
    for i, wire_mapping in enumerate(wire_mappings):
        if len(wire_mapping) == 1:
            for j, other_wire_mapping in enumerate(wire_mappings):
                if i != j:
                    wire_mappings[j] = other_wire_mapping.replace(
                        wire_mapping, '')
    return wire_mappings


def decode_digits(output_digits, wire_mappings):
    return [digit_display_wires.index(''.join(sorted([wire_mappings[char_to_index(wire)] for wire in digit]))) for digit in output_digits]


def decode_display(input_digits, output_digits):
    wire_mappings = calc_wire_mappings(input_digits)
    decoded_digits = decode_digits(output_digits, wire_mappings)
    return int(''.join(map(str, decoded_digits)))


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
decoded_sum = sum([decode_display(input_displays[i], output_displays[i])
                  for i in range(len(input_displays))])

print(decoded_sum)
