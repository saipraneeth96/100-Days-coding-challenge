"""
Day 30 coding Statement:
Write a Program to print Length of the string without using strlen() function
"""


# input a string
s1 = input("Enter a string: ")

# variable to store the count of characters
count = 0

# calculating length
for ch in s1:
    count += 1
    
# display the result
print(count)