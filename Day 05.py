"""
Day 5 coding Statement:  
Write a program to identify if the number is even or odd
"""

# Input a number
num = int(input("Enter a number: "))

# If number is divisible by 2, it is even otherwise odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")