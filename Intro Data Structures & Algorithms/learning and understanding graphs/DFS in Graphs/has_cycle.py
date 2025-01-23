def has_cycle(graph):
    visited = set()
    # implement this
    for i in graph:
        if i not in visited:
            dfs(i, visited, graph, parent=None)
    return False

def dfs(vertex, visited, graph, parent):
    visited.add(vertex)

    for neighbor in graph[vertex]:
        # implement this
        if neighbor not in visited:
            if dfs(neighbor, visited, graph, vertex):
                return True
        elif neighbor != parent:
            return True

    return False

# Test the function
graph = {
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['C'],
    'E': ['G', 'K'],
    'K': ['G', 'E'],
    'G': ['K', 'E']
}
print(has_cycle(graph))