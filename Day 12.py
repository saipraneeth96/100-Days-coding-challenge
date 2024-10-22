"""
Day 12 coding Statement:
Write a program to find Sum of digits of a number
"""


# Input a number
num = int(input("Enter a number: "))

# A variable to store sum
sum = 0

# Extracting each digit and adding to sum
while num != 0:
    sum = sum + (num % 10)
    num = num // 10
    
print(sum)    
