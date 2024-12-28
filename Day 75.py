"""
Day 75 coding Statement: Candy Problem

You are a person who is always fond of eating candies. Your friend gave you a candy of length N, to eat during the break period of your school.
You start eating this candy from one of the ends.
But as it is not your candy, your friend told you to eat exactly K unit length of candy during each bite.
You will stop eating if the candy's length becomes 00. This means that you have eaten the entire candy.
If at some point of time, the candy's length is positive, but less than K, you cannot take a bite thereafter.
Can you eat the complete candy? If yes, print the number bites it will take, else print −1−1.

Input Format

First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of two spaced integers N, K.
Output Format

For each testcase, print the minimum number of bites you need to eat the complete candy. Print −1−1 if it is not possible to do so.

Sample Input

3

3 1

3 2

0 3

Sample Output

3

-1

0

"""

def candy(n, k):
    # no bites are needed.
    if n == 0:
        return 0
    # you cannot eat the candy completely since the remaining part would be smaller than 𝐾
    elif k == 0 or n % k != 0:
        return -1
    # the number of bites required 
    else:
        return n//k
        

# input number of trst cases
t = int(input())

for i in range(t):
    # N = length of candy
    # K = length of candy you can eat
    N, K = map(int, input().split())
    
    result = candy(N, K)
    
    # print the result
    print(result)
