from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end="")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end="")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


print("DFS Traversal:")
visited = set()
dfs(graph, 'A', set())
print("\n")
print("BFS Traversal:")
bfs(graph, 'A')
