"""
Day 47 coding Statement:
Write Program to find longest palindrome in an array
Description: Get an array as the input from the user and find the longest palindrome in that array.

Input

Enter the size of array: 3

Enter the elements of array

121 10456 1000001

Output: 1000001
"""


def is_palindrome(number):
    # Check if a number is a palindrome
    # Convert number to string
    return number == number[::-1]

def find_longest_palindrome(arr):
    # Find the longest palindrome in an array
    longest_palindrome = None
    
    for number in arr:
        if is_palindrome(number):
            if longest_palindrome is None or len(str(number)) > len(str(longest_palindrome)):
                longest_palindrome = number

    return longest_palindrome

# Input
size = int(input("Enter the size of array: "))

array = []
print("Enter the elements of array:")
for i in range(size):
    array.append(input())


# Find the longest palindrome
longest_palindrome = find_longest_palindrome(array)

# Output
if longest_palindrome:
    print(longest_palindrome)
else:
    print("No palindrome found in the array.")
