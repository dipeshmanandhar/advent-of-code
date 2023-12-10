from src.common.read_input import read_input

input = read_input('input.txt', 2023, 3)

board = [[c for c in line] for line in input]
NUM_ROWS = len(board)
NUM_COLS = len(board[0])

def is_symbol(char):
    return (not char.isdigit()) and char != '.'

def fill_num(board, visited, r, c):
    if not board[r][c].isdigit() or visited[r][c]:
        return -1
    min_c = 0
    max_c = NUM_COLS
    # look left for more numbers
    for curr_c in range(c, -1, -1):
        if board[r][curr_c].isdigit():
            visited[r][curr_c] = True
        else:
            min_c = curr_c + 1
            break
    # look right for more numbers
    for curr_c in range(c+1, NUM_COLS):
        if board[r][curr_c].isdigit():
            visited[r][curr_c] = True
        else:
            max_c = curr_c
            break
    return int(''.join(board[r][min_c:max_c]))

visited = [[False for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
total = 0
for r, row in enumerate(board):
    for c, char in enumerate(row):
        if is_symbol(char):
            for curr_r in range(r-1, r+2):
                if curr_r < 0 or curr_r >= NUM_ROWS:
                    continue
                for curr_c in range(c-1, c+2):
                    if curr_c < 0 or curr_c >= NUM_COLS:
                        continue
                    num = fill_num(board, visited, curr_r, curr_c)
                    if num > 0:
                        total += num

print(total)
