Day 76 coding Statement: Minimum steps

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
