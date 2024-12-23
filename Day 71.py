"""
Day 71 coding Statement:
There are N students in a class, where the i-th student has a score of Ai.

The i-th student will boast if and only if the number of students scoring less than or equal Ai? 
is greater than the number of students scoring greater than Ai?.

Find the number of students who will boast.

Input Format

The first line contains T - the number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N - the number of students.
The second line of each test case contains N integers 1,2,…,A1?,A2?,…,AN? - the scores of the students.
Output Format

For each test case, output in a single line the number of students who will boast.

Constraints

1≤10001≤T≤1000
1≤1001≤N≤100
0≤1000≤Ai?≤100
 

Sample Input

3

3

100 100 100

3

2 1 3

4

30 1 30 30

Sample Output

3

2

3
"""

def count_boasting_students(T, test_cases):
    results = []
    for case in test_cases:
        N, scores = case
        scores.sort()  # Sort the scores
        boasting_count = 0
        
        for i in range(N):
            # Count students with scores ≤ scores[i]
            count_le = i + 1  # All elements up to the current index are ≤ scores[i]
            count_gt = N - count_le  # Remaining elements are > scores[i]
            
            if count_le > count_gt:
                boasting_count += 1
        
        results.append(boasting_count)
    return results

# Input Reading
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of students
    scores = list(map(int, input().split()))
    test_cases.append((N, scores))

# Solve and Output
results = count_boasting_students(T, test_cases)
for res in results:
    print(res)
