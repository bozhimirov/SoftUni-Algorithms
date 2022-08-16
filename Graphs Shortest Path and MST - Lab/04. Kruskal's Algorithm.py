from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


edges = int(input())
graph = []

max_node = float('-inf')
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(source, destination, weight))
    max_node = max(source, destination, weight)

parent = [num for num in range(max_node + 1)]
forest = []


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


for edge in sorted(graph, key=lambda e: e.weight):
    first_node_root = find_root(parent, edge.source)
    sec_node_root = find_root(parent, edge.destination)
    if first_node_root != sec_node_root:
        parent[first_node_root] = sec_node_root
        forest.append(edge)

for edge in forest:
    print(f'{edge.source} - {edge.destination}')

'''
11
0, 3, 9
0, 5, 4
0, 8, 5
1, 4, 8
1, 7, 7
2, 6, 12
3, 5, 2
3, 6, 8
3, 8, 20
4, 7, 10
6, 8, 7
'''