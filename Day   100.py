"""
Day 100 coding Statement : 

You have prepared four problems. The difficulty levels of the problems are A1?,A2?,A3?,A4? respectively. A problem set comprises at least two problems and no two problems in a problem set should have the same difficulty level. A problem can belong to at most one problem set. Find the maximum number of problem sets you can create using the four problems.

Input Format

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains four space-separated integers A1?, A2?, A3?, A4?, denoting the difficulty level of four problems.
Output Format

For each test case, print a single line containing one integer - the maximum number of problem sets you can create using the four problems.


Sample Input

3

1 4 3 2

4 5 5 5

2 2 2 2

 

Sample Output

2

1

0
"""
def difficulty(array):
     # Count the frequency of each difficulty level
    freq = {}
    for d in array:
        freq[d] = freq.get(d, 0) + 1
        
    # Convert frequency dictionary to a list of counts
    freq_counts = sorted(freq.values(), reverse=True)
    sets = 0
        
    while len(freq_counts) > 1:
        # Take two highest frequencies
        freq_counts[0] -= 1
        freq_counts[1] -= 1
            
        # Remove zeroes and re-sort
        freq_counts = [f for f in freq_counts if f > 0]
        freq_counts.sort(reverse=True)
            
        sets += 1
        
        return sets

# input number of test cases
T = int(input())

for i in range(T):
    # set of 4 problems
    array = []
    for j in range(4):
        array.append(int(input()))
    
    result = difficulty(array)
    
    #display the output
    print(result)
