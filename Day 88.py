"""
Day 88 coding Statement : 

Blobo2 is in his practical exam. The teacher gave him a permutation A of N integers.

The teacher has allowed Blobo2 to make a certain type of operation on the permutation. In one operation, he can:

Apply left shift on the permutation. In other words, he can take the first element of the permutation 
and move it to the back of the permutation.
The teacher has asked Blobo2 to find the lexicographically smallest permutation possible 
after applying any (possibly zero) number of given operations.

Since Blobo2 wants to impress his teacher, he decided to perform at most two swaps in addition to the allowed operation.

Find the lexicographically smallest possible permutation Blobo2 can generate after applying at most two swaps
and any number of given operations.

Note:

- A permutation of size N consists of all integers from 1 to N exactly once.
  During a swap, Blobo2 can choose any two indices i and j (1≤i,j≤N) and swap Ai? with Aj?.
- A permutation X is said to be lexicographically smaller than a permutation Y if Xi?<Yi?,
  where i is the first index where both the permutations differ.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
The second line will contain the integer N, denoting the size of the permutation.
The third line contains N distinct integers, the elements of the permutation A.
Output Format

Output the lexicographically smallest possible permutation Blobo2 can generate after applying at most 
two swaps and any number of given operations.

Sample Input
2
5
5 2 1 4 3
5
3 5 2 1 4

Sample Output

1 2 3 4 5
1 2 3 4 5
"""

def lexographically_smallest_permutation(N, A):
    
    # Generate all rotations
    rotations = [A[i:] + A[:i] for i in range(N)]
    
    # Find the lexicographically smallest rotation
    smallest_rotation = min(rotations)
    
    # Now we will try to perform at most two swaps on the smallest rotation
    smallest_permutation = smallest_rotation[:]
    
    # Try all pairs of indices for swapping
    for i in range(N):
        for j in range(i + 1, N):
            # Swap elements at index i and j
            swapped = smallest_rotation[:]
            swapped[i], swapped[j] = swapped[j], swapped[i]
                
            # Check if the new permutation is smaller
            if swapped < smallest_permutation:
                smallest_permutation = swapped
                
            # Try another swap with a different pair
            for k in range(N):
                for l in range(k + 1, N):
                    if k != i and k != j and l != i and l != j:
                        double_swapped = swapped[:]
                        double_swapped[k], double_swapped[l] = double_swapped[l], double_swapped[k]
                            
                        # Check if the new permutation is smaller
                        if double_swapped < smallest_permutation:
                            smallest_permutation = double_swapped
                
    return smallest_permutation            


# input number of test cases
T = int(input())

for i in range(T):
    # input the size of permutation
    N = int(input())
    # elements of permutation A
    A = list(map(int, input().split()))
    
    result = lexographically_smallest_permutation(N, A)
    
    # Display the output
    print(" ".join(map(str, result)))
