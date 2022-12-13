from collections import deque

from src.common.read_input import read_input


def bfs(graph, start_row, start_col, end_row, end_col):
    num_rows = len(graph)
    num_cols = len(graph[0])
    unvisited = deque()
    unvisited.append((start_row, start_col))
    visited = [[False] * num_cols for _ in range(num_rows)]
    visited[start_row][start_col] = True
    shortest_dist = [[float('inf')] * num_cols for _ in range(num_rows)]
    shortest_dist[start_row][start_col] = 0

    while unvisited:
        r, c = unvisited.popleft()
        for next_r, next_c in graph[r][c]:
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                unvisited.append((next_r, next_c))
                shortest_dist[next_r][next_c] = shortest_dist[r][c] + 1
                if next_r == end_row and next_c == end_col:
                    return shortest_dist[end_row][end_col]

    return float('inf')


input = read_input('input.txt', 2022, 12)

num_rows = len(input)
num_cols = len(input[0])
num_nodes = num_rows * num_cols

grid = [[-1] * num_cols for _ in range(num_rows)]
# 4 because left, right, up, down
graph = [[[] for _ in range(num_cols)] for _ in range(num_rows)]
start_row, start_col, end_row, end_col = [-1] * 4

for r, line in enumerate(input):
    for c, char in enumerate(line):
        elevation_char = char
        if char == 'S':
            start_row = r
            start_col = c
            elevation_char = 'a'
        elif char == 'E':
            end_row = r
            end_col = c
            elevation_char = 'z'
        grid[r][c] = ord(elevation_char) - ord('a')

for r in range(num_rows):
    for c in range(num_cols):
        if c > 0:   # left
            if grid[r][c-1] - grid[r][c] <= 1:
                graph[r][c].append((r, c-1))
        if c < num_cols-1:  # right
            if grid[r][c+1] - grid[r][c] <= 1:
                graph[r][c].append((r, c+1))
        if r > 0:  # up
            if grid[r-1][c] - grid[r][c] <= 1:
                graph[r][c].append((r-1, c))
        if r < num_rows-1:  # down
            if grid[r+1][c] - grid[r][c] <= 1:
                graph[r][c].append((r+1, c))

print(bfs(graph, start_row, start_col, end_row, end_col))
