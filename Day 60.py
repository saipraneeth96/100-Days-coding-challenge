"""
Day 60 coding Statement : Good Weather

The weather report of Magicland is Good if the number of sunny days in a week is strictly greater than the number of rainy days.

Given 7 integers A1,A2,A3,A4,A5,A6,A7 where Ai=1 denotes that the ith day of week in Magicland is a sunny day,
Ai=0 denotes that the ith day in Magicland is a rainy day. Determine if the weather report of Magicland is Good or not.

Input Format

First line will contain T, number of testcases. Then the testcases follow.

Each testcase contains of a single line of input, 7 space separated integers A1,A2,A3,A4,A5,A6,A7.

Output Format

For each testcase, print "YES" if the weather report of Magicland is Good, otherwise print "NO". Print the output without quotes.

You may print each character of the string in uppercase or lowercase
(for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Sample Input 1

4

1 0 1 0 1 1 1

0 1 0 0 0 0 1

1 1 1 1 1 1 1

0 0 0 1 0 0 0

Sample Output 1

YES

NO

YES

NO

SOLUTION:

"""

t = int(input())

for i in range(t):
    # input climate type  in each day of the week
    a1, a2, a3, a4, a5, a6, a7 = map(int, input().split())
    
    count_of_ones = 0
    for i in [a1, a2, a3, a4, a5, a6, a7]:
        if i == 1:
            count_of_ones += 1
    count_of_zeros = 7 - count_of_ones
    
    if count_of_ones > count_of_zeros:
        print("YES")
    else:
        print("NO")
