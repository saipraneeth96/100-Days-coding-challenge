"""
Day 73 coding Statement: Boring String

Day 73 coding Statement : 

A string is called boring if all the characters of the string are same.

You are given a string S of length N, consisting of lowercase english alphabets. 
Find the length of the longest boring substring of S which occurs more than once.

Note that if there is no boring substring which occurs more than once in S, the answer will be 00.

A substring is obtained by deleting some (possibly zero) elements from the beginning of the string and some (possibly zero) elements from the end of the string.

Input Format

The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two lines of input.
The first line of each test case contains an integer N, denoting the length of string S.
The next contains string S.
Output Format

For each test case, output on a new line, the length of the longest boring substring of S which occurs more than once.

 

Sample Input

4

3

aaa

3

abc

5

bcaca

6

caabaa

 

Sample Output

2

0

1

2
"""

def find_longest_boring_substring(T, test_cases):
    results = []
    
    for t in range(T):
        N, S = test_cases[t]
        
        # Dictionary to store counts of boring substrings
        boring_count = {}
        
        max_length = 0
        
        # Traverse the string to identify boring substrings
        i = 0
        while i < N:
            j = i
            # Find a sequence of identical characters
            while j < N and S[j] == S[i]:
                j += 1
            length = j - i
            
            # Add all substrings of this length to the dictionary
            for l in range(1, length + 1):
                substring = S[i:i + l]
                if substring in boring_count:
                    boring_count[substring] += 1
                else:
                    boring_count[substring] = 1
                
                # Check if the substring occurs more than once
                if boring_count[substring] > 1:
                    max_length = max(max_length, l)
            
            # Move to the next unique character sequence
            i = j
        
        results.append(max_length)
    
    return results


# Input Reading and Processing
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    S = input()
    test_cases.append((N, S))

# Finding Results
results = find_longest_boring_substring(T, test_cases)

# Output Results
for res in results:
    print(res)
