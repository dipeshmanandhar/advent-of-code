from src.common.read_input import read_input

input = read_input('input.txt', 2022, 9)

max_left, max_right, max_up, max_down = [0]*4
curr_x, curr_y = [0]*2
for line in input:
    dir, dist = line.split()
    dist = int(dist)
    if dir == 'L':
        curr_x -= dist
        if curr_x < max_left:
            max_left = curr_x
    elif dir == 'R':
        curr_x += dist
        if curr_x > max_right:
            max_right = curr_x
    elif dir == 'U':
        curr_y += dist
        if curr_y > max_up:
            max_up = curr_y
    elif dir == 'D':
        curr_y -= dist
        if curr_y < max_down:
            max_down = curr_y

x_range = max_right - max_left + 1
y_range = max_up - max_down + 1

t_visited = [[False]*x_range for _ in range(y_range)]


def x_to_c(x):
    return x - max_left


def y_to_r(y):
    return y - max_down


def t_visit(x, y):
    t_visited[y_to_r(y)][x_to_c(x)] = True


def move_t(t_x, t_y, h_x, h_y):
    if abs(t_x-h_x) <= 1 and abs(t_y-h_y) <= 1:
        return (t_x, t_y)
    d_t_x = 0
    d_t_y = 0
    if t_x > h_x:
        d_t_x = -1
    elif t_x < h_x:
        d_t_x = 1
    if t_y > h_y:
        d_t_y = -1
    elif t_y < h_y:
        d_t_y = 1

    return (t_x + d_t_x, t_y + d_t_y)


t_visit(0, 0)
t_x, t_y, h_x, h_y = [0]*4

for line in input:
    dir, dist = line.split()
    dist = int(dist)
    for i in range(dist):
        if dir == 'L':
            h_x -= 1
        elif dir == 'R':
            h_x += 1
        elif dir == 'U':
            h_y += 1
        elif dir == 'D':
            h_y -= 1
        t_x, t_y = move_t(t_x, t_y, h_x, h_y)
        t_visit(t_x, t_y)
total_t_positions = sum([sum(row) for row in t_visited])

print(total_t_positions)
