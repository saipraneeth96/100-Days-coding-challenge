"""
Day 99 coding Statement : 

There is a hallway of length N−1 and you have M workers to clean the floor. Each worker is responsible for segment [Li?,Ri?], i.e., the segment starting at Li? and ending at Ri?. The segments might overlap.

Every unit of length of the floor should be cleaned by at least one worker. A worker can clean 1 unit of length of the floor in 1 unit of time and can start from any position within their segment. A worker can also choose to move in any direction. However, the flow of each worker should be continuous, i.e, they can’t skip any portion and jump to the next one, though they can change their direction. What’s the minimum amount of time required to clean the floor, if the workers work simultaneously?

Input:

First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of M+1 lines of input.
First line contains 22 space separated integers N, M, length of the hallway and number of workers.
Each of the next M lines contain 2 space separated integers Li?, Ri?, endpoints of the segment under ith worker.
Output: For each testcase, output in a single line minimum time required to clean the hallway or −1 if it's not possible to clean the entire floor.

 

Sample Input

3

10 3

1 10

1 5

6 10

10 1

2 10

10 2

5 10

1 5

 

Sample Output

3

-1

5

"""

def minimum_cleaning_time(N, M, segments):
        
    # Merge the intervals and check coverage
    segments.sort()
    merged = []
    for start, end in segments:
        if not merged or merged[-1][1] < start - 1:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        
    # Check if the entire range [1, N-1] is covered
    if merged[0][0] > 1 or merged[-1][1] < N - 1:
        return -1
        
    # Find the maximum length of any segment (minimum time required)
    max_time = max(end - start + 1 for start, end in segments)
    return max_time
    
# Input and Output
T = int(input())

for i in range(T):
    # Read N and M
    N, M = map(int, input().split())
    segments = [tuple(map(int, input().split())) for _ in range(M)]
    
    result = minimum_cleaning_time(N, M, segments)
    print(result)
