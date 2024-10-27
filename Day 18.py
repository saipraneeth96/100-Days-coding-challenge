"""
Day 18 coding Statement:
Write a program to Add two fractions

Description

Get the values for numerator and denominator of two fractions, then add that fractions. Consider the following format

x3/y3 = (x1/y1) + (x2/y2)

here x3 = (x1*y2) + (x2*y1) and y3 = (y1*y2)
"""


import math

# input the fractions
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# calculate resultant
x3 = x1 * y2 + x2 * y1
y3 = y1 * y2

# divide both fractions bt greatest common divisior
hcf = math.gcd(x3, y3)
x3 = x3 // hcf
y3 = y3 // hcf

# display the result
if y3 == 1:
    print(f"{x3}/1")
else:
    print(f"{x3}/{y3}")
