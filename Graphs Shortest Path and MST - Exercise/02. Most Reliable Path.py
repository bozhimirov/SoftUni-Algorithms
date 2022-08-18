from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    #
    # if first not in graph:
    #     graph[first] = []
    # if second not in graph:
    #     graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

start = int(input())
target = int(input())

# max_node = max(graph.keys())

pq = PriorityQueue()
pq.put((-100, start))

distance = [float("-inf")] * nodes
parent = [None] * nodes

distance[start] = 100

while not pq.empty():
    max_distance, node = pq.get()
    if node == target:
        break
    for edge in graph[node]:
        child = edge.second if edge.first == node else edge.first
        new_distance = -max_distance + edge.weight / 100
        if new_distance > distance[child]:
            distance[child] = new_distance
            parent[child] = node
            pq.put((-new_distance, child))

print(f'Most reliable path reliability: {distance[target]:.2f}%')

path = deque()
node = target
while node is not None:
    path.appendleft(node)
    node = parent[node]
print(*path, sep='->')

