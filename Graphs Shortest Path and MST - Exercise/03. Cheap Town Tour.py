# from collections import deque


nodes = int(input())
edges = int(input())
graph = []

# max_node = float('-inf')
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(' - ')]
    graph.append((source, destination, weight))
    max_node = max(source, destination, weight)

parent = [num for num in range(nodes)]
# forest = []
total_cost = 0


def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


for source, destination, weight in sorted(graph, key=lambda x: x[2]):
    first_node_root = find_root(parent, source)
    sec_node_root = find_root(parent, destination)

    if first_node_root != sec_node_root:
        parent[first_node_root] = sec_node_root
        # forest.append(edge)
        total_cost += weight

print(f'Total cost: {total_cost}')

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