"""
Day 36 coding Statement:
Write a Program to Capitalize the first and last letter of each word of a string.
"""

# input a string
text = input("Enter some text: ")

# capitalize first letter
# text[0].upper()

# capita;ize last letter
# text[1:-1].upper()

# display final result
print(text[0].upper() + text[1:-1] + text[-1].upper())