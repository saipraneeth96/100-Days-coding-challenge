"""
Day 76 coding Statement: Minimum steps

You are given N integers. In each step you can choose some K of the remaining numbers and delete them, if the following condition holds: Let the K numbers you've chosen be a1, a2, a3, ..., aK in sorted order. Then, for each i ≤ K - 1, ai+1 must be greater than or equal to ai * C.

You are asked to calculate the maximum number of steps you can possibly make.

Input

The first line of the input contains an integer T, denoting the number of test cases. The description of each testcase follows.
The first line of each testcase contains three integers: N, K, and C
The second line of each testcase contains the N initial numbers
Output

For each test case output the answer in a new line.

Sample Input

2

6 3 2

4 1 2 2 3 1

6 3 2

1 2 2 1 4 4

Outpu

1

2

"""

def minsteps(n, k, c, nums):
    # Sort the array
    nums.sort()
    count = 0
    
    while len(nums) >= k:
        valid = True
        # Check if the first k elements satisfy the condition
        for i in range(k - 1):
            if nums[i + 1] < nums[i] * c:
                valid = False
                break
            if valid:
                count += 1
                # Remove the first k elements
                nums = nums[k:]
            else:
                break
    
    return count

# Input number of test cases
t = int(input())

for _ in range(t):
    # Read N, K, C
    N, K, C = map(int, input().split())
    # Read the array
    array = list(map(int, input().split()))
    
    # Calculate the number of steps
    steps = minsteps(N, K, C, array)
    
    # Display the result
    print(steps)
