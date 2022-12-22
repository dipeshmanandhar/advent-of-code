from collections import deque

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

X_LEN = max_x + 3
Y_LEN = max_y + 3
Z_LEN = max_z + 3

grid = [[[False] * Z_LEN for _ in range(Y_LEN)] for _ in range(X_LEN)]

for line in input:
    x, y, z = [int(num) for num in line.split(',')]
    grid[x+1][y+1][z+1] = True

visited = [[[False] * Z_LEN for _ in range(Y_LEN)] for _ in range(X_LEN)]
visited[-1][-1][-1] = True
unvisited = deque()
unvisited.append((X_LEN-1, Y_LEN-1, Z_LEN-1))
surface_area = 0
while unvisited:
    x, y, z = unvisited.popleft()
    if x-1 >= 0:
        if grid[x-1][y][z]:
            surface_area += 1
        elif not visited[x-1][y][z]:
            visited[x-1][y][z] = True
            unvisited.append((x-1, y, z))
    if x+1 < X_LEN:
        if grid[x+1][y][z]:
            surface_area += 1
        elif not visited[x+1][y][z]:
            visited[x+1][y][z] = True
            unvisited.append((x+1, y, z))
    if y-1 >= 0:
        if grid[x][y-1][z]:
            surface_area += 1
        elif not visited[x][y-1][z]:
            visited[x][y-1][z] = True
            unvisited.append((x, y-1, z))
    if y+1 < Y_LEN:
        if grid[x][y+1][z]:
            surface_area += 1
        elif not visited[x][y+1][z]:
            visited[x][y+1][z] = True
            unvisited.append((x, y+1, z))
    if z-1 >= 0:
        if grid[x][y][z-1]:
            surface_area += 1
        elif not visited[x][y][z-1]:
            visited[x][y][z-1] = True
            unvisited.append((x, y, z-1))
    if z+1 < Z_LEN:
        if grid[x][y][z+1]:
            surface_area += 1
        elif not visited[x][y][z+1]:
            visited[x][y][z+1] = True
            unvisited.append((x, y, z+1))

print(surface_area)
