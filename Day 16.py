"""
Day 16 coding Statement:
Write a program to identify if the number is Perfect number or not

Description

Get the input from the user and check whether that number is a perfect number or not.

E.g. Let number is 28, factors of 28 are 1,2,4,7,14. Now the sum of all these factors are 28 itself.
"""

# input a number
num = int(input("Enter a number: "))

sum = 0

# check for the factors of num and add it to sum
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
        
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")
