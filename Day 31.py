"""
Day 31 coding Statement:
Write a Program to Toggle each character in a string

Description
Get an input string from user and then convert the lower case of alphabets to upper case and all upper-case alphabets into lower case.
"""

# Original string
text = input("Enter a string: ")

# Toggle the string
new_text = text.swapcase()

# display the result
print(new_text)
