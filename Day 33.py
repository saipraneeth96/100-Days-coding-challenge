"""
Day 33 coding Statement:
Write a Program to check if String is a palindrome or not
"""

# input a string
s = input("Enter a string: ").lower()

# check if reverse of it is same as original
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")