"""
Day 4 coding Statement: 
Write a program to identify if the a number is positive or negative
"""

# Input a number 'num'
num = int(input("Enter a number: "))

# Check if it is positive, negative or none
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Neither positive nor negative")
