import functools

from src.common.read_input import read_input

LABELS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def str_to_hand(hand_str: str):
    hand = {label: 0 for label in LABELS}
    for label in hand_str:
        hand[label] += 1
    return hand


# returns -1 if hand_1 wins, returns 1 if hand_2 wins
def compare_hands(hand_1: list[str], hand_2: list[str]):
    hand_1_cards, bid_1 = hand_1
    hand_2_cards, bid_2 = hand_2
    hand_1_dict = str_to_hand(hand_1_cards)
    hand_2_dict = str_to_hand(hand_2_cards)
    hand_1_dict_no_j = {
        label: num_cards for label, num_cards in hand_1_dict.items() if label != "J"
    }
    hand_2_dict_no_j = {
        label: num_cards for label, num_cards in hand_2_dict.items() if label != "J"
    }
    max_repeats_1 = max(hand_1_dict_no_j.values()) + hand_1_dict["J"]
    max_repeats_2 = max(hand_2_dict_no_j.values()) + hand_2_dict["J"]
    if max_repeats_1 > max_repeats_2:
        return -1
    elif max_repeats_1 < max_repeats_2:
        return 1
    elif max_repeats_1 == 3:
        num_plain_pairs_1 = list(hand_1_dict_no_j.values()).count(2)
        num_plain_pairs_2 = list(hand_2_dict_no_j.values()).count(2)
        if hand_1_dict["J"] == 1:
            num_plain_pairs_1 -= 1
        if hand_2_dict["J"] == 1:
            num_plain_pairs_2 -= 1
        is_full_house_1 = num_plain_pairs_1 == 1
        is_full_house_2 = num_plain_pairs_2 == 1
        if is_full_house_1 and not is_full_house_2:
            return -1
        elif not is_full_house_1 and is_full_house_2:
            return 1
    elif max_repeats_1 == 2:
        num_pairs_1 = list(hand_1_dict_no_j.values()).count(2) + hand_1_dict["J"]
        num_pairs_2 = list(hand_2_dict_no_j.values()).count(2) + hand_2_dict["J"]
        if num_pairs_1 > num_pairs_2:
            return -1
        elif num_pairs_1 < num_pairs_2:
            return 1
    # now we know the 2 hands are the same type
    for i, label_1 in enumerate(hand_1_cards):
        label_2 = hand_2_cards[i]
        pos_1 = LABELS.index(label_1)
        pos_2 = LABELS.index(label_2)
        if pos_1 < pos_2:
            return -1
        elif pos_1 > pos_2:
            return 1
    return 0


input = read_input("input.txt", 2023, 7)

hands = [line.split() for line in input]
hands.sort(key=functools.cmp_to_key(compare_hands), reverse=True)
total = 0
for i, hand in enumerate(hands):
    rank = i + 1
    bid = int(hand[1])
    total += rank * bid

print(total)
