from src.common.read_input import read_input


def position_on_board(board, number):
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == number:
                return (r, c)
    return (-1, -1)


def mark_board(board_marks, r, c):
    board_marks[r][c] = True


def is_winner(board_marks, r, c):
    horizontal_win = all(board_marks[r])
    vertical_win = all(list(zip(*board_marks))[c])
    return horizontal_win or vertical_win


def calculate_score(board, board_marks, number):
    score = 0
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if not board_marks[r][c]:
                score += cell
    score *= number
    return score


# returns the score of the board if it just won, otherwise returns -1\
def draw_number(board, board_marks, number):
    r, c = position_on_board(board, number)
    if r < 0:
        return -1
    mark_board(board_marks, r, c)
    if is_winner(board_marks, r, c):
        return calculate_score(board, board_marks, number)
    else:
        return -1


input = read_input('input.txt', 2021, 4)

numbers = map(int, input[0].split(sep=','))
boards_start_index = 2
board_size = 5
num_boards = (len(input)-1) // 6
boards = []
boards_marks = [[[False] * 5 for _ in range(5)] for _ in range(num_boards)]
for i in range(num_boards):
    board_i_start_index = boards_start_index + (board_size+1)*i
    board_i_str = input[board_i_start_index:board_i_start_index+board_size]
    board_i = [[int(number) for number in line.split()]
               for line in board_i_str]
    boards.append(board_i)
score = -1
for number in numbers:
    for i in range(num_boards):
        score = draw_number(boards[i], boards_marks[i], number)
        if score >= 0:
            break
    if score >= 0:
        break

print(score)
