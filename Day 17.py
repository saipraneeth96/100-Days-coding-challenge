"""
Day 17 coding Statement:
Write a program to find the Factors of a number
"""


# input a number
num = int(input("Enter a number: "))

factors = []

# check for its factors and add them to a new list
for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)
        
print(factors)        
