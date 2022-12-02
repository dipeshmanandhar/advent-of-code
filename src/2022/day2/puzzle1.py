from src.common.read_input import read_input


def decrypt_shapes(shapes):
    return (ord(shapes[0]) - ord('A'), ord(shapes[1]) - ord('X'))


def score(opponent, you):
    opponent_score = opponent + 1
    your_score = you + 1
    if you == (opponent+1) % 3:   # you win
        your_score += 6
    elif you == opponent:   # draw
        your_score += 3
        opponent_score += 3
    else:   # you lose
        opponent_score += 3

    return (opponent_score, your_score)


input = read_input('input.txt', 2022, 2)

scores = [score(*decrypt_shapes(line.split())) for line in input]
total_scores = [sum(player_scores) for player_scores in [*zip(*scores)]]

print(total_scores)
