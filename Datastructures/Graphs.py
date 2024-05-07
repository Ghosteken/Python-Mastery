# Creating a graph using an adjacency list representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Traversing the graph using Depth-First Search (DFS)
visited = set()

def dfs(node):
    if node not in visited:
        visited.add(node)
        print(node, end=' ')
        for neighbor in graph[node]:
            dfs(neighbor)

print("DFS Traversal:")
dfs('A')  # Output: A B D E F C

# Traversing the graph using Breadth-First Search (BFS)
from collections import deque

def bfs(start_node):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

print("\nBFS Traversal:")
bfs('A')  # Output: A B C D E F
