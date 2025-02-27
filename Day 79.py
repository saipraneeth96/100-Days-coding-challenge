"""
Day 79 coding Statement : 

You are given a binary string S of length N. You can perform the following operation on S:

--Pick any set of indices such that no two picked indices are adjacent.
--Flip the values at the picked indices (i.e. change 0 to 1 and 1 to 0).

For example, consider the string S=1101101.
If we pick the indices {1,3,6}, then after flipping the values at picked indices, we will get 1?10?110?1→0111111.
Note that we cannot pick the set {2,3,5} since 2 and 3 are adjacent indices.

Find the minimum number of operations required to convert all the characters of S to 0.

Input Format

The first line contains a single integer T - the number of test cases. Then the test cases follow.
The first line of each test case contains an integer N - the length of the binary string S.
The second line of each test case contains a binary string S of length N.

Output Format

For each test case, output the minimum number of operations required to convert all the characters of S to 0.

Sample Input

3

6

101001

5

00000

3

111

 

Sample Output

1

0

2

"""

def attempts(n, s):
    # travese the string
    i, count = 0, 0
    
    # count number of groups of consecutive 1's
    while i<n:
        # if s[i] == '1', it marks the start of new group of 1's
        if s[i] == '1' and s[i-1] == '1':
            count += 1
            # skip next index
            i += 2
        else:
            i += 1
            
    return count        
            

# input number of test cases
T = int(input())

for i in range(T):
    # input length of string
    N = int(input())
    # input a binary string
    S = input()
    
    # calculate minimum possible attempts to convert S to all 0's
    result = attempts(N, S)
    
    # display the result
    print(result)
