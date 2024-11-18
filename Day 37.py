"""
Day 37 coding Statement:
Write a Program to calculate the Frequency of characters in a string

Description: Get a string as the input from the user and find the frequency of characters in the string.

Input: program

Output:
The frequency of a is 1
The frequency of g is 1
The frequency of m is 1
The frequency of o is 1
The frequency of p is 1
The frequency of r is 2
"""

# input a string
s = input("Enter s atring: ")

# empty dictionary to store the frequency of each character
freq = {}

# calculate count of each character ad add to dictionary
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
        
# Sort the dictionary by keys
sorted_freq = dict(sorted(freq.items()))  
     
# display each item with its value        
for key, value in sorted_freq.items():
    print(f"The frequency of {key} in {value}")
