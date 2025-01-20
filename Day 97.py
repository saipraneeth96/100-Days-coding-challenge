"""
Day 97 coding Statement : 

Arun has a rooted tree of N vertices rooted at vertex 1. Each vertex can either be coloured black or white.

Initially, the vertices are coloured A1?,A2?,…AN?, where Ai? ∈ {0,1} denotes the colour of the i-th vertex (here 0 represents white and 1 represents black). He wants to perform some operations to change the colouring of the vertices to B1?,B2?,…BN? respectively.

Arun can perform the following operation any number of times. In one operation, he can choose any subtree and either paint all its vertices white or all its vertices black.

Help Arun find the minimum number of operations required to change the colouring of the vertices to B1?,B2?,…BN? respectively.

Input Format

The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N — the size of the tree.
The second line of each test case contains N space-separated integers A1?,A2?,…,AN? denoting the initial colouring of the vertices of the tree.
The third line of each test case contains N space-separated integers B1?,B2?,…,BN? denoting the final desired colouring of the vertices of the tree.
The next N−1 lines contain two space-separated integers u and v — denoting an undirected edge between nodes u and v.
It is guaranteed that the edges given in the input form a tree.

Output Format

For each testcase, output the minimum number of operations required to obtain the desired colouring.

 

Sample Input

2

4

1 1 0 0

1 1 1 0

1 2

1 3

1 4

5

1 1 1 0 0

1 0 1 1 1

5 3

3 1

2 1

4 3

 

Sample Output

1

2

 

"""

from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def dfs(node, parent, adj, A, B, visited):
    # Base case: initialize operation count for this subtree
    operations = 0
    
    # Check if the current node's color matches the desired color
    if A[node] != B[node]:
        operations += 1  # Change the subtree's color
        A[node] = B[node]  # Simulate painting the subtree
    
    # Mark this node as visited
    visited[node] = True
    
    # Traverse all child nodes
    for neighbor in adj[node]:
        if neighbor != parent and not visited[neighbor]:
            operations += dfs(neighbor, node, adj, A, B, visited)
    
    return operations

def solve():
    T = int(input())  # Number of test cases
    results = []
    
    for _ in range(T):
        N = int(input())  # Number of vertices
        
        # Initial coloring
        A = list(map(int, input().split()))
        
        # Desired coloring
        B = list(map(int, input().split()))
        
        # Build the adjacency list for the tree
        adj = defaultdict(list)
        for __ in range(N - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        
        # Create a visited array to track visited nodes
        visited = [False] * (N + 1)
        
        # Run DFS starting from the root node (node 1)
        result = dfs(1, -1, adj, [0] + A, [0] + B, visited)
        results.append(result)
    
    # Output results for all test cases
    for res in results:
        print(res)

