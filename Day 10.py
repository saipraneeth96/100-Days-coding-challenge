"""
Day 10 coding Statement:
Write a program to find Factorial of a number
"""


# Input a number 
num = int(input("Enter a number: "))

# To store the factorial of number
prod = 1

# Calculating factorial
for i in range(num, 0, -1):
    prod = prod * i
    
print(prod)    
