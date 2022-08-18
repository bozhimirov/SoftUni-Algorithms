from collections import deque

def find_shortest_path(graph, source, destination):
    queue = deque([source])
    visited = {source}
    parent = {source: None}

    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            parent[child] = node

    return parent


def find_path_size(parent, destination):
    node = destination
    size = 0
    while node is not None:
        node = parent[node]
        size += 1
    return size - 1


nodes = int(input())
pairs = int(input())  # edges

graph = {}
# [graph.append([]) for _ in range(nodes + 1)]

for _ in range(nodes):
    node_str, children_str = input().split(':')
    node = int(node_str)
    children = [int(x) for x in children_str.split()] if children_str else []
    graph[node] = children

for _ in range(pairs):
    source, destination = [int(x) for x in input().split('-')]

    parent = find_shortest_path(graph, source, destination)

    if destination not in parent:
        print(f'{{{source}, {destination}}} -> -1')
        continue

    size = find_path_size(parent, destination)
    print(f'{{{source}, {destination}}} -> {size}')

'''
8 
4
1:4
2:4
3:4 5
4:6
5:3 7 8
6:
7:8
8:
1-6
1-5
5-6
5-8
'''
