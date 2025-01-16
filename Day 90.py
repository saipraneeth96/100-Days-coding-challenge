"""
Day 90 coding Statement : 

Gru has a string S of length N, consisting of only characters a and b for banana and P points to spend.

Now Gru wants to replace and/or re-arrange characters of this given string to get the lexicographically smallest string possible. 
For this, he can perform the following two operations any number of times.

Swap any two characters in the string. This operation costs 11point. (any two, need not be adjacent)
Replace a character in the string with any other lower case english letter. This operation costs 2 points.
Help Gru in obtaining the lexicographically smallest string possible, by using at most P points.


Input:

First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains two lines of input, first-line containing two integers N , P.
The second line contains a string S consisting of N characters.
Output: For each testcase, output in a single containing the lexicographically smallest string obtained.

 

Sample Input

1

3 3

bba

Sample Output

aab
"""

def lexicographically_smallest_string(N, P, S):
    S = list(S)  # Convert string to list for mutability
    target = sorted(S)  # Target lexicographically smallest string
    i = 0
        
    # Attempt to transform S into the target
    while P > 0 and i < N:
        # If already matching, move to the next character
        if S[i] == target[i]:
            i += 1
            continue
            
        # Calculate the cost of replacement and swap
        if S[i] != target[i]:
            if target[i] not in S[i + 1:]:
                # Replace S[i] with target[i] if it's not in the remaining string
                if P >= 2:
                    P -= 2
                    S[i] = target[i]
            else:
                # Swap S[i] with the next occurrence of target[i]
                j = S.index(target[i], i + 1)
                if P >= 1:
                    P -= 1
                    S[i], S[j] = S[j], S[i]
        i += 1
    
    return ''.join(S)

# Input number of test cases
T = int(input())

for i in range(T):
    N, P = map(int, input().split())
    S = input().strip()
    
    answers = lexicographically_smallest_string(N, P, S)
    
    # display the output
    print(answers)
