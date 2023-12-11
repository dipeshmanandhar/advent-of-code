from src.common.read_input import read_input

input = read_input("input.txt", 2023, 4)

num_cards = [1 for _ in range(len(input) + 1)]
num_cards[0] = 0
for line in input:
    card_info, card = line.split(":")
    card_num = int(card_info.split()[1])
    winning_nums, my_nums = card.split("|")
    winning_nums = sorted([int(num) for num in winning_nums.split()])
    my_nums = sorted([int(num) for num in my_nums.split()])
    i = 0
    num_matches = 0
    for winning_num in winning_nums:
        while True:
            if i >= len(my_nums):
                break
            my_num = my_nums[i]
            if winning_num == my_num:
                num_matches += 1
                break
            elif my_num < winning_num and i < len(my_nums):
                i += 1
            else:
                break
    for i in range(card_num + 1, card_num + 1 + num_matches):
        num_cards[i] += num_cards[card_num]

print(sum(num_cards))
