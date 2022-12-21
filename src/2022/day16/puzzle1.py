from collections import deque

from src.common.read_input import read_input


def bfs(graph, start_node, weighted_graph):
    NUM_NODES = len(graph)
    unvisited = deque()
    unvisited.append(start_node)
    visited = [False] * NUM_NODES
    visited[start_node] = True
    weighted_graph[start_node][start_node] = 0

    while unvisited:
        node = unvisited.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                unvisited.append(next_node)
                weighted_graph[start_node][next_node] = weighted_graph[start_node][node] + 1

    return weighted_graph


def create_weighted_graph(graph):
    NUM_NODES = len(graph)
    weighted_graph = [[0] * NUM_NODES for _ in range(NUM_NODES)]

    for start_node in range(NUM_NODES):
        weighted_graph = bfs(graph, start_node, weighted_graph)

    return weighted_graph


def find_best_gain(weighted_graph, flow_rates, curr_index, minutes_left, visited):
    NUM_VALVES = len(weighted_graph)
    if minutes_left <= 0:
        return 0

    max_next_gain = 0
    # max_next_i = -1
    for next_i in range(NUM_VALVES):
        if not visited[next_i]:
            next_minutes_left = minutes_left - \
                weighted_graph[curr_index][next_i] - 1
            next_visited = visited.copy()
            next_visited[next_i] = True
            next_gain = next_minutes_left * flow_rates[next_i] + find_best_gain(
                weighted_graph, flow_rates, next_i, next_minutes_left, next_visited)
            if next_gain > max_next_gain:
                max_next_gain = next_gain
                # max_next_i = next_i
    return max_next_gain


def find_pressure(graph, flow_rates, start_index, minutes_left=30):
    NUM_VALVES = len(graph)
    visited = [flow_rates[i] == 0 for i in range(NUM_VALVES)]
    weighted_graph = create_weighted_graph((graph))
    return find_best_gain(weighted_graph, flow_rates, start_index, minutes_left, visited)


input = read_input('input.txt', 2022, 16)

NUM_VALVES = len(input)
valve_to_index = {}
index_to_valve = ['??' for _ in range(NUM_VALVES)]
flow_rates = [0] * NUM_VALVES
graph = [[] for _ in range(NUM_VALVES)]

for i, line in enumerate(input):
    valve, flow_rate, next_valves = line.replace('Valve ', '').replace(' has flow rate=', '/')\
        .replace('s', '').replace('; tunnel lead to valve ', '/').split('/')
    valve_to_index[valve] = i
    index_to_valve[i] = valve
    flow_rates[i] = int(flow_rate)

for i, line in enumerate(input):
    valve, flow_rate, next_valves = line.replace('Valve ', '').replace(' has flow rate=', '/')\
        .replace('s', '').replace('; tunnel lead to valve ', '/').split('/')
    for next_valve in next_valves.split(', '):
        next_i = valve_to_index[next_valve]
        graph[i].append(next_i)

print(find_pressure(graph, flow_rates, valve_to_index['AA']))
