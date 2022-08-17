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


edges = int(input())
graph = {}

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    edge = Edge(source, destination, weight)
    graph[source].append(edge)
    graph[destination].append(edge)

forest = set()
forest_edges = []

for node in graph:
    if node in forest:
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f'{edge.source} - {edge.destination}')

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