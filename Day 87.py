"""
Day 87 coding Statement : 

There are N stones in a pond, each having a value Ai? written on it. 
A frog is at stone 1 and wants to reach stone N. The frog can jump from a stone i to any stone j(j>i). 
Let d be the length of subarray (i.e. j−i+1), then the energy required for the jump is (d⋅Ai?)−Aj?. 
Find the minimum non-negative amount of energy required by the frog to reach the N-th stone.

Note: It is possible that the total amount of energy required is negative, 
in that case, you should print the minimum non-negative value (i.e. 0).

Input Format

The first line contains an integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N - the number of stones.
The second line contains N integers denoting the numbers written on the stones.
Output Format

For each test case output a single integer - the minimum non-negative energy required by the frog.

Sample Input

4

3

6 1 3

4

3 1 10 4

3

7 9 1

2

1 5

Sample Output

10

4

20

0

"""

def minimum_energy(T, test_cases):
    results = []
    for t in range(T):
        N = test_cases[t][0]
        A = test_cases[t][1]
        
        # Initialize DP array
        dp = [float('inf')] * N
        dp[0] = 0  # Starting point
        
        for j in range(1, N):
            for i in range(j):
                d = j - i + 1
                energy = (d * A[i]) - A[j]
                dp[j] = min(dp[j], dp[i] + energy)
        
        # Ensure non-negative energy
        results.append(max(dp[N-1], 0))
    
    return results


# Input Processing
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

# Solve and Output Results
results = minimum_energy(T, test_cases)
for result in results:
    print(result)
