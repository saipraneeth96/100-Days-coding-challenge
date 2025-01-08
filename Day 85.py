"""
Day 85 coding Statement : 

You are given an undirected graph with N nodes (numbered 1 through N) and M edges. 
Each edge connects two distinct nodes. However, there may be multiple edges connecting the same pairs of nodes, 
and they are considered to be distinct edges. A lowercase English letter is written in each node.

You are also given a string S with length L.
A beautiful path is a sequence of L−1 edges such that there is a sequence of L nodes with the following properties:

for each valid i, the i-th edge connects the i-th and (i+1)-th of these nodes
for each valid i, the i-th character of S is written in the i-th of these nodes
There are no other restrictions — a path may visit nodes or edges any number of times in any order.

Determine the number of beautiful paths in the graph. Since the answer can be very large, compute it modulo (10^9)+7.

Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains three space-separated integers N, M and L.
The second line contains a single string S with length L.
The third line contains a single string with length N. For each valid i,
the i-th character of the string is the letter written in the i-th node.
Two lines follow. The first line contains M integers u1?,…,um?. The second lines contains M integers, v1?,…,vm?.
This denotes that there is an edge connecting nodes ui? and to vi?. These edges are distinct, even though they may connect the same pair of nodes.
Output

For each test case, print a single line containing one integer — the number of beautiful paths modulo (10^9)+7.

Sample Input

2

4 4 3

aac

aaca

1 2 2 1

2 3 4 2

2 1 2

aa

aa

1

2

Sample Output

3

1

"""

MOD = 10**9 + 7

def count_beautiful_paths(T, test_cases):
    results = []
    
    for case in test_cases:
        N, M, L = case['N'], case['M'], case['L']
        S = case['S']
        node_letters = case['node_letters']
        edges = case['edges']
        
        # Build the graph
        graph = {i: [] for i in range(1, N+1)}
        for u, v in zip(edges[0], edges[1]):
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize DP table
        dp = [[0] * (N + 1) for _ in range(L)]
        
        # Base case
        for node in range(1, N+1):
            if node_letters[node-1] == S[0]:
                dp[0][node] = 1
        
        # DP transitions
        for i in range(1, L):
            for node in range(1, N+1):
                if node_letters[node-1] == S[i]:
                    for neighbor in graph[node]:
                        dp[i][node] += dp[i-1][neighbor]
                        dp[i][node] %= MOD
        
        # Count total beautiful paths
        total_paths = sum(dp[L-1][node] for node in range(1, N+1)) % MOD
        results.append(total_paths)
    
    return results

# Input parsing
def parse_input():
    T = int(input())
    test_cases = []
    
    for _ in range(T):
        N, M, L = map(int, input().split())
        S = input().strip()
        node_letters = input().strip()
        u = list(map(int, input().split()))
        v = list(map(int, input().split()))
        test_cases.append({
            'N': N,
            'M': M,
            'L': L,
            'S': S,
            'node_letters': node_letters,
            'edges': (u, v)
        })
    
    return T, test_cases

# Main function
if __name__ == "__main__":
    T, test_cases = parse_input()
    results = count_beautiful_paths(T, test_cases)
    for res in results:
        print(res)
