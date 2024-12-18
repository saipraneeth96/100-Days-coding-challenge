Day 66 coding Statement: Palindromic substrings

Anoop likes strings a lot but he likes palindromic strings more. Today, Anoop has two strings A and B, each consisting of lower case alphabets.

Anoop is eager to know whether it is possible to choose some non empty strings s1 and s2 where s1 is a substring of A, s2 is a substring of B such that s1 + s2 is a palindromic string.

Here '+' denotes the concatenation between the strings.

SOLUTION:

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