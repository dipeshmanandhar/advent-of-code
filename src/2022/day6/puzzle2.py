from src.common.read_input import read_input

def is_unique(word):
    existing_chars = [0] * 26
    for char in word:
        index = ord(char) - ord('a')
        if existing_chars[index]:
            return False
        else:
            existing_chars[index] += 1
    return True

input = read_input('input.txt', 2022, 6)

input = input[0]
first_index = -1
for i in range(14, len(input)+1):
    if is_unique(input[i-14:i]):
        first_index = i
        break
print(first_index)
