Day 78 Coding Statement:

For a given array B1,B2,…,BM of length at least 3, let's define its weight as the largest value of (Bi−Bj)⋅(Bj
−Bk) over all possible triples(i,j,k) with 1≤i,j,k≤M and i!=j, j!=k, k!=i.
You are given a sorted array A1,A2,…,AN(that is, A1≤A2≤…≤AN).
Calculate the sum of weights of all contiguous subarrays of A of length at least 3. That is, count the sum
of weights of arrays[Ai,Ai+1,…,Aj] over all 1≤i<j≤N with j−i≥2.

def compute(arr):
    n = len(arr)
    total = 0
    
    for i in range(n - 2):
        j = i + 1
        for k in range(i + 2, n):
            mid = (arr[i] + arr[k]) / 2
            while (j < (k - 1)) and abs(arr[j + 1] - mid) <= abs(arr[j] - mid):
                j += 1
                weight = (arr[i] - arr[j]) * (arr[j] - arr[k])
                total += weight
    return total
 
# input number of test cases
t = int(input())
for t in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(compute(array))
