"""
Day 32 coding Statement:
Write a Program to Remove vowels from a string
"""

# input a string
text = input("Enter a string: ")

vowels = "aeiouAEIOU"

# loop through each character
for char in text:
    # if current character is a vowel
    if char in vowels:
        # remove this character
        text = text.replace(char, "")

# display the result
print(text) 
