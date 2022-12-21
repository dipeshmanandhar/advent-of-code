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


def find_best_gain(weighted_graph, flow_rates, curr_index, elephant_index, minutes_left, elephant_minutes_left, visited, node_to_i):
    NUM_NODES = len(node_to_i)
    if minutes_left <= 0 and elephant_minutes_left <= 0:
        return 0, [], []

    max_next_gain = 0
    max_you_path = []
    max_elephant_path = []
    next_visited = visited.copy()
    you_nothing_checked = False
    elephant_nothing_next_node = -1
    for next_node in range(NUM_NODES):
        next_i = node_to_i[next_node]
        if not visited[next_node]:
            next_minutes_left = minutes_left - \
                weighted_graph[curr_index][next_i] - 1
            if next_minutes_left < 0:
                next_minutes_left = 0
                if you_nothing_checked:
                    continue
                else:
                    you_nothing_checked = True
            next_visited[next_node] = True
            you_next_gain = next_minutes_left * flow_rates[next_i]
            for next_elephant_node in range(NUM_NODES):
                next_elephant_i = node_to_i[next_elephant_node]
                if not next_visited[next_elephant_node]:
                    elephant_next_minutes_left = elephant_minutes_left - \
                        weighted_graph[elephant_index][next_elephant_i] - 1
                    if elephant_next_minutes_left < 0:
                        elephant_next_minutes_left = 0
                        if elephant_nothing_next_node < 0:
                            elephant_nothing_next_node = next_node
                        elif elephant_nothing_next_node != next_node:
                            continue
                    next_visited[next_elephant_node] = True
                    elephant_next_gain = elephant_next_minutes_left * \
                        flow_rates[next_elephant_i]

                    next_gain, you_path, elephant_path = find_best_gain(
                        weighted_graph, flow_rates, next_i, next_elephant_i, next_minutes_left, elephant_next_minutes_left, next_visited, node_to_i)
                    next_gain += you_next_gain + elephant_next_gain
                    if next_gain > max_next_gain:
                        max_next_gain = next_gain
                        max_you_path = [next_i, *you_path]
                        max_elephant_path = [next_elephant_i, *elephant_path]
                    next_visited[next_elephant_node] = False
            next_visited[next_node] = False
    return max_next_gain, max_you_path, max_elephant_path


def find_pressure(graph, flow_rates, start_index, minutes_left=26):
    node_to_i = [i for i, flow_rate in enumerate(flow_rates)
                 if flow_rate or i == start_index]
    NUM_NODES = len(node_to_i)
    visited = [flow_rates[node_to_i[node]] == 0 for node in range(NUM_NODES)]
    weighted_graph = create_weighted_graph((graph))
    return find_best_gain(weighted_graph, flow_rates, start_index, start_index, minutes_left, minutes_left, visited, node_to_i)


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

max_gain, max_you_path, max_elephant_path = find_pressure(
    graph, flow_rates, valve_to_index['AA'])
print(max_gain)
print([index_to_valve[i] for i in max_you_path])
print([index_to_valve[i] for i in max_elephant_path])
