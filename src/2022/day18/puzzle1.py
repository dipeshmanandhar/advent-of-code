from src.common.read_input import read_input

input = read_input('input.txt', 2022, 18)

max_x, max_y, max_z = [0] * 3

for line in input:
    x, y, z = [int(num) for num in line.split(',')]
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if z > max_z:
        max_z = z

X_LEN = max_x + 1
Y_LEN = max_y + 1
Z_LEN = max_z + 1

grid = [[[False] * Z_LEN for _ in range(Y_LEN)] for _ in range(X_LEN)]
faces_open = [[[0] * Z_LEN for _ in range(Y_LEN)] for _ in range(X_LEN)]

for line in input:
    x, y, z = [int(num) for num in line.split(',')]
    grid[x][y][z] = True
    faces_open[x][y][z] = 6
    if x-1 >= 0 and grid[x-1][y][z]:
        faces_open[x][y][z] -= 1
        faces_open[x-1][y][z] -= 1
    if x+1 < X_LEN and  grid[x+1][y][z]:
        faces_open[x][y][z] -= 1
        faces_open[x+1][y][z] -= 1
    if y-1 >= 0 and grid[x][y-1][z]:
        faces_open[x][y][z] -= 1
        faces_open[x][y-1][z] -= 1
    if y+1 < Y_LEN and grid[x][y+1][z]:
        faces_open[x][y][z] -= 1
        faces_open[x][y+1][z] -= 1
    if z-1 >= 0 and grid[x][y][z-1]:
        faces_open[x][y][z] -= 1
        faces_open[x][y][z-1] -= 1
    if z+1 < Z_LEN and grid[x][y][z+1]:
        faces_open[x][y][z] -= 1
        faces_open[x][y][z+1] -= 1

print(sum([sum([sum(z) for z in yz]) for yz in faces_open]))
