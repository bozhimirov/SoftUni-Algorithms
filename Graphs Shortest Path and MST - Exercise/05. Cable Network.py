from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)
    pq = PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1

        if min_edge.source in forest and min_edge.destination not in forest:
            non_tree_node = min_edge.destination
        elif min_edge.destination in forest and min_edge.source not in forest:
            non_tree_node = min_edge.sourse

        if non_tree_node == -1:
            continue

        forest.add(non_tree_node)
        forest_edges.append(min_edge)

        for edge in graph[non_tree_node]:
            pq.put(edge)


budget = int(input())
nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]
# tree = set()
forest = set()

for _ in range(edges):
    edge_data = input().split()
    source, destination, weight = int(edge_data[0]), int(edge_data[1]), int(edge_data[2])
    # if source not in graph:
    #     graph[source] = []
    # if destination not in graph:
    #     graph[destination] = []
    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)

    if len(edge_data) == 4:
        forest.add(source)
        forest.add(destination)

# forest_edges = []
#
# for node in graph:
#     if node in forest:
#         continue
#     prim(node, graph, forest, forest_edges)
#
# for edge in forest_edges:
#     print(f'{edge.source} - {edge.destination}')

pq = PriorityQueue()
for node in forest:
    for edge in graph[node]:
        pq.put(edge)

budget_used = 0
while not pq.empty():
    min_edge = pq.get()
    non_tree_node = -1

    if min_edge.source in forest and min_edge.destination not in forest:
        non_tree_node = min_edge.destination
    elif min_edge.destination in forest and min_edge.source not in forest:
        non_tree_node = min_edge.source

    if non_tree_node == -1:
        continue
    if budget_used + min_edge.weight > budget:
        break
    budget_used += min_edge.weight
    forest.add(non_tree_node)
    # forest_edges.append(min_edge)

    for edge in graph[non_tree_node]:
        pq.put(edge)

print(f'Budget used: {budget_used}')

'''
11
0, 2, 5
2, 4, 7
4, 5, 12
0, 1, 4
1, 3, 2
0, 3, 9
2, 3, 20
3, 4, 8
6, 7, 8
6, 8, 10
7, 8, 7
'''