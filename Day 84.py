Day 84 coding Statement : 

Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

def is_valid_color(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring_util(node, graph, colors, m, n):
    if node == n:  # All vertices are colored
        return True
    
    for c in range(1, m + 1):  # Try each color from 1 to m
        if is_valid_color(node, c, graph, colors):
            colors[node] = c
            if graph_coloring_util(node + 1, graph, colors, m, n):
                return True
            colors[node] = 0  # Backtrack
    
    return False

def graph_coloring(n, m, edges):
    # Build the graph as an adjacency list
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize colors for all vertices
    colors = [0] * n
    
    # Start the coloring process
    if graph_coloring_util(0, graph, colors, m, n):
        return 1
    else:
        return 0

# Example Usage
N1, M1, E1, Edges1 = 4, 3, 5, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
print(graph_coloring(N1, M1, Edges1))  # Output: 1

N2, M2, E2, Edges2 = 3, 2, 3, [(0, 1), (1, 2), (0, 2)]
print(graph_coloring(N2, M2, Edges2))  # Output: 0
