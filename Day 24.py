"""
Day 24 coding Statement:
Write a program to print Pyramid pattern using stars

Description

Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.

Input

4

Output

*
***
*****
*******

"""

# input number of steps in the pyramid
num = int(input("Enter number of pyramid steps: "))

# loop untill num 
for i in range(1,num+1):
    # print number of stars corresponding to row number
    print("*"*i)
