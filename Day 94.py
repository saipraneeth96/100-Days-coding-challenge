"""
Day 94 coding Statement : 

Kekocity's population consist of N gnomes numbered with unique ids from 1 to N. As they are very joyful gnomes, 
they usually send jokes to their friends right after they get any (even if they knew it before) via their social network
named as Mybeard. Mybeard became popular in the city because of message auto-deletion.
It takes exactly one minute to read and resend joke to mates.
\Mayor of Kekocity, Mr. Shaikhinidin, is interested in understanding how the jokes are spread. He gives you database of Mybeard 
social network, and wants you to answer some queries on it.
You will be given a list of friends for every gnome and M queries of the following type: Who will receive a message 
with joke after exactly K minutes, if the creator of joke was gnome with id x?

Input

The first line contains a single integer N denoting the number of gnomes.

The next N lines contain the the matrix g[N][N]. Each of the i-th line,
will contain N space separated integers - j-th of those will denote g[i][j]. If gnome j is friend of gnome i, 
then g[i][j] is 1. Otherwise it will be zero. Plese note that the friendship relationship is not bidirectional,
i.e. it might happen that g[i][j] may not be equal to g[j][i]. Also one can be friend of itself also, 
i.e. g[i][i] may be equal to 1.
The next line contains a single integer M denoting the number of queries.
The next M lines contain two integers k and x described above.

Output

For each query, output two lines.
In the first line, output how many gnomes will know the joke after k minutes.
In the second line, print these ids (numbering) of these gnomes in increasing order. 
If no one will know the joke after K minutes, then print -1 in this line.

Constraints

1 ≤ N ≤ 500
1 ≤ M ≤ 500
0 ≤ k ≤ 109
1 ≤ x ≤ N
0 ≤ g[i][j] ≤ 1
 

Sample Input

5

0 1 0 0 0

0 0 1 1 0

1 0 0 0 0

0 0 0 1 0

0 0 0 0 0

4

3 1

10000 1

0 5

1 5

Sample Output

2

1 4

2

2 4

1

5

0

-1

"""

import numpy as np

def matrix_exponentiation(mat, k, n):
    """Exponentiate the matrix `mat` to the power `k`."""
    result = np.eye(n, dtype=int)  # Identity matrix
    base = np.array(mat)
    
    while k > 0:
        if k % 2 == 1:
            result = (result @ base) > 0  # Binary multiplication, boolean result
        base = (base @ base) > 0
        k //= 2
    
    return result.astype(int)

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    
    # Read adjacency matrix
    g = []
    for _ in range(N):
        g.append(list(map(int, data[idx:idx + N])))
        idx += N
    
    M = int(data[idx])
    idx += 1
    
    queries = []
    for _ in range(M):
        k, x = map(int, data[idx:idx + 2])
        queries.append((k, x))
        idx += 2
    
    # Process each query
    results = []
    for k, x in queries:
        if k == 0:  # Only the source gnome knows the joke
            results.append(f"1\n{x}")
            continue
        
        # Matrix exponentiation
        g_k = matrix_exponentiation(g, k, N)
        
        # Extract the row for gnome `x - 1` (0-indexed)
        row = g_k[x - 1]
        gnomes = [i + 1 for i in range(N) if row[i] > 0]
        
        if gnomes:
            results.append(f"{len(gnomes)}\n{' '.join(map(str, gnomes))}")
        else:
            results.append("0\n-1")
    
    # Print all results
    sys.stdout.write("\n".join(results) + "\n")
