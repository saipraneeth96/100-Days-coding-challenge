"""
Day 62 coding Statement : Gold Mining

Anusree has decided to go to a gold mine along with N of his friends (thus, total N+1 people including Anusree go to the gold mine).

The gold mine contains a total of X kg of gold. Every person has the capacity of carrying up atmost Y kg of gold.

Will Anusree and his friends together be able to carry up all the gold from the gold mine assuming that they can go to the mine exactly once.

Input Format

First line will contain T, number of testcases. Then the testcases follow. Each testcase contains of a single line of input, three integers N, X, Y.

Output Format

For each testcase, output "YES" if you and your friends can carry all the gold, otherwise output "NO".

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Sample Input 1

3

2 10 3

2 10 4

1 5 10

Sample Output 1

NO

YES

YES

SOLUTION:
"""

# enter number of testcases
t = int(input())

for i in range(t):
    # n = number of friends
    # x = kgs of gold
    # y = kgs of gold each person can carry
    n, x, y = map(int, input().split())
    
    # total gold they can carry
    total = (n+1) * y
    
    if total >= x:
        print("YES")
    else:
        print("NO")
