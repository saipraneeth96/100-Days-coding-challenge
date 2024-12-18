"""
Day 66 coding Statement: Palindromic substrings

Anoop likes strings a lot but he likes palindromic strings more. Today, Anoop has two strings A and B, each consisting of lower case alphabets.
Anoop is eager to know whether it is possible to choose some non empty strings s1 and s2 where s1 is a substring of A, s2 is a substring of B such that s1 + s2 is a palindromic string.
Here '+' denotes the concatenation between the strings.

Input:

First line of input contains a single integer T denoting the number of test cases.
For each test case:
First line contains the string A
Second line contains the string B.

Output:

For each test case, Print "Yes" (without quotes) if it possible to choose such strings s1 & s2. Print "No" (without quotes) otherwise.

Input:

3
abc
abc
a
b
abba
baab

Output:

Yes
No
Yes

SOLUTION:

"""

def check():
    s1 = input()
    s2 = input()
    
    # Use a set to store characters in A
    set_A = set(s1)
    
    # Check if any character in B is present in set_A
    for char in s2:
        if char in set_A:
            print("YES")
            print(char)
            return
    
    # If no common character is found
    print("NO")

# input number of test cases
t = int(input())

for i in range(t):
    check()
