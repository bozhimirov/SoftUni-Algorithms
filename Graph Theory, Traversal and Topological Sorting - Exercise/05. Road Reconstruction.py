def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count)]

edges = set()

for _ in range(edges_count):
    first, sec = [int(x) for x in input().split(' - ')]
    graph[first].append(sec)
    graph[sec].append(first)
    edges.add((min(first, sec), max(first, sec)))

print("Important streets:")
important_streets = []
for first, sec in edges:
    graph[first].remove(sec)
    graph[sec].remove(first)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        print(first, sec)

    graph[first].append(sec)
    graph[sec].append(first)

'''
5
5
1 - 0
0 - 2
2 - 1
0 - 3
3 - 4
'''