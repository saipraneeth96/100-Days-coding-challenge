"""
Day 39 coding Statement:
Write a Program to check if two strings are Anagram or not

Description: Get two strings as input from the user and check whether it is Anagram or not.

Input: sunlight thgiluns

Output: Anagram
"""


# input two strings
first = input("Enter first string: ").lower()
second = input("Enter second string: ").lower()

if len(first) != len(second):
    print("Not an anagram")
else:
    # iterate through each character of first string
    for char in first:
        # if the same is found in second string remove it from second
        if char in second:
            # reemove the first occurance of the character
            second = second.replace(char,"", 1)
        else:
            print("Not an anagram")
            break
    # if all characters are removed then second string is empty
    # hence the string is anagram
    else:
        print("Anagram")
