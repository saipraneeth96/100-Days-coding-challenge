"""
Day 38 coding Statement:
Write a Program to print Non-repeating characters in a string

Description: Get a string as the input from the user and print the non-repeating characters in a string.

Input: Hello

Output: H e o

"""


# input a string
text = input("Enter a string: ")

# calculate frequency of acch character
freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
        
# print keys(characters) that have value(count) 1
for key,value in freq.items():
    if value == 1:
        print(key)
